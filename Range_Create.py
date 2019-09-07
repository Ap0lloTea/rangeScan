
f = open('domain.txt','a+')
a = 'xxx.xxx.xxx.'
for i in range(255):
	ip = a+str(i)
	f.write(ip+'\n')
f.close()
