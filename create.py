a = 'xxx.xxx.xxx.'

f = open('domain.txt','a+')
for i in range(255):
	ip = a+str(i)
	f.write(ip+'\n')
f.close()
