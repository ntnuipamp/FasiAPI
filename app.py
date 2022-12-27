from fastapi import FastAPI
import uvicorn


app = FastAPI(host='0.0.0.0', port=8080)
@app.get("/")
def read_root():
    return {"Hello": "World"}



