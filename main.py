import importlib

FastAPI = importlib.import_module("fastapi").FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/info")
def get_info():
    return {"app_name": "Release Manager Project", "status": "active"}

@app.get("/")
def read_root():
    return {"message": "Hello World", "version": "1.0.0"}