import os
import uuid
from fastapi import FastAPI

app = FastAPI()

@app.get("/hostname")
async def get_hostname():
    return {"hostname": os.uname().nodename}

@app.get("/author")
async def get_author():
    return {"author": os.environ.get("AUTHOR", "Unknown")}

@app.get("/id")
async def get_uuid():
    return {"uuid": os.environ.get("UUID", str(uuid.uuid4()))}