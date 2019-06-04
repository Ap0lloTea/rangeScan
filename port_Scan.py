# Port_scan.py 环境:Python3
# 这个是用来扫描单个网站的某个端口内容,例如开放了80端口,那么其他很多端口也有可能开放并且提供web服务,方便渗透
# from Tknight    Email:369093335@qq.com
# 需要第三方运行库: lxml,bs4,requests,其他模块都为python3自带模块
# pip install lxml
# pip install bs4
# pip install requests

import requests
import threading
import re
from bs4 import BeautifulSoup

class myThread (threading.Thread):
    def __init__(self, portdomain):
        threading.Thread.__init__(self)
        self.portdomain = portdomain
    def run(self):
        Scan(self.portdomain)

#扫描主入口
def Scan(portdomain):
    print("Start>"+portdomain)
    if "http" not in portdomain:
        ip = "http://" + portdomain
    # 获得用户自定义端口
    ua_kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    scanip = ip
    try:
        # 开始最基础的爬虫
        # 如果找不到服务器或者连接超时直接回报timeout错误
        r1 = requests.get(scanip, headers=ua_kv, timeout=8)
        #连接成功保存
        if r1.status_code == 200:
            msg1 = scanip + "=可以测试"
            r1.encoding = "utf-8"
            title=gettitle(r1.text)
            save(0,scanip,title)
            print(msg1)
        else:
            #这里指的是网站404或者403,301,302等状态会将其改为异常连接状态
            msg2 = scanip + "=异常连接="+str(r1.status_code)
            save(1,scanip,"网站状态:"+str(r1.status_code))
            print(msg2)
    except:
        #如果出现无法连接的情况则再扫描端口
        msg5 = scanip + "=无法连接"
        print(msg5)

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



# 设置样式
def setStyle(filename):
    html=open(filename,"a+")
    set_style='<title>'+filename+'</title><style type="text/css">body{background: black;}a{color: lime;font-size:20px;}</style><body>\n'
    html.write(set_style)
    html.close()

def main():
    # 设置样式
    # 正常访问的网站会给出Scan.html
    # 状态非200访问的网站会给出Error.html
    setStyle("Scan.html")
    setStyle("Error.html")
    #打开范围文件直接扫描


    # url = input("Please input URL: ")
    url = input("input URL:")
    port = [ "80","81","82","83","84","85","86","87","88","89",
    "7001","7002","7003","7004","10443","993","2276",
    "8000", "8001","8002", "8003","8004","8005","8006","8007","8008","8009",
    "8080", "8081","8082","8083","8084","8085","8086","8087","8088","8089",
    "8090", "8091","8092","8093","8094","8095","8096","8097","8098","8099",
    "8887", "8888","8889","10004","10005","5000","6080"
    ]
    ip_arr = []
    for i in port:
    	ip_arr.append(url+":"+i)

    for i in ip_arr:
        thread = myThread(i)
        thread.start()

main()