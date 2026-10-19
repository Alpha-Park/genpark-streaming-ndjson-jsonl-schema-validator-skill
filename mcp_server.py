"""MCP Server wrapper for Streaming NDJSON Schema Validator."""
import json
import sys
from client import StreamingNdjsonSchemaValidator

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "validate_ndjson_stream",
                    "description": "Incrementally assemble chunks and validate streaming JSONL lines with quarantine isolation",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "chunks": {"type": "array", "items": {"type": "string"}},
                            "required_keys": {"type": "array", "items": {"type": "string"}}
                        },
                        "required": ["chunks", "required_keys"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        res = StreamingNdjsonSchemaValidator.validate_stream(
            args.get("chunks", []),
            args.get("required_keys", [])
        )
        return {
            "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
        }
    return {}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            try:
                r = json.loads(line)
                out = handle_request(r)
                print(json.dumps(out), flush=True)
            except Exception as e:
                print(json.dumps({"error": str(e)}), flush=True)
