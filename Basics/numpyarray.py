import numpy as np
#sort a dataframe based on certain columns

a=np.array([(1,2,3),(3,4,5)])
b=np.array([[12,3,3],[2,6,5]])
c=np.array([[(1,2,3),(3,4,5)],[(2,3,4),(4,5,6)]])
a.reshape([3,2]) # will not change the original dataset
a.reshape(3,2)   # same
a.T
np.linspace(0,1,50) #including stop value
np.arange(0,1,0.1)  # excluding stop value

np.zeros((2,3))
np.full((2,2),3)
np.eye(3)
np.ones((2,3))

np.random.random(3)
np.empty((2,2))
a.shape ##array dimensions
a.ndim  ## number of array dimensions
a.size  ## number of elements in the array

## operations
a-b
a+b
d=np.array([1,2,3])
np.subtract(a,b)
print(np.add(a,b))
print(d)
print(a)
print(a+d)
a/b
np.divide(a,d)
a.dot(b.T)
np.log(a)
a==b
## aggregations
np.sum(a,0)
np.min(a,0)
np.max(b,1)
a.cumsum(1)
a.cumsum(0)
a.mean(0)
b.sort(0)

## boolean indexing
a[a<3]

##reshaping
a.ravel() ## flatting the array
b.reshape(3,-2)

## combining arrays
np.concatenate((a,b),0)
np.vstack((a,b))
np.hstack((a,b))
