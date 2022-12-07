import os 

BACKEND_IP = '172.21.72.156'
try:
    possible_ips = os.popen("ifconfig | grep 'inet '").read().split("inet ")[1:]
    for ip in possible_ips:
        ip = ip.split(" ")[0]
        if ip.startswith("172."):
            BACKEND_IP = ip
            continue
except:
    print("could not get ip address")
    
BACKEND_PORT = '8000'