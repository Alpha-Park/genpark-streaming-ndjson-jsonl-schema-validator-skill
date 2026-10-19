"""Streaming NDJSON & JSONL Schema Validator.
100% Python Standard Library.
"""
import json

class StreamingNdjsonSchemaValidator:
    """Ultra-low-latency incremental line validator with chunk boundary reassembly, schema auditing, and quarantine logging."""

    @staticmethod
    def validate_stream(chunks: list, required_keys: list) -> dict:
        buffer = ""
        valid_records = []
        quarantine = []

        for chunk in chunks:
            buffer += chunk
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                    missing = [k for k in required_keys if k not in record]
                    if missing:
                        quarantine.append({"raw": line, "error": f"Missing required keys: {missing}"})
                    else:
                        valid_records.append(record)
                except Exception as e:
                    quarantine.append({"raw": line, "error": str(e)})

        if buffer.strip():
            try:
                record = json.loads(buffer.strip())
                valid_records.append(record)
            except Exception as e:
                quarantine.append({"raw": buffer.strip(), "error": f"Incomplete line: {e}"})

        return {
            "valid_count": len(valid_records),
            "quarantine_count": len(quarantine),
            "quarantine_details": quarantine,
            "valid_records_preview": valid_records[:2]
        }
