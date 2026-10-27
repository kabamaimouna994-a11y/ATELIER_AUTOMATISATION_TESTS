import sqlite3
import json

DB_NAME = "runs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            passed INTEGER,
            failed INTEGER,
            error_rate REAL,
            avg_latency REAL,
            p95_latency REAL,
            details TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_run(run_data):
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    summary = run_data["summary"]
    cursor.execute('''
        INSERT INTO runs (timestamp, passed, failed, error_rate, avg_latency, p95_latency, details)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        run_data["timestamp"],
        summary["passed"],
        summary["failed"],
        summary["error_rate"],
        summary["latency_ms_avg"],
        summary["latency_ms_p95"],
        json.dumps(run_data["tests"])
    ))
    conn.commit()
    conn.close()

def list_runs(limit=10):
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT timestamp, passed, failed, error_rate, avg_latency, p95_latency FROM runs ORDER BY id DESC LIMIT ?', (limit,))
    rows = cursor.fetchall()
    conn.close()
    
    runs = []
    for row in rows:
        runs.append({
            "timestamp": row[0],
            "passed": row[1],
            "failed": row[2],
            "error_rate": row[3],
            "avg_latency": row[4],
            "p95_latency": row[5]
        })
    return runs
