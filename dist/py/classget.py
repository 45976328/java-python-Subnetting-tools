
def getclassmask(mask):  # finds a class based on the mask
    mclass = 0
    if mask[0] == "255":
        mclass = 1
        if mask[1] == "255":   # mask[0] and mask[1] have the value 255 then mask is class B
            mclass = 2
            if mask[2] == "255":  # mask[0] , mask[1] and mask[2] have the value 255 then mask is class C
                mclass = 3
    return mclass

def getclassip(ip):  # finds the class of the given ip
    
    if int(ip[0]) >= 0 and int(ip[0]) <= 127:  # if first byte is between 0 and 127 then its a class A ip
        ipclass=1
    elif int(ip[0]) >= 128 and int(ip[0]) <= 191: # if first byte is between 128 and 191 then its a class B ip
        ipclass=2
    elif int(ip[0]) >= 192 and int(ip[0]) <= 223:   # if first byte is between 192 and 223 then its a class B ip
        ipclass=3
    else:
        ipclass=4

    return ipclass

def getclass(ip,mask):
    cl=getclassip(ip)

    if cl > getclassmask(mask):
        return "6"

    return cl
