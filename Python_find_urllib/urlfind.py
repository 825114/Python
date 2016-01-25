#-*- coding: UTF-8 -*-
#import modules
import urllib
#open file pr.txt
f = file('prg.txt','r')
# read file all
d = f.read()
#name and m4a file start,end flag
ns = '<span class=\"program-name\">'
ne = '</span>'
ms = '[&quot;'
me = '&quot;]'
#name and m4a file start , end position
fns = 0
fne = 0
fms = 0
fme = 0
#loop variable
i = 0
#some .....
head = r'http://od.qingting.fm'
tail = r'.mp3'
path = str("G:\\相声\\济公传\\").decode('utf-8')
#loop
while fne != -1:
    fns = d.find(ns,fne)
    fne = d.find(ne,fns)
    #file name
    fn = d[fns + len(ns):fne]
    fms = d.find(ms,fme)
    fme = d.find(me,fms)
    #file url
    fm = d[fms + len(ms):fme]
    #+++
    name = str(fn + tail).decode('utf-8')
    savePath = path + name
    url = head+fm
    #save file
    if fns != -1:
         print "G:\\相声\\济公传\\"+fn+tail,head+fm
        print "retrive start ..."
        data = urllib.urlretrieve(url,savePath)
        i = i + 1
        print "retrive success ..."
    else:
        print "End Of File"
else:
    #close  file prg.txt
    f.close()
    print 'file closed......'
    print ""