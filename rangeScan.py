import requests
import sys
import threading
from queue import Queue
from bs4 import BeautifulSoup
from colorama import init, Fore
from optparse import OptionParser

# init console color and queue
init(autoreset=True)
q = Queue(-1)

# Check User input
parse = OptionParser(usage='python rangeScan.py -r domain.txt(default) -o ScanName -p 8000-10000,9000 -t 20')
parse.add_option('-r', '--readfile', dest='ReadFile', default="domain.txt", type='string', help='Scan Domain file name')
parse.add_option('-o', '--outfile', dest='OutFile', default="Scan", type='string', help='Result file name')
parse.add_option('-p', '--ports', dest='Ports', default="default", type='string', help='Scan ports')
parse.add_option('-t', '--threads', dest='Threads', default="200", type='string', help='Threads')
options, args = parse.parse_args()
ReadFileName = options.ReadFile
OutFileName = options.OutFile
ports = options.Ports
thr = eval(options.Threads)


def CheckHttp(url_list):
    new_data = []
    for i in url_list:
        if "http" not in i[:4]:
            target = "http://" + i
            new_data.append(target)
        else:
            new_data.append(i)
    return new_data


# return list, html data and web status
def GetHTML(url):
    request_header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko )Chrome/70.0.3538.77 Safari/537.36'}
    try:
        _request = requests.get(url, headers=request_header, timeout=3)
        if _request.status_code == 200:
            _request.encoding = "utf-8"
            html_data_status = [url, _request.text, 0]
            print(Fore.GREEN + "[+] " + Fore.RESET + "{}".format(url))
            return html_data_status
        else:
            html_data_status = [url, _request.status_code, 1]
            print(Fore.BLUE + "[+] " + Fore.RESET + "{} -ResponseCode {}".format(url, str(_request.status_code)))
            return html_data_status
    except:
        request_timeout = ["t!i!meout", "timeout", "timeout"]
        return request_timeout


# Get website title
def GetTitle(html):
    soup = BeautifulSoup(html, "lxml")
    find = str(soup.find("title"))
    title = find[7:-8]
    return title


def SaveData(rstatus, url, filename, tit="null"):
    if rstatus == 0:
        f1= open(filename+".html","a+")
        a = '<tr onmouseover="this.style.backgroundColor=\'#ff6600\';" onmouseout="this.style.backgroundColor=\'#d4e3e5\';"><td><a href="'+url+'" target=_blank style="font-weight:bold;">'+url+'</a></td><td>'+tit+'</td></tr>\n'
        f1.write(a+"\n")
        f1.close()
    elif rstatus == 1:
        f2=open(filename+"Error.html", 'a+')
        a = '<tr onmouseover="this.style.backgroundColor=\'#ff6600\';" onmouseout="this.style.backgroundColor=\'#d4e3e5\';"><td><a href="'+url+'" target=_blank style="font-weight:bold;">'+url+'</a></td><td>'+tit+'</td></tr>\n'
        f2.write(a+"\n")
        f2.close()


def setStyle(filename):
    name1 = filename + ".html"
    name2 = filename + "Error.html"
    html1 = open(name1, "a+")
    html2 = open(name2, "a+")
    set_style = '''
    <html>
        <head>
        <style type="text/css">
        table.hovertable {
        font-family: verdana,arial,sans-serif;
        font-size:11px;
        color:#333333;
        border-width: 1px;
        border-color: #999999;
        border-collapse: collapse;}
        table.hovertable th {
        background-color:#c3dde0;
        border-width: 1px;
        padding: 8px;
        border-style: solid;
        border-color: #a9c6c9;}
        table.hovertable tr {
        background-color:#d4e3e5;}
        table.hovertable td {
        border-width: 1px;
        padding: 8px;
        border-style: solid;
        border-color: #a9c6c9;}
        a {
        color: #000000;
        font-size: 13px;}
        a:visited {
        color: #8c8c8c;}
        a:hover {
        color: #944dff;}
        </style>
        </head>
    <body>
    <table class="hovertable">
    <tr>
        <th>Url</th><th>Title</th>
    </tr>
    <br>
        '''
    html1.write(set_style)
    html2.write(set_style)
    html1.close()
    html2.close()


def SetPorts(p):
    # 3-6,999,222
    if p != "default":
        try:
            user_set_ports = []
            temp_list1 = p.split(",")
            for s in temp_list1:
                if "-" not in s:
                    try:
                        eval(s)
                        user_set_ports.append(s)
                    except:
                        print(Fore.RED + "[-]" + Fore.RESET + "ports error!")
                        sys.exit()
                else:
                    temp_list2 = i.split("-")
                    for z in range(eval(temp_list2[0]), eval(temp_list2[1]) + 1):
                        user_set_ports.append(str(z))
            return user_set_ports
        except:
            print(Fore.RED + "[-]" + Fore.RESET + "ports error!")
            sys.exit()
    default_port = ["81", "82", "83", "8000", "8001", "8002", "8003", "8080", "8081", "8082", "8887", "8888", "8889",
                    "9002", "9001", "5000", "5001", "1234", "9000", "8090"]
    return default_port


def Scan(target_url):
    # [url, _request.status_code, 1]
    # [url, _request.text, 0]
    returnlist = GetHTML(target_url)
    fn = OutFileName
    if returnlist[2] == 0:
        title = GetTitle(returnlist[1])
        SaveData(0,target_url, fn, title)
    elif returnlist[2] == 1:
        request_status = str(returnlist[1])
        SaveData(1, target_url, fn, request_status)


def start_scan(que):
    while not que.empty():
        u = que.get()
        Scan(u)


if __name__ == "__main__":
    info = '''
TTTTTTT	 K   K  N    N   O   _gggg   H     H  ttttttt
   T     K  K   NN   N   _  g        H     H     t
   T     KKK    N N  N   I  g  gggg  HH H HH     t
   T     K  K   N  N N   I  g     g  H     H     t
   T     K   K  N   NN   I   _ggg    H     H     t
    '''
    print(Fore.MAGENTA + info)
    readfile_list = []
    try:
        url_file = open(ReadFileName, "r+")
        for i in url_file.readlines():
            readfile_list.append(i.strip("\n"))
        url_file.close()
    except:
        print(Fore.RED + "[-]" + Fore.RESET + "Readfile error!")
        sys.exit()
    ports_list = SetPorts(ports)
    target_list = []
    for x in readfile_list:
        for y in ports_list:
            target_list.append(x + ":" + y)
    target_list = CheckHttp(target_list)
    setStyle(OutFileName)
    # target_list
    threads = []
    for _ in target_list:
        q.put(_)
    print(Fore.GREEN + "[+] " + Fore.RESET + "Scan start")
    for thread_ in range(50):
        t = threading.Thread(target=start_scan, args=(q,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(Fore.GREEN + "[+] " + Fore.RESET + "Scan complete")

