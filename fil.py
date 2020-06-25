from optparse import OptionParser
parse = OptionParser(usage='python fil.py -f port.txt')
parse.add_option('-f', '--file', dest='file',default="port.txt", type='string', help='Input masscan result file')
options, args = parse.parse_args()
file = options.file
f1 = open(file, 'r')
arr = []
nmap_ip = ''
nmap_allport = ''
for i in f1.readlines():
    try:
        a = i.strip('\n')[21:].strip(' ').split('/')
        port = a[0]
        waitclear = a[1][7:]
        nmap_ip = waitclear
        nmap_allport += port + ','
        ip = waitclear + ':' + port
        url = waitclear + ':' + port
        arr.append(url)
        nmap = "nmap -p " + port + " " + waitclear
    except:
        print("read file error")
        pass
f2 = open('domain.txt', 'a+')
for i in arr:
    f2.write(i + '\n')
f1.close()
f2.close()
print('nmap -p ' + nmap_allport[:-1] + ' ' + nmap_ip)
