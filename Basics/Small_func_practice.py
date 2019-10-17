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