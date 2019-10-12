## using two pointers ##
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    n=len(nums)
    res=set()
    for i in range(n-1):
        left=i+1
        right=n-1
        while left<right:
            if nums[i]+nums[left]+nums[right]==0:
                res.add((nums[i],nums[left],nums[right]))
                left +=1
                right -=1
            elif nums[i]+nums[left]+nums[right]<0:
                left +=1
            else:
                right -=1
    return res
        

nums=[-1, 0, 1, 2, -1, -4]
threeSum(nums)

