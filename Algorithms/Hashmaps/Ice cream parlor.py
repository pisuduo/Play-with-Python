### Basic solution: O (n^2) ###
import os
import re
import sys

def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==m:
                return i+1,j+1

### Turn it into a search problem, given first element, find the second element: m-element1 ###
### O(n) ###
def icecreamParlor2(m,arr):
    cost=dict()
    for i in range(len(arr)):
        if arr[i] not in cost:
            cost[m-arr[i]]=i+1 #put the complement in the dictionary
        else:
            return sorted([i+1,cost[arr[i]]])





m=6
arr=[1,4,2,5]

m=8
arr=[2, 1, 9, 4, 4, 56, 90, 3]

arr=[2, 1, 9, 4, 56, 90, 4]




icecreamParlor(m,arr)
icecreamParlor2(m,arr)