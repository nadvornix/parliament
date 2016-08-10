

import urllib

i=1000

url = "http://www.psp.cz/sqw/detail.sqw?id=%s&t=11,1"
while i > 0:
    print i
    urllib.urlretrieve(url % i, filename="posls/%s.html" % i)
    i=i-1
