import sys
import classget
import binary

def generate(maskbits, hostbits, subnetbits, noofsubnets, hostspersub, sbm, ip, mask): #info [mask bits 0, host bits 1, subnetbits 2, number of subnets 3, hosts per subnet 4, subnet bit mask 5], class, ipbin

    info = [int(maskbits), int(hostbits), int(subnetbits), int(noofsubnets), int(hostspersub), sbm]
    cl = classget.getclass(ip.split("."),mask.split("."))
    ip = binary.tobin(ip.split("."))
    
    
    #netbits=32-info[1]-info[2] #network bits
    
    temp=""
    net=""      #network bits (no change)
    sub=[]      #all subnet bitss
    host=""     #
    broad=""    #broadcast bits
    frm=""      #host range host bits from  (ex. 00000001)
    to=""       #host range host bits to    (ex. 11111110)

    listbin=[]
    list=[]
    

    if cl >= 1: #A
        temp=ip[0]
        for i in range(0,8):
            net+=temp[i]
    
    if cl >= 2: #B
        temp=ip[1]
        for i in range(0,8):
            net+=temp[i]
    
    if cl == 3: #C
        temp=ip[2]
        for i in range(0,8):
            net+=temp[i]
    
    temp=""
    for i in range(0,info[2]): #subnet bits
        temp+="0"
    sub.append(temp)

    for i in range(0,info[3]-1): #all subnet bits (from 0 to snumber of subnets -1)
        temp=bin(int(temp,2)+1)[2:] #make temp (binary) into int ,add 1 and make it into binary again, type str
        for j in range(0,info[2]):  #add missing 0 infront of temp 
            if len(temp) < info[2]:
                temp="0"+temp
        sub.append(temp)
    
    for i in range(0,info[1]):  #host bits of subnet id, also broadcast 
        host+="0"               #host bits for subnet id
        broad+="1"              #host bits for broadcast

    for i in range(0,info[1]):
        if i == info[1]-1:
            frm+="1"
            to+="0"
        else:
            frm+="0"
            to+="1"
    #print(net,sub,host,broad,frm,to)

    temp=net
    for i in range(0,info[3]): #from 0 to snumber of subnets
        temp+=sub[i]

        subnetid=temp+host
        hrfrom=temp+frm
        hrto=temp+to
        broadcast=temp+broad

        temp=net

        listbin.append([subnetid,hrfrom,hrto,broadcast])

    c=1
    temp=""
    dec=""
    templist=[]
    list=[]

    for i in listbin:
        for j in i:
            for k in j:
                temp+=k
                if c == 8 or c == 16 or c == 24:
                    dec+=str(int(temp,2))+"."
                    temp=""
                c+=1
            dec+=str(int(temp,2))
            templist.append(dec)
            temp=""
            dec=""
            c=1
        list.append(templist)
        templist=[]

    return list



print( generate(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]), end="")


# print( generate("24","8","0","1","254","nnnnnnnn.nnnnnnnn.nnnnnnnn.hhhhhhhh", "192.168.1.1", "255.255.255.0"))

# #print( generate("192.168.1.1", "255.255.255.0"))