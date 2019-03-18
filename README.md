# Tknight from 369093335@qq.com
all right all right,期待已久终于更新2.0多线程版本了,本次的脚本扫描完成后会生成一个html文件,文件中存放着网站可以以200状态码访问的连接,同时无法正常访问的例如 301  302  404 等等会以txt的形式保存下来
食用方法:
  运行环境 Python3.x   并且拥有requests库, 如果没有的话可以 pip install requests 进行下载
  在配置好Python系统path环境变量的情况下 使用 在cmd中输入 python xxx.py "你想扫描的URL"    (xxx.py,你可以将代码保存,然后根据个人喜好修改文件名)
  即可完成自动收集功能

近期会尽快编写2.x版本,预计增加获取网站标题的功能,方便快速识别资产

URL_IPandPort_scan_V1.0 为源生设计版
URL_IPandPort_scan_V1.1 为无需手动输入IP版
URL_IPandPort_scan_V1.2 为同时储存HTML文件方便渗透版---2019/3/8
URL_IPandPort_scan_V2.0为多线程扫描最大版本，嘿嘿，一个网站的d段预计一分钟内扫描完成，并且生成一个Scan.html供用户快速访问渗透D段资产,而且也会生成一个txt文本可以查看异常连接状态,301 302 404等等 
