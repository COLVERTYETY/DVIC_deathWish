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

    possible_ips = os.popen("ifconfig | grep 'inet '").read().split("inet ")[1:]
    for ip in possible_ips:
        ip = ip.split(" ")[0]
        if ip.startswith("172."):
            continue
        print("using ip", ip)
        break
    
    print("running on", ip, BACKEND_PORT)
    uvicorn.run(app, host="0.0.0.0", port=BACKEND_PORT)

