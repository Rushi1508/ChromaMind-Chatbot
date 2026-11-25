"""
Loads knowledge entries from a JSON file into ChromaDB.

Usage: python populate_knowledge.py [path/to/knowledge.json]   (default: data/knowledge.json)
Each entry needs "id", "text" and a non-empty "metadata" object.
"""
import json
import sys

from knowledge_base import add_knowledge

path = sys.argv[1] if len(sys.argv) > 1 else "data/knowledge.json"
with open(path, encoding="utf-8") as f:
    knowledge_entries = json.load(f)

failed = 0
for entry in knowledge_entries:
    failed += "error" in add_knowledge(entry["id"], entry["text"], entry["metadata"])

print(f"Loaded {len(knowledge_entries) - failed} of {len(knowledge_entries)} entries from {path}.")
sys.exit(1 if failed else 0)
