import os
import requests
import threading
import re
import sys
from queue import Queue
from bs4 import BeautifulSoup
from colorama import init,Fore

# console color
init(autoreset=True)

# queue
q = Queue(-1)

#Scan_main
def Scan(C_ip):
    if "http" not in C_ip:
        ip = "http://" + C_ip
    else:
        ip = C_ip

    prot = setport()
    ua_kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko )Chrome/70.0.3538.77 Safari/537.36'}
    scanip = ip
    try:
        r1 = requests.get(scanip, headers=ua_kv, timeout=3)
        if r1.status_code == 200:
            r1.encoding = "utf-8"
            title=gettitle(r1.text)
            save(0,scanip,title)
            print(Fore.GREEN + "{}-Live".format(scanip))
        else:
            save(1,scanip,"Status:"+str(r1.status_code))
            print(Fore.BLUE + "{}-Error-{}".format(scanip,str(r1.status_code)))
        for y in prot:
            url = scanip+":"+ y
            try:
                r2 = requests.get(url, headers=ua_kv, timeout=3)
                if r2.status_code == 200:
                    r2.encoding = "utf-8"
                    title=gettitle(r2.text)
                    save(0,url,title)
                    print(Fore.GREEN + "{}-ON".format(url))
                else:
                    save(1,url,"Status:"+str(r2.status_code))
                    print(Fore.BLUE + "{}-Error-{}".format(url,str(r2.status_code)))
            except:
                continue
    except:
        for y in prot:
            url = scanip+":"+ y
            try:
                r3 = requests.get(url, headers=ua_kv, timeout=3)
                if r3.status_code == 200:
                    r3.encoding = "utf-8"
                    title=gettitle(r3.text)
                    save(0,url,title)
                    print(Fore.GREEN + "{}-ON".format(url))
                else:
                    save(1,url,"Status:"+str(r3.status_code))
                    print(Fore.BLUE + "{}-Error-{}".format(url,str(r3.status_code)))

            except:
                continue

def gettitle(html):
    soup = BeautifulSoup(html,"lxml")
    find = str(soup.find("title"))
    title = find[7:-8]
    return title

def save(num,content,tit="null"):
    if num==0:
        f1= open("Scan.html","a+")
        a = '<a href="'+content+'" target=_blank>'+content+'---'+tit+'</a><br>\n'
        f1.write(a+"\n")
    elif num==1:
        f2=open("Error.html", 'a+')
        a = '<a href="'+content+'" target=_blank>'+content+'---'+tit+'</a><br>\n'
        f2.write(a+"\n")

def setStyle(filename):
    html=open(filename,"a+")
    set_style='''
    <!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>Range_Scan</title>
		<style type="text/css">
			body {
				background-color: #262626;
			}

			a {
				color: #ff4d4d;
				font-size: 23px;
			}

			a:visited {
				color: #ffffff;
			}

			a:hover {
				color: #884dff;
			}
		</style>
	</head>
	<body>
    '''
    html.write(set_style)
    html.close()

def setport():
    port = [ "81", "82","83","8000", "8001","8002", "8003","8080", "8081","8082","8887", "8888","8889","9002","9001","5000" ]
    return port

def gooo(q):
	while not q.empty():
		u = q.get()
		Scan(u)

def main():
	info = '''
	   ______
	  /______/@  @  @@   @  @@  @@@@  @       @
	    / /   @ @   @ @  @  __ @   @  @     @@@@@
	   / /    @ @   @  @ @  --  @@@@  @@@@    @
	  /_/     @  @  @  @ @  @@     @  @   @   @   @
	                            @@@@  @   @   @@@@ 
	'''
	print(info)
	print("Start_Connect")
	setStyle("Scan.html")
	setStyle("Error.html")

	f = open("domain.txt","r")
	for i in f.readlines():
		url = i.strip('\n')
		q.put(url)

	threads = []
	for thread_ in range(200):
		t = threading.Thread(target=gooo, args=(q,))
		t.start()
		threads.append(t)

	for t in threads:
		t.join()

	print("Success!")

main()
