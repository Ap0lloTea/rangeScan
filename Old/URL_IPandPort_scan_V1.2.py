#URL_IPandPort_scan.py
# from Tknight    versions:1.1    Email:369093335@qq.com
import os
import requests
import re
import sys

def geturlIP(url):
    if "http://" in url:
        url = url[7:]
    elif "https://" in url:
        url= url[8:]
    x = os.popen("ping "+url).read()
    ip = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", x)
    return ip.group(0)

def splitIP(ip):
    str1 = ip.split(".")
    num = len(str1[0]) + len(str1[1]) + len(str1[2]) + 3
    return ip[:num]

def callip(url):
    ip = geturlIP(url)
    ip = splitIP(ip)

    if "http" not in ip:
        ip = "http://" + ip

    prot = setport()

    ua_kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

    arr=[]

    file = open("./ScanUrl.txt", 'w+')

    for i in range(255):
        ip_tail = str(i)
        scanip = ip + ip_tail
        try:
            iin = requests.get(scanip, headers=ua_kv, timeout=1)
            if iin.status_code == 200:
                str1 = scanip + "=连接成功"
                arr.append(scanip)
                file.write(str1+"\n")
                print(str1)
            else:
                str1 = scanip + "=异常连接(访问状态非200)"
                file.write(str1 + "\n")
                print(str1)
        except:
            str1 = scanip + "=无法连接"
            print(str1)
            for y in prot:
                url = scanip + y
                try:
                    r = requests.get(url, headers=ua_kv, timeout=1)
                except:
                    str1 = url + "=无法连接"
                    print(str1)
                    continue
                if r.status_code == 200:
                    str1 = url + "=连接成功"
                    arr.append(url)
                    file.write(str1 + "\n")
                    print(str1)
                else:
                    str1 = url + "=异常连接(访问状态非200)"
                    file.write(str1 + "\n")
                    print(str1)
    file.close()
    return arr

def savehtml(arr):
    html=open("Scan.html","a")
    set_style='<title>Scan</title><style type="text/css">body{background: black;}a{color: greenyellow;font-size:20px;}</style><body>\n'
    html.write(set_style)
    for i in arr:
        a='<a href="'+i+'" target=_blank>'+i+'</a><br>\n'
        html.write(a)
    html.close()


def setport():
    port = [":80", ":81", ":82", ":8080", ":8081", ":3389", ":8887"]  # 请自定义端口并且 冒号开头 逗号隔开 例如 ':80',':81'
    return port
def main():
    s=sys.argv[1]
    arr = callip(s)
    savehtml(arr)

main()
