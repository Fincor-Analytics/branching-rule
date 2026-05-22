from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "now master is connecte to dev now"}
    
