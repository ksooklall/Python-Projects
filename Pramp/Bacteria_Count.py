"""
Bacteria Counters
NOT DONE INDEX PROBLEMS
"""

import numpy as np

def cultureCount(A):
    culture = 0
    for r in range(len(A)):         # Rows
        for c in range(len(A[0])):  # Columns
            if A[r][c] == 1:
                A[r][c] = -1
                # Label as seen
                if c > 0 and c < len(A[0])-1: # Edge case: Stay within bounds, west spill
                    if A[r][c-1]== 1:    
                        A[r][c-1] = -1
                    if A[r][c+1] == 1:
                        A[r][c+1] = -1
                if r > 0 and r < len(A)-1: # Edge case: Stay within bounds, north spill
                    if A[r-1][c]==1:
                        A[r-1][c] = -1
                    if A[r+1][c] == 1:
                        A[r+1][c] = -1
                if r == 0 or c == 0:
                    if A[r-1][c] == 1: A[r-1][c] = -1
                    if A[r][c+1] == 1: A[r][c+1] = -1
                    if A[r][c+1] != -1 or A[r+1][c] != -1:
                        culture +=1
                elif r == len(A) or c == len(A[0])-1:
                    if A[r-1][c] != -1 or A[r][c-1] != -1:
                        culture +=1
                else:
                    if A[r][c-1] != -1 or A[r][c+1]!=-1 or A[r-1][c]!=-1 or A[r+1][c]!=-1:
                        culture +=1                
    return culture

def boundryCheck(A,r,c):
    return r>=0 and r<=len(A) and c>=0 and c<=len(A[0])

if __name__ == '__main__':
    A = [[0,1,0,1,0],[0,0,1,1,1],[1,0,0,1,0],[0,1,1,0,0],[1,0,1,0,1]]
    #A = [[2,1,3,1,5],[0,0,1,1,1],[1,0,0,1,0],[0,1,1,0,0],[1,0,1,0,1],[4,5,6,7,8]]
    print(cultureCount(A))

