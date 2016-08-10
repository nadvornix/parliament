
import cPickle as cp

hs = cp.load(file("hlass.dump"))

ps = cp.load(file("poss.dump"))

for p in ps:
    print p.k,

print 

def find(h, k1):
    for hlas,k2 in h:
        if k1==k2:
            return hlas
    else:
        return None

for h in hs:
    for p in ps:
        hlas= find(h,p.k)
        if hlas:
            print hlas,
        else:
            print "?",
        
#        if hlas == "A":
#            r="A"
#        elif hlas == "N":
#            r="N"
#        elif hlas == "Z":
#            r="Z"
#        else:
#            r=0

#        print r,
    print 
