# Tknight 369093335@qq.com
此脚本由在渗透测试过程中为了方便快速探测目标站点和快速打开而出现
需要第三方运行库: lxml,bs4,requests,colorama 其他模块都为python3自带模块

pip install lxml

pip install bs4

pip install requests

pip install colorama

Create domain.txt

将目标资产放入domain.txt中

python3 rangeScan.py

运行后即可获得html文件


2020.05.19更新
更新了rangeScan.py输出报告的样式,之前只是生成a标签html文件,现在为了页面的美观更新为输出列表,后续将添加更多内容


19.10.03更新
上传了fil.py文件,该文件可以读取masscan扫描的结果自动生成配合RangeScan.py的扫描范围,并且可以配合Nmap进行目标系统端口探测


19.09.08更新:
  过了很久的时间再次更新脚本,重新审视了整个代码运行的流程,添加了默认200线程的限制来进行扫描(PS:之前写的脚本只用于对C段进行信息收集没有线程限制),而此次做了线程限制可以进行B段收集并且大幅减少CPU与内存耗费.
  使用方法:
    首先运行Range_Create.py来根据脚本内容自行添加IP,或者自己想办法生成IP段存储为domain.txt,将domain.txt与Range_Scan.py存储到同一目录下即可运行Range_Scan.py,扫描完成后会生成Scan.html与Error.html,并且将扫描内容进行了保存,其中访问状态非200的存储为Error.
  后期会对各样的用户需求进行不定期更新,同时在我使用的途中也会对使用不如意的地方进行修改更新,尽情期待.



后期该脚本会向漏洞自动化挖掘方向进行慢慢开发,喜欢的表哥可以点个Star   LOL
声明:此脚本是开源脚本,自行开发,可以有很不错的效果XD
