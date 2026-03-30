import os

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\api.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Regex to replace the whole get_roi_snapshot function
pattern = r'@app\.get\("/api/dashboard/roi"\)\s*def get_roi_snapshot\(\):.*?return \{.*?\}'
new_func = '''@app.get("/api/dashboard/roi")
def get_roi_snapshot():
    if not supabase:
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail="Supabase not configured")
    try:
        response = supabase.table("calls").select("*").execute()
        calls = response.data
        total_calls = len(calls)
        leads_saved = sum(1 for call in calls if call.get("outcome") == "booked_appointment")
        conversion_rate = round((leads_saved / total_calls * 100) if total_calls > 0 else 0, 1)
        
        return {
            "leads_saved": leads_saved,
            "estimated_value": leads_saved * 200,
            "period": "All Time",
            "total_calls": total_calls,
            "conversion_rate": conversion_rate
        }
    except Exception as e:
        print(f"Error fetching ROI data: {e}")
        return {
            "leads_saved": 0, "estimated_value": 0, "period": "All Time", "total_calls": 0, "conversion_rate": 0
        }'''

content = re.sub(pattern, new_func, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Patched api.py')
