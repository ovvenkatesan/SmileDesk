from fastapi import FastAPI

app = FastAPI(title="Smile Garden Voice AI API")

@app.get("/")
def read_root():
    return {"message": "Smile Garden Voice AI API is running"}
