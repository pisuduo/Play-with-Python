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
   