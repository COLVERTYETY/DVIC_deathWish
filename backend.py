import fastapi 
import uvicorn
import os
import time
import random
from settings import *

app = fastapi.FastAPI()

deathWishes = set()

@app.get("/count")
def count():
    return len(deathWishes)

@app.get("/wishes")
def wishes():
    #  pick a random person from the list of death wishes
    #  and return it
    return random.choice(list(deathWishes))

@app.put("/wishes")
def wishes(wish: str):
    print(wish)
    deathWishes.add(wish)
    return "OK"

if __name__ == "__main__":
    #  get the ip address of the machine from ifconfig
    uvicorn.run(app, host="0.0.0.0", port=BACKEND_PORT)

