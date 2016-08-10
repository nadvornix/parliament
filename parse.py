import os, sys, re
from BeautifulSoup import BeautifulSoup as BS
import datetime as dt


class Hlasovani():
    pass


#filename = sys.argv[1]

def getH(filename):
    f=open(filename)
    data=f.read().decode("cp1250")

    soup = BS(data)

    h = Hlasovani()
    title = soup.find('h2', align="center")

    schuze, hlasovani = soup.title.contents[0].split(" - ")[1].split("/")

    h.schuze = int(schuze)
    h.hlasovani = int(hlasovani)

    datum = soup.find("h2").contents[2][2:]

    h.datum = dt.datetime.strptime(datum, "%d.&nbsp;%m.&nbsp;%Y, %H:%M")
    h.nazev = soup.find("h2").contents[-1]
    a=soup.findAll("td", align="CENTER")

    h.pritomno = int(a[0].contents[0].split("=")[1])
    h.jetreba = int(a[1].contents[0].split("=")[1])

    h.hlasy = re.findall(r'<TD>(.)</TD><TD align=left><a href="detail\.sqw\?id=([0-9]+)&o=6">',data)

    h.hlasy = map(lambda x: (x[0],int(x[1])),h.hlasy)
#    print h.datum,h.nazev, h.pritomno, h.jetreba, h.hlasy
    return h



