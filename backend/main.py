from fastapi import FastAPI

app = FastAPI(
    title="PDF to E-Course API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Backend is running 🚀"
    }