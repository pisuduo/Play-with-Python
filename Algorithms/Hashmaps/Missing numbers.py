def missingNumbers(arr, brr):

    typeb=list(set(brr))
    #counta=countb=[0]*len(typeb)
    counta=dict((x,0) for x in typeb)
    countb=dict((x,0) for x in typeb)
    result=[]

    for i in range(len(brr)):
        if brr[i] in typeb:
            countb[brr[i]] +=1

    for i in range(len(arr)):
        if arr[i] in typeb:
            counta[arr[i]] +=1

    indx=[x<y for x, y in zip(counta.values(),countb.values())]

    for i in range(len(countb)):
        if indx[i]==True:
            result.append(typeb[i])
    return sorted(result)

### optimizing the algorithm ###

## find the minimum, create a array with size 100, start from the minimum value
def missingNumbers2(arr,brr):
    mini=min(brr)
    A=[0]*100

    for x in brr:   ## add +1 if occur in barray
        indx=x-mini
        A[indx] +=1
    
    for y in arr:   ## subtract 1 if occur in a array
        indx=y-mini
        A[indx] -=1
    
    result=[]
    for i in range(100):  ## mising value with: value in A >0
        if A[i]>0:
            result.append(i+mini)

    return result

    

