# Binary Search Tree

class Node:
    def __init__(self,val):
        self. value = val
        self.left = None
        self.right = None

    def insert(self, data):
        # Check if the data is already in the tree
        if self.value == data:
            return False
        # Check if the data is less than the current value
        elif self.value > data:
            # check for a left child
            # if there is one add the data to it
            if self.left:
                return self.left.insert(data)
            else:
            # if not create one
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self,data):
        if self.value == data:
            return True
        elif self.value>data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))

    def inorder(self):
        if self:       
            if self.left:
                self.left.inorder()
            print(str(self.value))
            if self.right:
                self.right.preorder()
class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        # Check if root node exists
        if self.root:
            return self.root.insert(data)
        else:
        # If the root node does not exist create it
            self.root = Node(data)
            return True

    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print('PreOrder')
        self.root.preorder()
    def postorder(self):
        print('PostOrder')
        self.root.postorder()
    def inorder(self):
        print('In order')
        self.root.inorder()

    def height(self, tree):
        if self.root:
            return (1+max(tree.height(self.root.left),
                          tree.height(self.root.right)))
        else:
            return 0
        
