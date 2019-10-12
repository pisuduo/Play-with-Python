def towords(n):
    ## n is at most three digits
    ## convert n to english words
    word1=['One','Two','Three','Four','Five','Six','Seven','Eight',
    'Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen',
    'Sixteen','Seventeen','Eighteen','Nineteen']
    word2=['Twenty','Thirty','Forty','Fifty','Sixty','Seventy',
    'Eighty','Ninety']

    hundred=n//100
    ten=n%100//10
    digit=n%10

    res=[]
    if hundred>0:
        res.append(word1[hundred-1])
        res += ['Hundred']
    if ten >=2:
        res.append(word2[ten-2])
        if digit >0:
            res.append(word1[digit-1])
    elif ten<2:
        if ten*10+digit !=0:
            res.append(word1[ten*10+digit-1])


    return ' '.join(res)

def integertowords(n):
    ## divide the integer into four parts
    if n==0:
        return "zero"

    numstr=str(n)[::-1]  ## reverse the numstring
    l=len(numstr)
    parts=[numstr[i:i+3][::-1] for i in range(0,l,3)] 
    ## divide into parts in which the length is smaller than 3, staring from right to left

    baselist=[' ',' Thousand ',' Million ',' Billion ']

    res=''
    for i in range(len(parts)):
        temp= towords(int(parts[i]))
        res = temp+('' if not temp else baselist[i])+res
    
    return res.rstrip()



