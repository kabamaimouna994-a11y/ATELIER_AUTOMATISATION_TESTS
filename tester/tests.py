def run_tests(res):
    tests = []
    
    # Test 1 : Code HTTP 200
    t1 = {"name": "HTTP Status 200", "status": "PASS" if res["status_code"] == 200 else "FAIL"}
    if t1["status"] == "FAIL": 
        t1["details"] = f"Got status {res['status_code']} (Error: {res.get('error')})"
    tests.append(t1)
    
    if res["status_code"] == 200:
        data = res["json"]
        
        # Test 2 : Réponse JSON valide
        tests.append({"name": "Valid JSON Payload", "status": "PASS" if isinstance(data, dict) else "FAIL"})
        
        # Test 3 : Champ 'name' présent et string
        has_name = "name" in data and isinstance(data["name"], str)
        tests.append({"name": "Field 'name' present & string", "status": "PASS" if has_name else "FAIL"})
        
        # Test 4 : Champ 'age' présent et valide (int ou None)
        has_age = "age" in data and (isinstance(data["age"], int) or data["age"] is None)
        tests.append({"name": "Field 'age' present & valid type", "status": "PASS" if has_age else "FAIL"})
        
        # Test 5 : Champ 'count' présent et int
        has_count = "count" in data and isinstance(data["count"], int)
        tests.append({"name": "Field 'count' present & int", "status": "PASS" if has_count else "FAIL"})
    else:
        for name in ["Valid JSON Payload", "Field 'name' present & string", "Field 'age' present & valid type", "Field 'count' present & int"]:
            tests.append({"name": name, "status": "FAIL", "details": "Skipped due to non-200 response"})

    # Test 6 : Latence QoS inférieure à 1500ms
    t6 = {"name": "Latency < 1500ms", "status": "PASS" if res["latency_ms"] < 1500 else "FAIL", "details": f"{res['latency_ms']}ms"}
    tests.append(t6)
    
    return tests
