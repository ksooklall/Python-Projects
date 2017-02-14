"""
Bacteria Counters
NOT DONE INDEX PROBLEMS
"""

import numpy as np

def bacteriaCount(M):
    colony = 0
    m = len(M)
    n = len(M[0])

    for i in range(m-1):
        for j in range(n-1):
            bacteriaMark(M,n,m,i,j)
            colony+=1

def bacteriaMark(M,m,n,i,j):
    l = []
    l.append([i,j])
    c = 0
    while(len(l)>0):
        del l[c]
        c+=1
        x = l[0]
        y = l[1]
        if (M[x][y] == 1):
            M[x][y]=-1
            push(l,m,n,x-1,y)
            push(l,m,n,x,y-1)
            push(l,m,n,x+1,y)
            push(l,m,n,x,y+1)
            
def push(l,m,n,x,y):
    if x>=0 and x<m and y>=0 and y<n:
        return l.append([x,y])

if __name__ == '__main__':
    A = [[0,1,0,1,0],[0,0,1,1,1],[1,0,0,1,0],[0,1,1,0,0],[1,0,1,0,1]]
    #A = [[2,1,3,1,5],[0,0,1,1,1],[1,0,0,1,0],[0,1,1,0,0],[1,0,1,0,1],[4,5,6,7,8]]
    print(bacteriaCount(A))

