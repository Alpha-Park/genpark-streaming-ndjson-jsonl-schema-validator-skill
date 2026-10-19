"""Example usage for Streaming NDJSON & JSONL Schema Validator."""
from client import StreamingNdjsonSchemaValidator

if __name__ == "__main__":
    chunks = ['{"id": 1, "status": "active"}\n{"id": 2', ', "status": "pending"}\n']
    res = StreamingNdjsonSchemaValidator.validate_stream(chunks, required_keys=["id", "status"])
    print("Stream validation result:", res)
