#------- Rotation function ---------------#
# given a string, a index,(int),put the first int charcs on the back of the string
# Example: 
# rotate('Happy',0) => 'Happy'
# rotate('Happy',1) => 'appyH'
# rotate('Happy',12) =>'ppyHa' (12%5=2)
def rotate(string, indx):
    n=len(string)
    if indx==0:
        return string
    pos=indx%n
    front=string[:pos]
    back=string[pos:]
    return back+front

string='Happy'
indx=12
rotate(string,indx)

#-------------- manuplate with numpy array --------#
import numpy as np
arr=np.array([[0.2,0.2,0.3,0.2,0.1],
[0.0,0.1,0.5,0.3,0.1],
[0,0,0,0.5,0.5]])

# calculate the entropy for each row
def entropy(v):
    # default: v is a row vector
    e=0
    n=len(v)
    for i in range(n):
        if v[i]!=0:
            e=e-v[i]*np.log2(v[i])
    return e

entropy(arr[0,:])
e=list(map(entropy,arr))
e=np.array(e)

#------find the frequency of certain character in a string-----#
def fre(string,x):
    if x not in string:
        return 'not found'
    # build a disctionary to store the frequencies of the characters
    count={}
    for s in string:
        if s not in count:
            count[s]=1
        else:
            count[s]=count[s]+1
    
    return count[x]


string='aabcdef'
fre(string,'b')
fre(string,'m')
fre(string,'a')

#------------- reverse an integer ------------------------#
def reverse(x):
    sign=[-1 if x<0 else 1]
    sign=sign[0]
    rev=sign*int(str(x*sign)[::-1])
    if rev<2**31 and rev>=-2**31:
        return rev
    else: 
        return 0

#------------- sort a list -----------------------------#
def sortlist(l):
    if len(l)<=1:
        return l
    p=l[0] ## pivot
    left=[]
    right=[]
    equal=[p]
    for i in range(len(l)):
        if l[i]<p:
            left.append(l[i])
        elif l[i]>=p and i!=0:
            right.append(l[i])
    return sortlist(left)+equal+sortlist(right)

l=[3,5,2,1,2,7,7]
sortlist(l)      

## follow up, if the range of the list is known, for example: 1-15
## how can we improve the algorithm?
def followsort(l):
    ## given range of elements in l: 1-15
    d={}
    for i in range(1,16):
        d[i]=i
    
    sortedlist=[0]*15
    for x in l:
        indx=d[x]
        sortedlist[indx-1]=x
    
    res=[]
    for i in range(len(sortedlist)):
        if sortedlist[i]!=0:
            res.append(sortedlist[i])
    return res

l=[3,2,6,4,5]
followsort(l)

#-----merge sort-----##
def spl(l):
    ## spli l into two parts
    m=len(l)//2
    left=l[:m]
    right=l[m:]
    return left, right

def merge(left,right):
    ## merger two sorted array
    if len(left)==0:
        return right
    if len(right)==0:
        return left
    target=[]
    n=len(left)+len(right)
    p1=0 #pointer for the left array
    p2=0 #pointer for the right array
    while len(target)<n:
        if left[p1]<right[p2]:
            target.append(left[p1])
            p1 +=1
        else:
            target.append(right[p2])
            p2 +=1
        if p1==len(left):
            target.extend(right[p2:])
            break
        elif p2==len(right):
            target.extend(left[p1:])
            break
    return target
    
def mergesort(l):
    if len(l)<=1:
        return l
    else:
        left,right=spl(l)
        return merge(mergesort(left),mergesort(right))


left=[1,4,6,8]
right=[2,3,5,6]
merge(left,right)
mergesort(l)


