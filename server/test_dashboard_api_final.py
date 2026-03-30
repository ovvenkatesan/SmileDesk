import requests
import json
try:
    res = requests.get('http://localhost:8000/api/dashboard/roi')
    print('ROI API Status:', res.status_code)
    print('ROI Data:', res.json())
    
    calls_res = requests.get('http://localhost:8000/api/dashboard/calls')
    if calls_res.status_code == 200:
        calls = calls_res.json()
        if calls:
            print('\nLatest Call in API:', calls[0]['start_time'], 'ID:', calls[0]['id'])
        else:
            print('\nNo calls in API response.')
except Exception as e:
    print('Error:', e)
