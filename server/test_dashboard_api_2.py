import requests
import json
try:
    res = requests.get('http://localhost:8000/api/dashboard/calls')
    if res.status_code == 200:
        calls = res.json()
        print('Number of calls:', len(calls))
        if calls:
            print('Latest Calls:')
            for c in calls[:3]:
                print(f"- {c['start_time']} | {c['caller_number']} | {c['outcome']}")
except Exception as e:
    print('Error:', e)
