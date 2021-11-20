class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, troot, e):
        temp = None
        while troot:
            temp = troot
            if e == troot.element:
                return
            elif e < troot.element:
                troot = troot.left
            elif e > troot.element:
                troot = troot.right
        n = Node(e)
        if self.root:
            if e < temp.element:
                temp.left = n
            else:
                temp.right = n
        else:
            self.root = n

    def inorder(self, troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element,end=' ')
            self.inorder(troot.right)