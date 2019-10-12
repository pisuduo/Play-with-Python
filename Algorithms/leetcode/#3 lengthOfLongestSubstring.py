## straightforward solution ##
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    ss=[x for x in s]
    maxlen=[]
    for i in range(len(ss)):
        visit=[]
        while i<len(ss) and ss[i] not in visit :
            visit.append(ss[i])
            i+=1
        l=len(visit)
        maxlen.append(l)
    if maxlen==[]:
        return 0
    else:
        return max(maxlen)

s="abcdbef"
lengthOfLongestSubstring(s)


### sliding windows ###

def lengthOfLongestSubstring2(s):
    l1,l2=len(s),len(set(s))
    if l1==0: return 0
    while l2>=0:
        for i in range(l1-l2+1):
            slide=s[i:i+l2]
            if len(set(slide))==l2:
                 return l2
        l2 -=1
    
## try optimizting the slide window :
