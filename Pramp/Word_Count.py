"""
Given a string, return the count of each word
"""

# Initial approach
# T: O(n*m) - Read each element of the doc and check each element for punctuation
# S: O(n)   - Space for the dictionary
def wordCount(words):
    word = words.split(' ')             # Split the words by spaces
    h = {}                              # Create empty dict
    pun = '!@#$%%^^&*()-.0123456789'    # All common punctuation
    for i in word:
        for j in i:                     # Check each word for a punctuation
            if j in pun:
                b = i.replace(j,'')
            else:
                b = i
        if b.lower() in h:              # If word in dict increase count
            h[b] += 1
        else:                           # else add word to dict
            h[b] = 1
    return h

if __name__ == '__main__':
    doc = 'practice makes perfect. get perfect by practice. just practice!'
    print(wordCount(doc))
    # Ans: {'just': 1, 'practice': 3, 'makes': 1, 'by': 1, 'perfect': 2, 'get': 1}
    # Order of the elements is not fixed due to nature of dict
