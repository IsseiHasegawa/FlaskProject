from fastapi import FastAPI

app = FastAPI()

@app.get("/sample")
def read_root():
    return {"message": "サプーAPIです"}