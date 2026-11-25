"""Retrieval tests for the ChromaDB knowledge base (no LLM or network calls beyond the first model download)."""
import json
from pathlib import Path

import knowledge_base as kb
from config.settings import FALLBACK_REPLY

DATA = json.loads((Path(__file__).parent.parent / "data" / "knowledge.json").read_text(encoding="utf-8"))


def test_empty_collection_returns_fallback():
    assert kb.collection.count() == 0
    assert kb.query_knowledge("anything") == FALLBACK_REPLY


def test_query_returns_most_relevant_entry():
    for e in DATA:
        assert "error" not in kb.add_knowledge(e["id"], e["text"], e["metadata"])

    results = kb.query_knowledge("What are the support hours?")
    assert isinstance(results, list) and len(results) == 3
    assert "Monday to Friday" in results[0]


def test_add_existing_id_overwrites():
    kb.add_knowledge("6", "Support is available on weekends only.", {"category": "Support"})
    assert kb.collection.get(ids=["6"])["documents"] == ["Support is available on weekends only."]


def test_delete():
    kb.delete_knowledge("6")
    assert kb.collection.get(ids=["6"])["ids"] == []
