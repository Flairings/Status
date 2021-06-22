import json

from pypresence import Presence
from colorama import Fore, init
import time
import os

init()

with open("config.json", "r") as config:
    config = json.load(config)

    client_id = config.get("client.id")

    state = config.get("state")
    large_image = config.get("large_image")

    button_1_name = config.get("button.1_name")
    button_1_url = config.get("button.1_url")

    button_2_name = config.get("button.2_name")
    button_2_url = config.get("button.2_url")

def clear():
    os.system("cls")

def update():
    RPC.update(state=state, start=1, large_image=large_image, buttons=[{"label": f"{button_1_name}", "url": f"{button_1_url}"}, {"label": f"{button_2_name}", "url": f"{button_2_url}"}])


refresh_time = 15
version = 1.0
color = Fore.LIGHTCYAN_EX

def home():
    clear()
    print(f"""
    {color}Presence {Fore.LIGHTWHITE_EX}{version}
    Discord presence changer {Fore.LIGHTWHITE_EX}by {color}@Flairings""")

clear()
print(f"\n {Fore.YELLOW}  Connecting to Discord RPC Service")
time.sleep(1)
clear()

try:
    RPC = Presence(client_id)
    RPC.connect()
    RPC.clear(pid=os.getpid())
    print(f"\n {Fore.GREEN}  Successfully connected to Discord RPC Service \n {Fore.RESET}")
    time.sleep(1)
    home()
except Exception as e:
    clear()
    print(f"\n {Fore.LIGHTRED_EX}  Unable to connect to Discord RPC Service {Fore.WHITE}({e})")
    time.sleep(999)
    exit(0)

except BrokenPipeError as e:
    clear()
    print(f"\n {Fore.LIGHTRED_EX}  Unable to connect to Discord RPC Service {Fore.WHITE}({e})")
    time.sleep(999)
    exit(0)

print(f"\n     {Fore.GREEN}Status will be set in {refresh_time} seconds")

while True:
    time.sleep(refresh_time)
    update()
    home()
    print("")
    print(f"    {color}refresh time: {Fore.LIGHTWHITE_EX}{refresh_time}")
    print(f"    {color}state: {Fore.LIGHTWHITE_EX}{state}")
