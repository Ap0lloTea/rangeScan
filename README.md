# Tknight 369093335@qq.com
介绍:此脚本为刚接触安全时由于一些站点需要手动复制粘贴打开导致渗透途中浪费了很多时间,所以便有了此创意进行该脚本的开发;
拿旧版本与新版本相比较也是很利于Python初学者对爬虫概念与线程概念一步一步学习的非常好的途径
# 需要第三方运行库: lxml,bs4,requests,colorama 其他模块都为python3自带模块
# need lxml,bs4,requests,colorama
# pip install lxml
# pip install bs4
# pip install requests
# pip install colorama
====
19.09.08更新:
  过了很久的时间再次更新脚本,重新审视了整个代码运行的流程,添加了默认200线程的限制来进行扫描(PS:之前写的脚本只用于对C段进行信息收集没有线程限制),而此次做了线程限制可以进行B段收集并且大幅减少CPU与内存耗费.
  使用方法:
    首先运行Range_Create.py来根据脚本内容自行添加IP,或者自己想办法生成IP段存储为domain.txt,将domain.txt与Range_Scan.py存储到同一目录下即可运行Range_Scan.py,扫描完成后会生成Scan.html与Error.html,并且将扫描内容进行了保存,其中访问状态非200的存储为Error.
  后期会对各样的用户需求进行不定期更新,同时在我使用的途中也会对使用不如意的地方进行修改更新,尽情期待.


后期该脚本会向漏洞自动化挖掘方向进行慢慢开发,喜欢的表哥可以点个Star   LOL
声明:此脚本是开源脚本,自行开发,可以有很不错的效果XD
