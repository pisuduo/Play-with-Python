## 26. Remove Duplicates from Sorted Array
def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums)==0:
        return 0
    i=0   # slow pointer
    j=1
    while j<=len(nums)-1:
        if nums[i]!=nums[j]:
            i +=1
            nums[i]=nums[j]
        j +=1
    return i+1

## 27. Remove Element
def removeElement(self, nums: List[int], val: int) -> int:
    i=0 # slow pointer
    j=0 # fast pointer
    while j <= len(nums)-1:
        if nums[j]!=val:
            nums[i]=nums[j]
            i +=1
        j +=1
    return i



## 28. Implement strStr()
def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0
    for i in range(len(haystack)-len(needle)+1):
        for j in range(len(needle)):
            if haystack[i+j]!=needle[j]:
                break
            if j== len(needle)-1:
                return i
    return -1