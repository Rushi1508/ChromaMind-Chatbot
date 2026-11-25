# ChromaMind Chatbot

A retrieval-augmented chatbot: it finds relevant entries in a ChromaDB knowledge base and has an LLM answer from them, in a Streamlit chat UI.

![Screenshot](docs/screenshot.png) <!-- TODO: add screenshot -->

## What it does

1. `populate_knowledge.py` reads entries from `data/knowledge.json`, embeds each one with `all-MiniLM-L6-v2`, and stores it in a local ChromaDB collection. Re-running it overwrites entries that have the same `id`.
2. In the Streamlit app, your question is embedded the same way and the 3 nearest entries are retrieved. Retrieval has no similarity cutoff, so you always get the closest 3, even if they are only loosely related.
3. Those entries are sent as context, together with the question, to a Llama model on the Groq API, and the model's answer is shown in the chat.

If the knowledge base is empty, the app returns a configurable fallback reply.

## Stack

- **ChromaDB**: persistent local vector store
- **sentence-transformers** (`all-MiniLM-L6-v2`): embeddings
- **Groq API** (`llama-3.1-8b-instant` by default): answer generation
- **Streamlit**: chat UI
- **pytest**: retrieval tests

## Project layout

```
config/settings.py      settings read from env vars / .env
knowledge_base.py       ChromaDB add / update / delete / query
llm_response.py         Groq chat-completions call
populate_knowledge.py   loads data/knowledge.json into ChromaDB
streamlit_app.py        chat UI (entry point)
data/knowledge.json     small generic sample dataset
tests/                  pytest tests for retrieval
```

## Setup

Tested with Python 3.12.

```bash
git clone https://github.com/Rushi1508/ChromaMind-Chatbot.git
cd ChromaMind-Chatbot
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then set GROQ_API_KEY
```

Get a free API key at https://console.groq.com. All settings live in `.env` (see `.env.example`):

| Variable | Default | Purpose |
|---|---|---|
| `GROQ_API_KEY` | (empty) | Groq API key, required for answers |
| `GROQ_MODEL` | `llama-3.1-8b-instant` | Groq model name |
| `CHROMA_DB_PATH` | `./chroma_db` | where ChromaDB stores its data |
| `COLLECTION_NAME` | `knowledge_base` | ChromaDB collection |
| `BOT_NAME` | `Assistant` | name shown in the UI and system prompt |
| `SYSTEM_PROMPT` | generic RAG prompt | system message sent to the LLM |
| `FALLBACK_REPLY` | generic message | reply when the knowledge base is empty |

On first run, sentence-transformers downloads the embedding model (about 90 MB).

## Populate the knowledge base

```bash
python populate_knowledge.py                    # loads data/knowledge.json
python populate_knowledge.py path/to/mine.json  # or your own file
```

Each entry looks like `{"id": "1", "text": "...", "metadata": {"category": "..."}}`. Metadata must not be empty.

## Run

```bash
streamlit run streamlit_app.py
```

Open http://localhost:8501 and ask something like "What are the support hours?".

## Tests

```bash
pytest
```

The tests use a temporary ChromaDB directory and check retrieval, overwrite, and delete. They do not call the LLM.

## License

MIT
