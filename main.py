#__author__ = 'Johnny'
#coding=utf-8

import urllib
import re
import time

url = "http://guonei.news.baidu.com/n?cmd=4&class=civilnews&pn=1"

respone = urllib.urlopen(url)
html = respone.read()
htmltrans = html.decode('gbk').encode('utf-8')

r = re.compile(r'<a href=".*(?P<Date>.{10}).*" mon="ph" target="_blank">(?P<Title>.+)</a>')
news = r.findall(htmltrans)

for i in range(len(news)):
    date = news[i][0]
    title = news[i][1]
    print(date +" "+title)
