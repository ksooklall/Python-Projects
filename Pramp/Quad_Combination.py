"""
Quad Combination

Given an array of numbers arr and a number S, find 4 different numbers in arr
that sum up to S.

Write a function that gets arr and S and returns an array with 4 indices of such
numbers in arr, or null if no such combination exists.
Explain and code the most efficient solution possible, and analyze its runtime
and space complexity.
"""

def inefficient(arr,s):
    for i in range(len(arr)-3):
        for j in range(1,len(arr)-2):
            for k in range(2,len(arr)-1):
                for l in range(3,len(arr)):
                    c = arr[i]+arr[j]+arr[k]+arr[l]
                    if c == s:
                        return [i,j,k,l]
    return null

def efficient(arr,s):
    h = dict()
    for i in range(len(arr)):
        for j in range(len(arr)):
            h.update({arr[i]+arr[j] : [i,j]})
    for i in h.getKeys():
        pass
    return h
if __name__ == '__main__':
    arr = [0,1,2,3,4,5,6,7] #2,4,5,6
    s = 21 #3+5+6+7
    ans = inefficient(arr,s)
    a = efficient(arr,s)
    print(a)
