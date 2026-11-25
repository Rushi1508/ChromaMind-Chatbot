import os
import sys
import tempfile

# Must run before knowledge_base is imported: it opens the DB at import time.
os.environ["CHROMA_DB_PATH"] = tempfile.mkdtemp(prefix="chroma_test_")
os.environ["COLLECTION_NAME"] = "test_collection"
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
