""" Given a string and an array find the first occurance in the string
containing all elements of the array A
"""

# T: O(n+m) for string of length n and array of length m
# S: O(m) temp has the length of array
def findingSub(string, array):
    count = 0
    array_len = len(array)
    for i in range(len(string)-array_len-1):
        temp = array
        sub = string[i:array_len+i]
        for j in sub:
            if j in temp:
                count += 1
                temp.remove(j)
        if count == array_len:
            return sub
    return -1

if __name__ == '__main__':
    string = 'xxyxzyzxy'
    array = ['x','y','z']
    print(findingSub(string,array))
