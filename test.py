
from parse import getH
import cPickle
import sys

i = 52361

hls=[]


while i < 55630:
    try:
        filename = "hlass/%s.html" % i
        h = getH(filename)
        h.k=i
        print i
        print h
        hls.append(h.hlasy)
    except KeyboardInterrupt:
        break
    except:
        print sys.exc_info()
    i=i+1

print hls
#sys.exit()

cPickle.dump(hls, open("hlass.dump","w"))

