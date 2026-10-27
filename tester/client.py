import requests
import time

def call_api():
    url = "https://api.quotable.io/random"
    start_time = time.time()
    try:
        response = requests.get(url, timeout=3.0)
        latency_ms = round((time.time() - start_time) * 1000, 2)
        
        if response.status_code == 429:
            return {"status_code": 429, "latency_ms": latency_ms, "error": "Rate limit exceeded"}
        
        return {
            "status_code": response.status_code,
            "latency_ms": latency_ms,
            "json": response.json() if response.status_code == 200 else None,
            "error": None
        }
    except requests.exceptions.Timeout:
        latency_ms = round((time.time() - start_time) * 1000, 2)
        return {"status_code": 504, "latency_ms": latency_ms, "error": "Timeout"}
    except Exception as e:
        latency_ms = round((time.time() - start_time) * 1000, 2)
        return {"status_code": 500, "latency_ms": latency_ms, "error": str(e)}
