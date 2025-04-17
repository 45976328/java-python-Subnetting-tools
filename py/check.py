import sys
import binary
import classget

def check(ip,mask,maskbin):

    if len(ip) != 4 :      #if length > or  < then print error
        print("1",end="") #dont change line or else .equals on java programm will not match
        exit()

    if len(mask) != 4 :  #if length > or  < then print error
        print("2",end="")
        exit()

    for i in range(0,4):
        if int(ip[i]) > 255 or int(ip[i]) < 0:
            print("3",end="")
            exit()

        if int(mask[i]) > 255 or int(mask[i]) < 0:
            print("4",end="")
            exit()
    
    temp = ""
    for i in range(0,4):
        temp+=maskbin[i]

    if "01" in temp:
        print("5",end="")
        exit()


    if (classget.getclass(ip,mask) == "6"):
        print("6",end="")  
        exit()    

    print("0",end="")



if "" in sys.argv[1].split("."):
        print("1",end="")
        exit()

if "" in sys.argv[2].split("."):
        print("2",end="")
        exit()


check( sys.argv[1].split("."), sys.argv[2].split("."), binary.tobin(sys.argv[2].split(".")) )


# codes
# 0 = no errors
# 1 = wrong ip size
# 2 = wrong mask size
# 3 = out of boundaries ip
# 4 = out of boundaries mask
# 5 = mask format wrong
# 6 = IP and Mask Classes don't match
