

from math import sqrt

f=open("corm.csv")
m=[]
for line in f.xreadlines():
    l=[]
    for num in line.split():
        x=float(num)
        
        if x<0:
            x=x*x
            
            print x
            if x>0.035:
                x=x-0.0
                x=x*50
                
                x=int(x)
                print x
            else:
                x=0
        else:
            x=0
        
#        x=float(num)
        l.append(x)
    m.append(l)
#print m


for i in range(len(m)):
#    print i,":",
    for j in range(i):
#        print j,
        if m[i][j]>0:
            print "    {source:%s, target:%s, value:%s}," % (i,j,m[i][j])
#    print 


