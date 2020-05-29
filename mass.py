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
	except:
		pass

def gettitle(html):
	soup = BeautifulSoup(html,"lxml")
	find = str(soup.find("title"))
	title = find[7:-8]
	return title

def save(num,content,tit="null"):
    if num==0:
        f1= open("Scan.html","a+")
        a = '<tr onmouseover="this.style.backgroundColor=\'#ff6600\';" onmouseout="this.style.backgroundColor=\'#d4e3e5\';"><td><a href="'+content+'" target=_blank style="font-weight:bold;">'+content+'</a></td><td>'+tit+'</td></tr>\n'
        f1.write(a+"\n")
    elif num==1:
        f2=open("Error.html", 'a+')
        a = '<tr onmouseover="this.style.backgroundColor=\'#ff6600\';" onmouseout="this.style.backgroundColor=\'#d4e3e5\';"><td><a href="'+content+'" target=_blank style="font-weight:bold;">'+content+'</a></td><td>'+tit+'</td></tr>\n'
        f2.write(a+"\n")

def setStyle(filename):
	html=open(filename,"a+")
	set_style='''
    <html>
<head>
<style type="text/css">
table.hovertable {
    font-family: verdana,arial,sans-serif;
    font-size:11px;
    color:#333333;
    border-width: 1px;
    border-color: #999999;
    border-collapse: collapse;
}
table.hovertable th {
    background-color:#c3dde0;
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #a9c6c9;
}
table.hovertable tr {
    background-color:#d4e3e5;
}
table.hovertable td {
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #a9c6c9;
}
a {
    color: #000000;
    font-size: 13px;
    }
a:visited {
    color: #8c8c8c;
    }
a:hover {
    color: #944dff;
}
</style>
</head>
<body>
<table class="hovertable">
<tr>
    <th>Url</th><th>Title</th>
</tr>
	'''
	html.write(set_style)
	html.close()

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
