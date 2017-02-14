"""
Given an array where each element is at most k distance away from
it's correct sorted position. 
"""

# Brute force approach without considerating k
# T: O(n^m) - Each pass requirest looking back m elements
# S: O(1)

def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        print('temp:{} j:{}'.format(temp,j))
        while (arr[j]>temp and j>=0):
            arr[j+1] = arr[j]
            j-=1
        print('after while j:{}'.format(j))
        arr[j+1] = temp
    return arr

# Future update will add using K

if __name__ == '__main__':
    arr = [1,2,3,9,8,7]
    print(insertionSort(arr))
