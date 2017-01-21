"""
Array of Array Products

Given an array of integers arr, write a function that returns another array at
the same length where the value at each index i is the product of all array
values except arr[i].

Solve without using division and analyze the runtime and space complexity

Example: given the array [2, 7, 3, 4]
your function would return: [84, 24, 56, 42]
(by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3])
"""

import numpy as np

# Brute force approach
# T: O(n^2) - Double for loop
# S: O(n)   - Return a new array of same size as given array

def arrayProducts(arr):
    p = 1
    prod = []
    for i in range(len(arr)):       # Fix index i
        for j in range(len(arr)):   # Having index J move
            if i!=j:                # Check when they are the same
                p *= arr[j]
        prod.append(p)
        p = 1
    return prod

# Efficient approach
# T: O(n)   - Multiple single for loops
# S: O(n)   - Return a new array of same size as given array
def efficientArrayProducts(arr):
    n = len(arr)
    prodArr = []
    for i in range(n):              # Create an array of ones
        prodArr.append(1)
    p = 1                           
    for i in range(n):
        prodArr[i] *= p
        p *= arr[i]
    print(prodArr)
    p = 1
    for i in range(n-1,-1,-1):
        prodArr[i]*= p
        p*= arr[i]
    return prodArr

if __name__ == '__main__':
    arr = [2,7,3,4]
    print(arrayProducts(arr))           # Ans: [82,24,56,42]
    print(efficientArrayProducts(arr))
