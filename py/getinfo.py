import sys
import binary
import classget

def getinfo(ip,mask):
    maskbin = binary.tobin(mask)
    cl = classget.getclass(ip,mask)

    maskbits=0
    for i in range(0,4):
        temp=maskbin[i] # get each item of list mb(mask binary)
        for j in range(0,len(temp)): #get each item of list mbi
            maskbits+=int(temp[j])   #add the ones and zeroes

    hostbits=32-maskbits

    if cl == 1: #"A":
        subnetbits=24-hostbits
        sbm="nnnnnnnn"
    elif cl == 2:#"B":
        subnetbits=16-hostbits
        sbm="nnnnnnnnnnnnnnnn"
    else:
        subnetbits=8-hostbits
        sbm="nnnnnnnnnnnnnnnnnnnnnnnn"

    for i in range(0,subnetbits): #add subnetbits amount of s's in sbm
        sbm+="s"
    for i in range(0,hostbits):
        sbm+="h"
    
    temp=""

    for i in range(0,len(sbm)):
        temp+=sbm[i]
        if i == 7 or i == 15 or i == 23:    #separate every 8 
            temp+="."
    sbm=temp
    
    return [maskbits, hostbits, subnetbits, pow(2,subnetbits), pow(2,hostbits)-2, sbm] #mask bits, host bits, subnet bits, number of subnets, hosts per subnet , subnet bit mask


print(getinfo(sys.argv[1].split("."),sys.argv[2].split(".")))