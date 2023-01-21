

# def write_ip_c(ip,index,end):
# 	f = open("domain.txt","a+")
# 	for i in range(index,end+1):
# 		temp = ip+str(i)
# def write_ip_b(ip,index,end):
# 	print("b")

# def write_ip_a(ip,index,end):
# 	print("a")


f = open("ip.txt","r+")
f1 = open("domain.txt","a+")
ip_list_src = []
for i in f.readlines():
	ip_list_src.append(i.strip("\n"))
f.close()
ip_tab_data_list = []
for j in ip_list_src:
	# ip_tab_data_list = [["1.2.3.4",'1.2.3.5'],[]]
	ip_tab_data_list.append(j.split("\t"))
#尽量一次性的处理干净数据然后add添加数据,先写个函数用作添加
# 这里定义重组列表的格式(二维),后续函数将围绕这个regroup_list来展开编写
# regroup_list = []
# 需要将A.B.C.D段四个段的IP范围根据判断条件压入其中,并且还需要将C.D两个段的内容"注意范围"的写入regroup中(考虑丢弃,感觉没必要重新循环一次,这样写的就太乱了,不如在当前循环直接用index end 两个列表来判断)
save_ip_list = []
for z in ip_tab_data_list:
	# ["1.2.3.4","1.2.3.5"]
	ip_index_data_list = z[0].split(".")		
	ip_end_data_list = z[1].split(".")		
	# if ip_index_data_list[0] == ip_end_data_list[0] && ip_index_data_list[1] == ip_end_data_list[1] &&  ip_index_data_list[2] == ip_end_data_list[2]:
	# 	static_ip = ip_index_data_list[0]+"."+ip_index_data_list[1]+"."+ip_index_data_list[2]+"."
	# 	write_ip(static_ip,int(ip_index_data_list[3]),int(ip_end_data_list[3]))
		# 此时产生新问题,如果数据是["1.1.3.8","1.4.3.3"] 那么该判断方法就失效了,还是需要重新判断后方的参数值,此时需要将判断内容提取为函数来编写脚本
		# 要寻找解决办法,可以使用 != 来快速编写前段的IP,但是后段会有问题..那么我们可以将列表重组,并且写成我们需要的函数,下方开始构造列表情况

	# 另外脚本还考虑到如果存在一整个A段的数据我们该如何去生成对应的IP,但是如果存在A段的话那就太大了,所以不推荐大范围的用A段来生成IP,否则后期还需要划片处理去遍历HTTP服务
	# [ 真实ip前缀.,ipA段index ,ipA段end ,ipB段index ,ipB段end ,ipC段index ,ipC段end ,ipD段index ,ipD段end ] 

	# 这个condition list可以省去,这些数据都是上方有的,又感觉没有必要写到这,直接用if判断就行
	Cdt_List = ["",ip_index_data_list[0],ip_end_data_list[0],ip_index_data_list[1],ip_end_data_list[1],
	ip_index_data_list[2],ip_end_data_list[2],ip_index_data_list[3],ip_end_data_list[3]]
	subscript = 1
	if ip_index_data_list[0] != ip_end_data_list[0]:
		subscript = int(ip_end_data_list[0])+1
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
		a_ip = ip_index_data_list[0]+"."+ip_index_data_list[1]+"."
		for c in range(int(ip_index_data_list[2]),int(ip_end_data_list[2])+1):
			for d in range(0,255):
				save_ip_list.append(a_ip+str(c)+"."+str(d))
	elif ip_index_data_list[3] != ip_end_data_list[3]:
		subscript = int(ip_end_data_list[3])+1
		a_ip = ip_index_data_list[0]+"."+ip_index_data_list[1]+"."+ip_index_data_list[2]+"."
		for d in range(int(ip_index_data_list[3]),int(ip_end_data_list[3])+1):
			save_ip_list.append(a_ip+str(d))


	# 差不多就这些,但是CD段是1,255还好,如果是 25,30 类似的短数据的话我们则需要根据C段生成的最后一位走D段的end 30,这样一想感觉很麻烦,但是的确没有更好的解决办法
	# 额外设置一个值,如果该设置值不等于当前循环的end值则后续的IP填充都按照0-255来填充,如果等于了最后一位则进入后续循环(可以考虑提取为函数,但是如果提取为函数又会受限一开始提出的额外设置一个值)
	# 接着调用save来保存即可或者定义一个全局的待保存的列表,程序最后保存该列表内容到文本中


for s in save_ip_list:
	f1.write(s+"\n")

f1.close()



