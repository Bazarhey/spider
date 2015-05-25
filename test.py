#conding=utf-8
import urllib
import re
import time

class Spider:
    def __int__(self):

    def getUrl(self):
        readUrl = open('url.txt')
        lines = readUrl.readlines()
        try:
            if len(lines) != 0:
                    return lines
            else:
                print"Configure your url.txt!"
                exit()
        finally:
            readUrl.close()

    def getHtml(self):
        URl = self.getUrl()
        for i in URl:
            response = urllib.urlopen(i)
            html = response.read()
            htmlcode = html.decode('gb2312').encode('utf-8')
        return (htmlcode)

    r = re.compile(r'<a target="_blank" class="linkto" href="/a/(?P<Date>.{8}).*">(?P<Title>.+)</a>')
    for code in getHtml():
        news = r.findall(code)
    out = file("test.txt", 'a+')

    for i in range(len(news)):
        date = news[i][0]
        title = news[i][1]
        out.writelines(title +" "+ date+"\n")
    out.close()