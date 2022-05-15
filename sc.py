import socket # for connecting
from colorama import init, Fore
from tqdm import tqdm
# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX



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


# get the host from the user
#host = input("Enter the host:")
# iterate over ports, from 1 to 1024
#for port in range(80, 443):

def main():
    if is_port_open(host, port):
        print('\r'+f"{GREEN}[+] {host}                        {RESET}                                  ")
    else:
        print(f"{GRAY}[!] {host}:    is closed    {RESET}", end="\r")


wordlist=input("path ==> ")
domain=input(" domain ==> ")
nwords=len(list(open(wordlist,"rb")))


print (nwords)
#port = 80

#with open(wordlist, "rb") as wordlist:


while nwords > 0:
    nwords=nwords-1
    try:

#        print ("done")
        with open(wordlist, "rb") as wordlist:
            for word in tqdm(wordlist):
                host=word.decode().strip()+"."+domain
                port = 80
                main()

    except:
        continue


print ("                                 ")



#port = 80
#main()
#port = 443
#main()
#port = 8443
#main()
#port=input("  from port : ")
#mport=input("  to port  :")
#while port <= mport :
#    port=nport+1
#    main()

