"""
Given a sorted array of integer elements, find the first occurance of
an elemnt that satifies the constraint:
arr[i] == i
If no such element exists return -1
"""

# T: O(n) - Go through the entire array
# S: O(1)
def bf_arraySearch(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1

# Noting that the array is sorted, a binary search is a better approach
# Efficient search
# T: O(log(n))
# S: O(1)
def es_arraySearch(arr):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] - mid == 0:
            return mid
        if mid < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    arr = [-8,0,1,2,3,4,5,7]
    print(bf_arraySearch(arr)) # Ans: 7
    print(es_arraySearch(arr)) # Ans: 7
