###--------------------- Recursion ------------------------- ###
## Fibonacci Sequence (straightforward) ##
def Fib(n):
    if n<0:
        print ("Error: Input is negative!")
    elif n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return Fib(n-1)+Fib(n-2)

Fib(0)
Fib(1)
Fib(9)


## Fibonacci Sequence (Dynamic Programming) ##
def Fib_DP(n):
    fib=[0,1]
    if n<0:
        print ("Error: Input is negative!")
    elif n<=1:
        return fib[n]
    for x in range(2,n+1):
        fib.append(fib[x-1]+fib[x-2])
    return fib[n]
   
###------------------------ Sorting ---------------------- ###

## QuickSort: 1 Partition ##

def quickSort(arr):
    p=arr[0]  ## pivot
    n=len(arr)
    left=[]
    equal=[]
    right=[]
    for i in range(n):
        if arr[i]<p:
            left.append(arr[i])
        elif arr[i]==p:
            equal.append(arr[i])
        elif arr[i]>p:
            right.append(arr[i])
    res=left+equal+right
    return res


b=[4,5,3,7,2]
result = quickSort(b)
' '.join(map(str, result))

## QuickSort: 2 Sorting ##

def quickSort2(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)-1]  ## can customize pivot, either 1st, last or random choice
    #pivot=arr[0]
    equal=[pivot]
    left,right=[],[]   
    for x in arr:
        if x<pivot:
            left.append(x)
        elif x>pivot:
            right.append(x)
    return quickSort2(left)+equal+quickSort2(right)
    
#testing
t=[3,5,1,2,7,9,8]
print(quickSort2(t))

