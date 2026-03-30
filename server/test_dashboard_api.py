import requests
import json

try:
    response = requests.get('http://localhost:8000/api/dashboard/calls')
    calls = response.json()
    if calls:
        print('First call ID:', calls[0]['id'])
        call_details = requests.get(f'http://localhost:8000/api/dashboard/calls/{calls[0]["id"]}').json()
        print('Call Details Keys:', call_details.keys())
        print('Call Details Preview:', json.dumps(call_details, indent=2)[:300])
    else:
        print('No calls returned.')
except Exception as e:
    print('Error:', e)
