
from optparse import OptionParser

parse = OptionParser(usage='python3 cc2.py -r ip.txt(default) -o domain.txt(default)')
parse.add_option('-r', '--readfile', dest='ReadFile', default="ip.txt", type='string', help='Scan Domain file name')
parse.add_option('-o', '--outfile', dest='OutFile', default="domain.txt", type='string', help='Result file name')
options, args = parse.parse_args()
ReadFileName = options.ReadFile
OutFileName = options.OutFile

f = open(ReadFileName,"r+")
f1 = open(OutFileName,"a+")
ip_list_src = []
try:
	for i in f.readlines():
		ip_list_src.append(i.strip("\n"))
except:
	print("ReadFileError")
f.close()
ip_tab_data_list = []
for j in ip_list_src:
	if "-" in j:
		ip_tab_data_list.append(j.split("-"))
	elif "\t" in j:
		ip_tab_data_list.append(j.split("\t"))
save_ip_list = []
for z in ip_tab_data_list:
	ip_index_data_list = z[0].split(".")
	ip_end_data_list = z[1].split(".")
	subscript = 1
	if ip_index_data_list[0] != ip_end_data_list[0]:
		subscript = int(ip_end_data_list[0])+1
		# 此处逻辑待更改
		for a in range(int(ip_index_data_list[0]),int(ip_end_data_list[0])+1):
			if subscript == int(ip_end_data_list[0]):
				break
			for b in range(0,255):
				for c in range(0,255):
					for d in range(0,255):
						save_ip_list.append(str(a)+"."+str(b)+"."+str(c)+"."+str(d))
	elif ip_index_data_list[1] != ip_end_data_list[1]:
		subscript = int(ip_end_data_list[1])+1
		a_ip = ip_index_data_list[0]+"."
		for b in range(int(ip_index_data_list[1]),int(ip_end_data_list[1])+1):
			for c in range(0,255):
				for d in range(0,255):
					save_ip_list.append(a_ip+str(b)+"."+strip(c)+"."+strip(d))
	elif ip_index_data_list[2] != ip_end_data_list[2]:
		subscript = int(ip_end_data_list[2])+1
		print("subscript :"+str(subscript))
		a_ip = ip_index_data_list[0]+"."+ip_index_data_list[1]+"."
		for c in range(int(ip_index_data_list[2]),int(ip_end_data_list[2])+1):
			for d in range(0,255):
				save_ip_list.append(a_ip+str(c)+"."+str(d))
	elif ip_index_data_list[3] != ip_end_data_list[3]:
		subscript = int(ip_end_data_list[3])+1
		a_ip = ip_index_data_list[0]+"."+ip_index_data_list[1]+"."+ip_index_data_list[2]+"."
		for d in range(int(ip_index_data_list[3]),int(ip_end_data_list[3])+1):
			save_ip_list.append(a_ip+str(d))
for s in save_ip_list:
	f1.write(s+"\n")
f1.close()
