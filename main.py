from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "now it is working fine"}
    
