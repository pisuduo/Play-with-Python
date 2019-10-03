###---------------------- 20 -----------------------------###
### using stack data structure ###
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s)%2 !=0:
        return False

    stack=[]
    map={')':'(','}':'{',']':'['}
    for x in s:
        if x in map:  ## x is a closing bracket
            top=stack.pop() if stack else '$'
            if top!=map[x]: return False
        else:
            stack.append(x)
    
    return stack==[]


s='(((([[}]]))))'
s1='{[(())]}'
isValid(s)
isValid(s1)

###------------------------- 301 --------------------------###

