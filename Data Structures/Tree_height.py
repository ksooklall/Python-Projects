"""
Author@ KSooklall

Given a tree, no necessary a binary search tree this class will determine the
height

"""

from tree_node import Node

# Get tree height
def get_height(root):
    if root is None:
        return 0

    left = get_height(root.left)
    right = get_height(root.right)

    return 1+max(left,right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(7)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    root.left.left.left = Node(-1)
    root.left.right.right = Node(2)
    root.left.right.right.right = Node(4)
    print(get_height(root))
