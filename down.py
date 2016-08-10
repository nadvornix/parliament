

import urllib

i=50562

url = "http://www.psp.cz/cgi-bin/text/sqw/hlasy.sqw?G=%s&o=6"
while i > 1000:
    print i
    urllib.urlretrieve(url % i, filename="hlass/%s.html" % i)
    i=i-1
