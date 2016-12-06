"""
Merging 2 Packages

Given a package with a weight limit and an array arr of item weights, how can
you most efficiently find two items with sum of weights that equals the weight
limit?

Your function should return 2 such indices of item weights or -1 if such pair
doesn't exist.
What is the runtime and space complexity of your solution?
"""

# Brute force
# Space complexity  -   O(n^2): Using a double for loop
# Time complexity   -   O(1):   Only keeping the index values i and j in memory
def bruteMerge(arr,lim):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i]+arr[j]==lim:
                return [i,j]
    return -1

# Efficient
def efficientMerge(arr,lim):
    h = dict()
    for i in range(len(arr)-1):
        t = arr[i]+arr[i+1]
        print(t)
        if t not in h:
            h[t] = [i,i+1]
        if t == lim:
            return h[t]
    print(h)
    return -1

def fcw(arr,lim):
    h = dict()
    for i,v in enumerate(arr):
        if (lim-v) in h:
            c = h[lim-v]
        if c!=None:
            return [i,c]
        else:
            h[w] = v
    return -1

if __name__ == '__main__':
    arr = [1,2,3,4,54,5,67,7,8]
    lim = 56
    print(bruteMerge(arr,lim)) # Ans = [1,4]
    print(efficientMerge(arr,lim)) # Ans = [1,4]
    print(fcw(arr,lim))
