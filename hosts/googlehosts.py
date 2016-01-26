# encoding: utf-8
import urllib
import os
url = "http://www.360kb.com/kb/1_122.html"
urlConnect = urllib.urlopen(url)
htmlContent = urlConnect.read()
flagStart = "==更新分界线，复制下面内容到hosts文件即可====="
flagEnd = "</pre>"
flagStartPosistion = htmlContent.find(flagStart)
flagEndPosistion = htmlContent.find(flagEnd,flagStartPosistion)
hostsContent = htmlContent[flagStartPosistion + len(flagStart):flagEndPosistion]
hostsPath = "C:\Windows\System32\drivers\etc\hosts"
hosts = file(hostsPath,"w")
hosts.write(hostsContent)