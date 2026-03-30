import requests
import json
try:
    res = requests.get('http://localhost:8000/api/dashboard/calls')
    if res.status_code == 200:
        calls = res.json()
        print('Number of calls:', len(calls))
        if calls:
            print('First call:', calls[0]['start_time'])
            print('Last call:', calls[-1]['start_time'])
except Exception as e:
    print('Error:', e)
