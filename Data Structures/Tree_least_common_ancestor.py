"""
Author@ KSooklall

Determine the least common ancestor of two nodes in a tree

"""
from Binary_Search_Tree import Node

def least_common_ancestor(root,node1, node2):
    if root == None:
        return None

    if root.value == node1 or root.value == node2:
        return root

    left = least_common_ancestor(root.left,node1,node2)
    right = least_common_ancestor(root.right,node1,node2)

    if left != None and right != None:
        return root

    if left == None and right == None:
        return None

    if left != None:
        return left
    else: return right

if __name__ == '__main__':
    root = Node(10)
    root.insert(7)
    root.insert(8)
    root.insert(1)
    root.insert(3)
    root.insert(5)
    root.insert(9)
    root.insert(-1)
    root.insert(2)
    root.insert(4)
    root.insert(12)
    root.insert(11)
    root.insert(13)
    # Answer should be 10
    print(least_common_ancestor(root,2,13).value)
