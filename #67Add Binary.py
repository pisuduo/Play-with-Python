n=10

x="2"
x.zfill(n)

## Add Binary ##
 def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    maxlen=max(len(a),len(b))
    a=a.zfill(maxlen)
    b=b.zfill(maxlen)

    result=""
    hold=0
    for i in range(maxlen-1,-1,-1):
        hold += 1 if a[i]=="1" else 0
        hold += 1 if b[i]=="1" else 0

        if hold == 2:
            result= "0"+result
            hold =1
        elif hold == 0:
            result= "0"+result
            hold =0
        elif hold==3:
            result="1"+result
            hold=1
        elif hold ==1:
            result= "1"+result
            hold=0
            
    if hold != 0: 
        result= "1"+ result

    return result
          
          
a="1111"
b="1111"
addBinary(a,b)
