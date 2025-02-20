import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models.request_models import UserInitRequest, KnowledgeQueryRequest, LLMRequest, LanguageRequest, TranslationRequest
from models.response_models import KnowledgeQueryResponse, UserHistoryResponse, LLMResponse, LanguageResponse, TranslationResponse
from agents.knowledge_agent import query_knowledge
from agents.history_agent import initialize_user_history, get_user_history
from agents.llm_agent import generate_llm_response
from agents.language_agent import set_language, user_languages
from agents.translation_agent import translate_text
from config.logging_config import logger

# ✅ Initialize FastAPI App
app = FastAPI(title="Way2Reach Chatbot API", version="1.2")


@app.get("/")
async def root():
    """API Status Check."""
    return {"message": "Welcome to Way2Reach Chatbot API!", "status": "running"}


@app.get("/get_user_history/{user_id}")
async def get_history_endpoint(user_id: str):
    """Retrieves the chat history of a user while ensuring proper Unicode handling."""
    logger.info(f"📜 Fetching history for user: {user_id}")
    history = get_user_history(user_id)

    if not history:
        logger.warning(f"⚠️ No history found for user: {user_id}")
        raise HTTPException(status_code=404, detail="No history found for this user.")

    # ✅ Preserve Unicode in the response
    return JSONResponse(content={"user_id": user_id, "history": history}, media_type="application/json")

@app.post("/initialize_user/")
async def initialize_user(data: UserInitRequest):
    """
    Initializes a new user profile and conversation history.
    """
    logger.info(f"🆕 Initializing user: {data.user_id} ({data.user_name})")
    initialize_user_history(data.user_id, data.user_name)
    return {"message": f"✅ User {data.user_name} initialized successfully.", "user_id": data.user_id}


@app.post("/query_knowledge/")
async def knowledge_endpoint(data: KnowledgeQueryRequest):
    """Handles user queries and retrieves responses from ChromaDB or LLM, ensuring Unicode compatibility."""
    logger.info(f"📥 Query from {data.user_id}: {data.query_text}")

    try:
        response = query_knowledge(data)

        user_lang = user_languages.get(data.user_id, "en")
        if user_lang != "en":
            translation_request = TranslationRequest(text=response.response, target_language=user_lang)
            response.response = translate_text(translation_request).translated_text

        from services.history_manager import save_interaction
        save_interaction(data.user_id, data.query_text, response.response)

        return JSONResponse(content={"query": response.query, "response": response.response}, media_type="application/json")

    except Exception as e:
        logger.error(f"❌ Query Error: {str(e)}", exc_info=True)
        return JSONResponse(status_code=500, content={"error": "An error occurred while processing your query."})


@app.post("/generate_llm_response/")
async def generate_llm_endpoint(data: LLMRequest):
    """Generates responses using Groq LLM, ensuring Unicode handling."""
    logger.info(f"🤖 LLM Query: {data.prompt}")

    try:
        response = generate_llm_response(data)

        user_lang = user_languages.get(data.user_id, "en")
        if user_lang != "en":
            translation_request = TranslationRequest(text=response.generated_text, target_language=user_lang)
            response.generated_text = translate_text(translation_request).translated_text

        return JSONResponse(content={"generated_text": response.generated_text}, media_type="application/json")

    except Exception as e:
        logger.error(f"❌ LLM Query Error: {str(e)}", exc_info=True)
        return JSONResponse(status_code=500, content={"error": "An error occurred while processing your LLM request."})


@app.post("/set_language/")
async def set_language_endpoint(data: LanguageRequest):
    """Sets the user's preferred language."""
    return set_language(data)


@app.post("/translate_text/")
async def translate_text_endpoint(data: TranslationRequest):
    """Handles text translation."""
    return translate_text(data)


if __name__ == "__main__":
    import uvicorn
    logger.info("🚀 Starting FastAPI Server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
