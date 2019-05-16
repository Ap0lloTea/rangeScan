# Tknight from 369093335@qq.com
请使用2.3版本,copy或者下载后文件名可以随意更改方便使用

2.3版本更新,其中有2.2版本没有发布,2.2并不是一个特别完善的版本,因为其中线程与网站标题获取并没有得到很好的处理,在2.3版本中这些问题都得到了非常不错的改善
使用方法:请在脚本当前目录下存放all_domain.txt的文件中存放需要扫描的域名或者IP
cmd中运行 python xxx.py即可开始扫描

# 需要第三方运行库: lxml,bs4,requests,其他模块都为python3自带模块
# pip install lxml
# pip install bs4
# pip install requests

====
2.1版本更新:增加了在HTML扫描结果文件中添加网站标题功能,而且优化了界面 233333 lol  欢迎体验

====
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

此脚本是开源脚本,可以自行开发,可以有很不错的效果
