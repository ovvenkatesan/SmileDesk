import requests
import json

try:
    print('--- Recent Calls ---')
    calls_res = requests.get('http://localhost:8000/api/dashboard/calls')
    if calls_res.status_code == 200:
        calls = calls_res.json()
        print(json.dumps([{'id': c['id'], 'time': c['start_time'], 'outcome': c['outcome']} for c in calls[:3]], indent=2))
    
    print('\n--- Recent Bookings ---')
    bookings_res = requests.get('http://localhost:8000/api/dashboard/bookings')
    if bookings_res.status_code == 200:
        bookings = bookings_res.json()
        print(json.dumps(bookings[:3], indent=2))
except Exception as e:
    print('Error:', e)
