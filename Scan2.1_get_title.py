#URL_IPandPort_scan.py
# from Tknight    versions:2.1    Email:369093335@qq.com
import os
import requests
import threading
import re
import sys
from bs4 import BeautifulSoup

#这里的线程模块就暂时不动了
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self,  name, D):
        threading.Thread.__init__(self)
        self.name = name
        self.D = D
    def run(self):                   
        Scan(self.name, self.D)


def Scan(threadName, D_ip):
    print("Start>"+str(threadName))
    
    if "http" not in D_ip:
        ip = "http://" + D_ip
    # 用户自定义端口号
    prot = setport()
    ua_kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

    scanip = ip
    try:
        r1 = requests.get(scanip, headers=ua_kv, timeout=2)
        if r1.status_code == 200:
            str1 = scanip + "=连接成功"
            
            #这里添加了新的模块用来保存标题title
            html=r1.text
            soup=BeautifulSoup(html,"lxml")
            find=str(soup.find("title"))
            title=find[7:-8]

            save(0,scanip,title)
            save(1,str1)
            print(str1)
        else:
            str2 = scanip + "=异常连接(访问状态非200)"
            save(1,str2)
            print(str2)
    except:
        #如果出现无法连接IP域名的情况则更换端口通过循环访问
        str3 = scanip + "=无法连接"
        print(str3)
        for y in prot:
            url = scanip + y
            #开始端口内爬虫扫描
            try:
                # timeout参数设置最长访问时间限制，以免造成爬虫假死, timeout=0.5
                r2 = requests.get(url, headers=ua_kv, timeout=1)
                if r2.status_code == 200:
                    str4 = url + "=连接成功"
                    save(0,url)
                    save(1,str4)
                    print(str4)
                else:
                    str5 = url + "=异常连接(访问状态非200)"
                    save(1,str5)
                    print(str5)

            except:
                str1 = url + "=无法连接"
                print(str1)
                continue
                
def save(num,content,tit="null"):
    if num==0:
        f1= open("Scan.html","a+")
        a = '<a href="'+content+'" target=_blank>'+content+'______'+tit+'</a><br>\n'
        f1.write(a+"\n")
    elif num==1:
        f2=open("./ScanUrl.txt", 'a+')
        f2.write(content+"\n")


def geturlIP(url):
    if "http://" in url:
        url = url[7:]
    elif "https://" in url:
        url= url[8:]
    x = os.popen("ping "+url).read()
    ip = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", x)
    return ip.group(0)


#分割IP
def splitIP(ip):
    str1 = ip.split(".")
    #这里通过ip A B C段位数只和得出我们接下来要分隔的内容,并且在最后方算上了三个[.]
    num = len(str1[0]) + len(str1[1]) + len(str1[2]) + 3
    return ip[:num]
    # 返回值即为分割后的字符串

def setStyle():
    html=open("Scan.html","a+")
    set_style='<title>Scan</title><style type="text/css">body{background: black;}a{color: lime;font-size:20px;}</style><body>\n'
    html.write(set_style)
    html.close()

def setport():
    port = [":80", ":81", ":82", ":8080", ":8081", ":3389", ":8887"]  # 请自定义端口并且 冒号开头 逗号隔开 例如 ':80',':81'
    return port


def main():
    os.system("color a")
    s=sys.argv[1]
    setStyle()

    #通过下方内容实现了所有需要爆破的IP都封装进了ip_arr中
    ip = geturlIP(s)
    ip_spl = splitIP(ip)
    ip_arr=[]
    for i in range(1,255):
        a=ip_spl+str(i)
        ip_arr.append(a)

    #循环添加线程开始爆破
    for i in ip_arr:
        thread = myThread( "Scan_D:IP"+str(i), i)
        thread.start()

main()


