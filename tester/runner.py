from datetime import datetime
from tester.client import call_api
from tester.tests import run_tests

def execute_run():
    latencies = []
    last_res = None
    
    # 3 appels consécutifs pour mesurer la latence (avg / p95)
    for _ in range(3):
        res = call_api()
        latencies.append(res["latency_ms"])
        last_res = res
        
    tests_results = run_tests(last_res)
    
    passed = sum(1 for t in tests_results if t["status"] == "PASS")
    failed = sum(1 for t in tests_results if t["status"] == "FAIL")
    
    latencies.sort()
    avg_lat = sum(latencies) / len(latencies)
    p95_lat = latencies[int(len(latencies) * 0.95)] if len(latencies) > 1 else latencies[0]
    
    error_rate = 0.0 if last_res["status_code"] == 200 else 1.0

    run_data = {
        "api": "Quotable",
        "timestamp": datetime.now().isoformat(),
        "summary": {
            "passed": passed,
            "failed": failed,
            "error_rate": error_rate,
            "latency_ms_avg": round(avg_lat, 2),
            "latency_ms_p95": round(p95_lat, 2)
        },
        "tests": tests_results
    }
    return run_data
