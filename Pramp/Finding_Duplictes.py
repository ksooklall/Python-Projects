"""
Given two sorted array find of unequal extreme lengths return all duplicates
"""

# Since both arry are sorted use binary search on the larger to find
# T: O(n*log(m)) <> O(m*log(n)) where log(x) x smallest
# S: O(1)

def find_duplicates(arr1,arr2):
    # Determine which array is larger
    smallest, largest = (arr1,arr2) if len(arr1)<len(arr2) else (arr2,arr1)
    duplicates = []                     # Create an empty array for duplicates
    
    for i in smallest:                  # Go through the smallest list
        left = 0     
        right = len(largest)-1
        while left<=right:              # Apply binary search
            middle = (right+left)//2
            if largest[middle] == i:
                duplicates.append(i)
            if largest[middle] > i:
                right = middle - 1
            else:
                left = middle + 1
    return duplicates if len(duplicates)>0 else -1  # Return -1 if none

if __name__ == '__main__':
    arr1 = [1,2,12,23,32,46,57,62,73,84,95,101]
    arr2 = [1,2,53,56,95]
    print(find_duplicates(arr1,arr2))   # Ans = [1,2,95]
