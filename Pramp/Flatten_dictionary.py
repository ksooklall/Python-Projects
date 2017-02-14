"""
Dict compression
------------- NOT COMPLETE ----------------
"""

flatten = dict()
def compression(fatDict, k = None):
    for i,v in fatDict.items():
        if type(v) != dict and not k:
            flatten[i] = v
        else:
            parentK = k
        if type(v) == dict:
            flatten[parentK+'.'+i] = v
        else:
            compression(fatDict[k],k)
    return flatten
        
if __name__ == '__main__':
    fatDictionary = {'k1':'a',
               'k2':{
                   'a':'2',
                   'b':'3',
                   'c':{
                       'd':'3',
                       'e':'1'
                       }
                   }
               }
    print(compression(fatDictionary))
