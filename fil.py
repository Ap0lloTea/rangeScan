f1 = open('port.txt','r')
arr = []
nmap_ip = ''
nmap_allport = ''
n = []
for i in f1.readlines():
	a = i.strip('\n')[21:].strip(' ').split('/')
	port = a[0]
	waitclear = a[1][7:]
	# print(waitclear)
	nmap_ip= waitclear
	nmap_allport+=port+','
	ip = waitclear+':'+port
	url = waitclear+':'+port
	arr.append(url)
	# print(url)
	nmap = "nmap -p "+port+" "+waitclear
	n.append(nmap)
f2 = open('domain.txt','a+')
for i in arr:
	f2.write(i+'\n')
f1.close()
f2.close()


# for i in n:
	# print(i)
print('nmap -p '+nmap_allport[:-1]+' '+nmap_ip)