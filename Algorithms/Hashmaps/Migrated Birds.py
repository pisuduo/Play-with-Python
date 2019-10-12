
def migratoryBirds(arr):
    types=list(set(arr))
    count=dict((x,0) for x in types)
    for i in range(len(arr)):
        if arr[i] in count:
            count[arr[i]] +=1
    
    return min([x for x in count.keys() if count[x]==max(count.values())])



def migratoryBirds2(arr):
    count = [0]*len(arr)
    for t in arr:
         count[t] += 1
    return count.index(max(count))



