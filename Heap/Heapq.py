import heapq
L=[10,20,30,20,50,60,80,9]
heapq.heapify(L)
heapq.nlargest(2,L) ## find the 2 largest element in L
heapq.nsmallest(1,L) 
heapq.heappush(L,2)  ##push a new element in the heap
heapq.nsmallest(1,L)

heapq.heappushpop(L,1) ## push 1 in the heap then pops and return the samllest
L[0] ## returns the smallest element on the heap without popping it.


###  Heaps Boot Camp ###

## Given a sequence of strings, find the k longest strings in the sequence

## Idea:  using a min heap, , track the k longest structure
## if a longer string is added to the sequence, then pop the smallest.

import itertools
def top_k(k, stream):
    heap=[(len(s),s) for s in itertools.islice(stream,k)] ## initialize the heap with the first k strings
    heapq.heapify(heap)
    for nextstring in stream:
        heapq.heappushpop(heap,(len(nextstring),nextstring))
    
    return [s[1] for s in heap]
    


stream=["abced",'theo',"kkkkkkk","werrd","ttttttttttt","theo"]
top_k(2,stream)

## if find the k shortest strings, using maxheap
def shortest_k(k, stream):
    heap=[(-len(s),s) for s in itertools.islice(stream,k)] ## initialize the heap with the first k strings
    heapq.heapify(heap)
    for nextstring in stream:
        heapq.heappushpop(heap,(-len(nextstring),nextstring))
    
    return [s[1] for s in heap]
    


stream=["abced",'theo',"kkkkkkk","werrd","ttttttttttt","theo"]
shortest_k(2,stream)
