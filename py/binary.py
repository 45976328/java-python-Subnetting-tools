def dectobin(dec): #gets a dec and returns a bin
    bin=""
    for i in range(7,-1,-1):
        if dec >= pow(2,i):
            dec-=pow(2,i)
            bin+="1"
        else:
            bin+="0"
    return bin

def tobin(dec): #gets a list of decs and returns a list of bins
    bin=[]
    for i in range(0,len(dec)):
        bin.append( dectobin( int ( dec[i] ) ) ) 
    return bin      #type [str]
