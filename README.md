# genpark-streaming-ndjson-jsonl-schema-validator-skill

[![Verified by Smithery](https://smithery.ai/badge/@Alpha-Park/genpark-streaming-ndjson-jsonl-schema-validator-skill)](https://smithery.ai/servers/@Alpha-Park/genpark-streaming-ndjson-jsonl-schema-validator-skill)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![Website](https://img.shields.io/badge/Website-GenPark.ai-green)](https://www.genpark.ai)

> Ultra-low-latency incremental line validator with chunk boundary reassembly, schema auditing, and quarantine logging

## Quick Installation & MCP Integration
Add to your Claude Desktop or Cursor configuration:
```json
{
  "mcpServers": {
    "genpark-streaming-ndjson-jsonl-schema-validator-skill": {
      "command": "python",
      "args": ["mcp_server.py"]
    }
  }
}
```

## Zero Dependencies
Implemented entirely in Python 3 standard library.
