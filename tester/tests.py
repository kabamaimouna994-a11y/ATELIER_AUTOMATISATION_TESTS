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
        
        # Test 3 : Champ 'content' présent et de type string
        has_content = "content" in data and isinstance(data["content"], str) and len(data["content"]) > 0
        tests.append({"name": "Field 'content' present & string", "status": "PASS" if has_content else "FAIL"})
        
        # Test 4 : Champ 'author' présent et de type string
        has_author = "author" in data and isinstance(data["author"], str)
        tests.append({"name": "Field 'author' present & string", "status": "PASS" if has_author else "FAIL"})
        
        # Test 5 : Champ 'length' présent et de type int
        has_length = "length" in data and isinstance(data["length"], int)
        tests.append({"name": "Field 'length' present & int", "status": "PASS" if has_length else "FAIL"})
    else:
        for name in ["Valid JSON Payload", "Field 'content' present & string", "Field 'author' present & string", "Field 'length' present & int"]:
            tests.append({"name": name, "status": "FAIL", "details": "Skipped due to non-200 response"})

    # Test 6 : Latence QoS inférieure à 1500ms
    t6 = {"name": "Latency < 1500ms", "status": "PASS" if res["latency_ms"] < 1500 else "FAIL", "details": f"{res['latency_ms']}ms"}
    tests.append(t6)
    
    return tests
