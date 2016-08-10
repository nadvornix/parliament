
import os, sys, re
from BeautifulSoup import BeautifulSoup as BS
import datetime as dt

class Poslanec():
    pass

from IPython.Shell import IPShellEmbed
ipshell = IPShellEmbed()


#data = file(sys.argv[1]).read().decode("cp1250")
def parsePos(data):
    s=BS(data)

    p = Poslanec()
    t=s.title
    p.jmeno = t.contents[0].replace("MBA","").split(",")[0].split(".")[-1].strip()

#    ipshell()
    
    klub=s.findAll("a", href=re.compile(r"fsnem.sqw\?id=[0-9]+"))[0]
    k=re.match('.*id=([0-9]+)&amp;o=6">([^<]+)</a>',str(klub))

    p.klub=(k.group(1),k.group(2))
    return p

