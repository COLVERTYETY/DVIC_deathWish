import fastapi 
import uvicorn
import os
import time
from settings import *

app = fastapi.FastAPI()

deathWishes = []

@app.get("/count")
def count():
    return len(deathWishes)

@app.get("/wishes")
def wishes():
    buffer  = "{"
    for i,wish,time in enumerate(deathWishes):
        buffer += f'"{i}": ("{wish}", "{time}"),'
    buffer += "}"
    return buffer

@app.post("/wishes")
def wishes(wish: str):
    deathWishes.append((wish, time.time()))
    return "OK"

if __name__ == "__main__":
    #  get the ip address of the machine from ifconfig
    uvicorn.run(app, host="0.0.0.0", port=BACKEND_PORT)

