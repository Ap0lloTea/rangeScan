# URL_IPandPort_scan.py 环境:Python3
# from Tknight    versions:2.2    Email:369093335@qq.com
# 需要第三方运行库: lxml,bs4,requests,其他模块都为python3自带模块
# pip install lxml
# pip install bs4
# pip install requests

import os
import requests
import threading
import re
from bs4 import BeautifulSoup

#线程基础
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self,  name, D):
        threading.Thread.__init__(self)
        self.name = name
        self.D = D
    def run(self):
        Scan(self.name, self.D)

#扫描主入口
def Scan(threadName, C_ip):
    print("Start>"+str(threadName))
    if "http" not in C_ip:
        ip = "http://" + C_ip
    # 获得用户自定义端口
    prot = setport()
    ua_kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    scanip = ip
    try:
        # 开始最基础的爬虫
        # 如果找不到服务器或者连接超时直接回报timeout错误
        r1 = requests.get(scanip, headers=ua_kv, timeout=3)
        #连接成功保存
        if r1.status_code == 200:
            msg1 = scanip + "=连接成功"
            r1.encoding = "utf-8"
            title=gettitle(r1.text)
            save(0,scanip,title)
            print(msg1)
        else:
            #这里指的是网站404或者403,301,302等状态会将其改为异常连接状态
            msg2 = scanip + "=异常连接="+str(r1.status_code)
            save(1,scanip,"网站状态:"+str(r1.status_code))
            print(msg2)
        # 在判断完成后下方开启第二次爬虫扫描(端口)
        for y in prot:
            url = scanip+":"+ y
            try:
                r2 = requests.get(url, headers=ua_kv, timeout=3)
                if r2.status_code == 200:
                    msg3 = url + "=连接成功"
                    r2.encoding = "utf-8"
                    title=gettitle(r2.text)
                    save(0,url,title)
                    print(msg3)
                else:
                    msg4 = url + "=异常连接="+str(r2.status_code)
                    save(1,url,"网站状态:"+str(r2.status_code))
                    print(msg4)
            except:
                ScanPortmsg = url + "=无法连接"
                print(ScanPortmsg)
                continue

    except:
        #如果出现无法连接的情况则再扫描端口
        msg5 = scanip + "=无法连接"
        print(msg5)
        for y in prot:
            url = scanip+":"+ y
            #开始端口内爬虫扫描
            try:
                r3 = requests.get(url, headers=ua_kv, timeout=3)
                if r3.status_code == 200:
                    msg6 = url + "=连接成功"
                    r3.encoding = "utf-8"
                    title=gettitle(r3.text)
                    save(0,url,title)
                    print(msg6)
                else:
                    msg7 = url + "=异常连接="+str(r3.status_code)
                    save(1,url,"网站状态:"+str(r3.status_code))
                    print(msg7)

            except:
                msg8 = url + "=无法连接"
                print(msg8)
                continue

def gettitle(html):
    soup = BeautifulSoup(html,"lxml")
    find = str(soup.find("title"))
    title = find[7:-8]
    return title

# 保存扫描内容
def save(num,content,tit="null"):
    if num==0:
        f1= open("Scan.html","a+")
        a = '<a href="'+content+'" target=_blank>'+content+'______'+tit+'</a><br>\n'
        f1.write(a+"\n")
    elif num==1:
        f2=open("Error.html", 'a+')
        a = '<a href="'+content+'" target=_blank>'+content+'______'+tit+'</a><br>\n'
        f2.write(a+"\n")

#获得与分割IP
def geturlIP(url):
    if "http://" in url:
        url = url[7:]
    elif "https://" in url:
        url= url[8:]
    x = os.popen("ping "+url).read()
    ip = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", x)
    ip = ip.group(0)
    s1 = ip.split(".")
    num = len(s1[0]) + len(s1[1]) + len(s1[2]) + 3
    return ip[:num]


# 设置样式
def setStyle(filename):
    html=open(filename,"a+")
    set_style='<title>Scan</title><style type="text/css">body{background: black;}a{color: lime;font-size:20px;}</style><body>\n'
    html.write(set_style)
    html.close()

# 用户自定义端口
def setport():
    # 自定义端口如下,已经有部分自定义端口,请根据个人情况添加(PS:最好不要设置过多的端口,否则可能会被有waf的网站暂时封禁IP)
    port = [ "81", "82","83","8000", "8001","8002", "8003","8080", "8081","8082","8887", "8888","8889","5000" ]
    return port

def main():
    # 设置样式
    # 正常访问的网站会给出Scan.html
    # 状态非200访问的网站会给出Error.html
    setStyle("Scan.html")
    setStyle("Error.html")
    #打开范围文件直接扫描
    url = input("Please input URL: ")
    ip = geturlIP(url)
    ip_arr=[]
    for i in range(1,255):
    	ip_arr.append(ip+str(i))

    #循环添加线程开扫
    #此时全力爆破,会导致CPU消耗过高,后边版本将会寻找解决办法
    for i in ip_arr:
        thread = myThread( "Scan_C:IP"+str(i), str(i))
        thread.start()

main()
