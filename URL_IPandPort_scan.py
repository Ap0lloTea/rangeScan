#URL_IPandPort_scan.py
# from Tknight    versions:1.0    Email:369093335@qq.com
import os
import requests
def geturlIP(url):
    if "http://" in url:
        url = url[7:]
    elif "https://" in url:
        url= url[8:]
    os.system("ping " + url)
def callip():
    ip = input("请输入上方扫描出的IP:")
    ip = splitIP(ip)
    if "http" not in ip:
        ip = "http://" + ip
    prot = setport()
    ua_kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    file = open("./ScanUrl.txt", 'w+')

    for i in range(255):
        if i == 0:
            continue
        ip_tail = str(i)
        scanip = ip + ip_tail
        try:
            iin = requests.get(scanip, headers=ua_kv, timeout=0.5)
            if iin.status_code == 200:
                str1 = scanip + "=连接成功"
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
                    r = requests.get(url, headers=ua_kv, timeout=0.5)
                except:
                    str1 = url + "=无法连接"
                    print(str1)
                    continue
                if r.status_code == 200:
                    str1 = url + "=连接成功"
                    file.write(str1 + "\n")
                    print(str1)
                else:
                    str1 = url + "=异常连接(访问状态非200)"
                    file.write(str1 + "\n")
                    print(str1)
    file.close()

def splitIP(ip):
    str1 = ip.split(".")
    num = len(str1[0]) + len(str1[1]) + len(str1[2]) + 3
    return ip[:num]

def setport():
    # 请在此自定义端口并且 冒号开头 逗号隔开 例如 ':80',':81'
    port = [":80", ":81", ":82", ":8080", ":8081", ":3389", ":8887"]
    return port
def main():
    #请在此自定义url 不用管http还是HTTPS协议头，会自动过滤
    geturlIP("hzynwb.9966.org")
    callip()

if __name__ == '__main__':
    main()
