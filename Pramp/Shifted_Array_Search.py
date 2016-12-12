"""
Shifted Array Search

1. Find a given number num in a sorted array arr:
arr = [2, 4, 5, 9, 12, 17] 

2. If the sorted array arr is shifted left by an unknown offset and you don't have a pre-shifted copy of it, how would you modify your method to find a number in the shifted array?
shiftArr = [9, 12, 17, 2, 4, 5]

Explain and code an efficient solution and analyze its runtime complexity
if num doesn't exist in the array, return -1

Hints & Tips
The first part of the question is there to make sure that your peer understands binary search. Make sure this is the case

If your peer doesn't understand binary search go ahead and explain it, but be sure to reduce your rating on the knowledge section of the interview feedback 

A common attempt to reach a solution is by concatenating the shifted array to itself (will produce [9, 12, 17, 2, 4, 5, 9, 12, 17, 2, 4, 5] according to the example)
While this seems right, it's then difficult to tune what half of the array to focus on next (left/right). Be aware of that if your peer tries it.

Watch for mistakes with index calculations (division results not rounded, out of array bounds, forgotten indices etc.)

If uncertain of different solution approaches taken by your peer, ask your peer to explain why the solution is always correct for all cases and examine it together

Correct solution must involve O(log n) runtime complexity

    a = [2,9,12,17,18,19,20]
    n = 17
    print(BinarySearchTree(a,n))
"""

# Part 1 Solution: Since the array is already sorted, a binary search is an optmial
# approach
# Binary search tree algorithm
# T: O(log(n))
# S: O(1)
def BinarySearchTree(arr,leftS, rightS, num):
   left = leftS
   right = rightS
   while (left <= right):
      mid = (left+right)//2
      if arr[mid] < num:
         left = mid+1
      elif arr[mid] == num:
         return mid
      else:
         right = mid-1
   return -1

# Part 2 Solution: Find where the shift occured and apply binary search on
# both sides. There are two way to find where the shift has occured.

# Linear search, starting from the right side os the array and checking
# when arr[i] < arr[i-1]
# T: O(k) where k is the number of shifted elements, worst case k = n-1
# S: O(1)

def getShiftedIndexLinear(arr):
   l = len(arr)
   for i in range(1,len(arr)):
      if arr[-i]-arr[-i-1]<0:
         index = i
   return len(arr)-index

# Modified Binary search, keep splitting the array until arr[mid] < arr[mid-1]
# T: O(log(n)) Similar to binary search
# S: O(1)
def getShiftedIndexBS(arr):
   left = 0
   right = len(arr)
   while (left <= right):
      m = (left+right)//2
      if (arr[m] < arr[m-1]):
         return m
      if arr[m]>arr[0]:
         left = m + 1
      else:
         right = m - 1
   return 0

# Once the shift location is known apply BST on both sides of the shift
def BSTShifted(arr,num):
   shifted = getShiftedIndexBS(arr)
   left = BinarySearchTree(arr,0,shifted-1,num)
   right = BinarySearchTree(arr,shifted,len(arr)-1,num)
   if left != -1: return left
   if right != -1: return right
   else: return -1
   
if __name__ == '__main__':
   shiftArr = [9, 12, 17, 2, 4, 5]
   print(BSTShifted(shiftArr,12))
