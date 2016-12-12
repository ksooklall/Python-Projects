"""
Find two integers that sum to one 

Given an array A of integers and an integer N, return the index of two integers
in A such that ai+aj = N for i and j in A. Return -1 if no such integers exists.
Determine space and time complexity.

Example:
A = [5,3,7,0,1,4,2]
N = 6
return 0,4

Bonus: Return the values in A that sum to N
"""

# Brute force
# Time complexity   -   O(n^2): Using a double for loop
# Space complexity  -   O(1):   Only keeping the index values i and j in memory
def brutePairSum(A,N):
    for i in range(len(A)):
        for j in range(1,len(A)):
            if A[i]+A[j]==N:
                return [i,j]
    return -1

# Efficient
# We are looking for two values ai+aj = N, so we can solve for one of them
# and look for the other. ai = N - ajCollect elements in a hash map
# Time complexity   - O(n): Length of the Aay
# Space complexity  - O(n): Hasing the Aay
def efficientPairSum(A,N):
    h = dict()
    for i in range(len(A)):
        ai = N-A[i]
        if ai in h:
            return j,h[ai]   # Return the index
            #return ai,A[i] # Return the array values
        h[A[i]] = i
    return -1

if __name__ == '__main__':
    A = [5,3,7,0,1,4,2]
    N = 6
    print(brutePairSum(A,N))    # Ans = [0,4]
    print(efficientPairSum(A,N))# Ans = (0,4)
    
