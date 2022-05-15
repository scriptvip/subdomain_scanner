import requests
from bs4 import BeautifulSoup
import time
import socket # for connecting
from colorama import init, Fore
from tqdm import tqdm
import os
# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX



#for _ in tqdm(range(2), leave=False):
#     time.sleep(1)


domain = input("    Domain ==> ")
url = "https://api.hackertarget.com/hostsearch/?q="+domain
subdomain = []
req = requests.get(url)
if req.status_code == 200:
    soup = BeautifulSoup(req.text, "html.parser")
    css = "body table ~ table td.outer table tr:not(:nth-child(1)) td:nth-child(5)"
    data = soup.select(css)
    for dt in data:
        sub = dt.get_text().replace("*.","")
        if sub not in subdomain:
            subdomain.append(sub)
#print (sub)

    with open("domain.txt", "w") as f:
        for sub in subdomain:
            try:
                f.write(sub + "\n")
#                print(sub)
            except:
                pass

######:&*_*%&*_*^*&^%^*&*&^^&^*_*_*^^€^?€*^^€

def is_port_open(host, port):
    """
    determine whether `host` has the `port` open 
    """
    # creates a new socket
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.settimeout(.2)
        s.connect((host, port))
        # make timeout if you want it a little faster ( less accuracy )
#        s.settimeout(0.2)
    except:
        # cannot connect, port is closed return false
        return False
    else:
        # the connection was established, port is open!
        return True


def main():
    if is_port_open(host, port):
#        print(f"{GREEN}[+] {host}:{port} is open {RESET}")
        print(" ")
    else:
        print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")


wordlist = "domain.txt"

nwords=len(list(open(wordlist,"rb")))

os.system("rm -rf host.txt")

while nwords > 0:
    nwords=nwords-1
    try:
#        print ("done")
        with open(wordlist, "rb") as wordlist:
            for word in tqdm(wordlist, leave=False):
                host=word.decode().strip()
                print (" ====================")
                port = 80
                main()
                if is_port_open(host, port) == True:
                    print (is_port_open(host, port))
                    port = 443
                    main()
                    if is_port_open(host, port) == True:
                        port = 8443
                        main()
                        if is_port_open(host, port) == True:
#                            num = 1
                            print(f"{GREEN}[+] {host}:80,443,8443 is open {RESET}")
                            h=open("host.txt", 'a', newline=None)
                            h.write(" [+] " + host + ": 80, 443, 8443" + "\r" + "\r")
#                            h.close()
                print (" ====================")
#                print ("   ===== "+s)
    except:
        continue
#h=open("host.txt", "r")
#print (h.read())
