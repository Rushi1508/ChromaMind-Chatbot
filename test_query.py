"""
Tests the ChromaDB query functionality.
"""
from llm_response import generate_llm_response
from knowledge_base import query_knowledge

# Sample Queries
queries = [
    "What services do you provide?",
    "Tell me about your logistics solutions.",
    "Do you offer financial services?",
    "How can I contact you?",
    "What industries do you work with?",
    "Do you handle manpower supply?",
    "Tell me about space exploration."  # Out-of-bound query
]

for query in queries:
    print(f"🟢 Query: {query}")
    retrieved_text = query_knowledge(query)
    
    if isinstance(retrieved_text, list):  # If knowledge found, send to LLM
        response = generate_llm_response(f"Generate a response for: {retrieved_text[0]}")
    else:
        response = retrieved_text  # Direct response (fallback)

    print(f"🔹 Response: {response}\n")
