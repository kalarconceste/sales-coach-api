from fastapi import FastAPI

app = FastAPI(title="Sales Coach API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sales Coach API. Use /coach to get feedback."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
