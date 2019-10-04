### 1st solution ###
def insert(nums1,x,pos):
    ## insert x at at pos
    mm=len(nums1)
    for j in range(mm-1,pos,-1):
        temp=nums1[j-1]
        nums1[j]=temp
    
    nums1[pos]=x



nums1=[1,2,3,0,0,0]
insert(nums1,5,5)
nums1

def merge(nums1,nums2,m,n):
    for i in range(n):
        j=0
        check=False
        while j < i+m:
            if nums2[i]<=nums1[j]:
                insert(nums1,nums2[i],j)
                check=True
                break
            else: 
                j +=1
        if check==False:
            insert(nums1,nums2[i],i+m)
        

nums1=[4,0,0,0,0,0]
nums2=[1,2,3,5,6]
merge(nums1,nums2,1,5)
nums1

### 2nd solution, using two pointers ###

def mergearray(nums1,nums2,m,n):

    p1=m-1
    p2=n-1
    pos=m+n-1
    while p1>=0 and p2>=0:
        if nums1[p1]>nums2[p2]:
            nums1[pos]=nums1[p1]
            p1 -=1
        else:
            nums1[pos]=nums2[p2]
            p2 -=1
        pos -=1

    while p2>=0:
        nums1[pos]=nums2[p2]
        p2 -=1
        pos -=1

nums1=[4,0,0,0,0,0]
nums2=[1,2,3,5,6]
mergearray(nums1,nums2,1,5)
nums1
