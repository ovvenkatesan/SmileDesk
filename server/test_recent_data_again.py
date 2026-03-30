import requests
import json
try:
    print('Checking recent bookings via API...')
    bookings_res = requests.get('http://localhost:8000/api/dashboard/bookings')
    if bookings_res.status_code == 200:
        bookings = bookings_res.json()
        print('Bookings Count:', len(bookings))
        print(json.dumps(bookings[:2], indent=2))
except Exception as e:
    print('Error:', e)
