import requests
import json
try:
    print('Checking recent calls via API...')
    calls_res = requests.get('http://localhost:8000/api/dashboard/calls')
    if calls_res.status_code == 200:
        calls = calls_res.json()
        print('Total Calls:', len(calls))
        if len(calls) > 0:
            print('Latest Call:', calls[0]['start_time'])
except Exception as e:
    print('Error:', e)
