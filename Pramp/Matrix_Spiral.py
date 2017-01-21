"""
Matrix Spiral
Given an array of integers, return a clockwise spiral of the elements
"""

import numpy as np

def clockwiseSpiral(M):
    topRow = 0
    bottomRow = len(M)-1
    rightCol = len(M[0])-1
    leftCol = 0
    
    for i in range(len(M[0])):       # Printing top row
        print(M[topRow][i])          # len(M[0]) - Number of columns
    topRow+=1
    
    for i in range(1,len(M)):        # Printing right col
        print(M[i][rightCol])        # len(M) - Number of rows
    rightCol-=1

    for i in range(2,len(M[0])+1):     # Print bottom row 
        print(M[bottomRow][-i])      
    bottomRow-=1

    for i in range(1,len(M)-2):      # Print left col
        print(M[leftCol][i])
    leftCol+=1
    
    return 0
if __name__ == '__main__':
    matrix = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
    clockwiseSpiral(matrix)
