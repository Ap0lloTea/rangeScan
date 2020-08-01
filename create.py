
f1 = open("ip.txt","r+")
arry_  = []
for i in f1.readlines():
	if "." in i:
		i = i.strip("\n").split(".")
		tempdata = i[0]+"."+i[1]+"."+i[2]+"."
		arry_.append(tempdata)
	else:
		print("Open file Error!")


#a = 'xxx.xxx.xxx.'

f = open('domain.txt','a+')

for i in range(255):
	# if you want input ip address please delete # ip = a...... or input "#" to ip=j+str....
	# ip = a+str(i)
	for j in arry_:
		ip = j+str(i)+"\n"
		f.write(ip+'\n')
f.close()

