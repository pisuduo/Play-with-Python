###-------------------- MergeSort ---------------------###
def split(arr):
    ## arr should be of length>1
    m=len(arr)//2
    left=arr[:m]
    right=arr[m:]
    return left, right

def Merge(left, right):
    ## left, right are two sorted arrays
    ## returned the mergered sorted array
    if len(left)==0:
        return right
    elif len(right)==0:
        return left
    merged_arr=[]
    target_len=len(left)+len(right)
    left_indx=0
    right_indx=0

    while len(merged_arr)<target_len:
        if left[left_indx]<right[right_indx]:
            merged_arr.append(left[left_indx])
            left_indx +=1
        else:
            merged_arr.append(right[right_indx])
            right_indx +=1
        if left_indx==len(left):
            merged_arr=merged_arr+right[right_indx:]
            break
        elif right_indx==len(right):
            merged_arr=merged_arr+left[left_indx:]
            break
    return merged_arr
        

def MergeSort(arr):
    if len(arr)<=1:
        return arr
    else:
        left,right=split(arr)
        return Merge(MergeSort(left),MergeSort(right))
        
    