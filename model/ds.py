class Node:
    def __init__(self, data = None,  left=None, right=None, next = None, prev = None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next
        self.prev = prev

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.head = None


    def rsearch(self, troot, key):
        if troot:
            if key == troot.data:
                return True
            elif key < troot.data:
                return self.rsearch(troot.left,key)
            elif key > troot.data:
                return self.rsearch(troot.right,key)
        else:
            return False

    def insert(self, s):
        temp = None
        troot = self.root
        while troot:
            temp = troot
            if s == troot.data:
                return
            elif s < troot.data:
                troot = troot.left
            elif s > troot.data:
                troot = troot.right

        f = Node(s)
        if self.root:
            if s < temp.data:
                temp.left = f
                temp.prev = f
            else:
                temp.right = f
                temp.next = f
        else:
            self.root = f
            self.head = f


    def delete(self,e):
        p = self.root
        pp = None
        while p and p.data != e:
            pp = p
            if e < p.data:
                p = p.left
            else:
                p = p.right
        if not p:
            return False
        if p.left and p.right:
            s = p.left
            ps = p
            while s.right:
                ps = s
                s = s.right
            p.data = s.data
            p = s
            pp = ps
        c = None
        if p.left:
            c = p.left
        else:
            c = p.right
        if p == self.root:
            self.root = None
        else:
            if p == pp.left:
                pp.left = c
            else:
                pp.right = c

#naghes
    def printlist(self):

        temp = self.head
        while temp.left:
            temp = temp.left

        while temp.next is None:
            print(temp.data)
            temp = temp.next

# in-order traverse - sort from the smallest to the largest one
    def inorder(self, troot):
        current = troot

        while current is not None:
            if current.left is None:
                yield current.data
                current = current.right
            else:
                pre = current.left
                while pre.right is not None and pre.right is not current:
                    pre = pre.right

                if pre.right is None:
                    pre.right = current
                    current = current.left

                else:
                    pre.right = None
                    yield current.data
                    current = current.right

    def sum_all(self):
        sum = 0
        for v in self.inorder(self.root):
            sum += v
        print(sum)

    def preorder(self, troot):
        if troot:
            print(troot.data,end=' ')
            self.preorder(troot.left)
            self.preorder(troot.right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.data, end=' ')


tree = BinarySearchTree()
tree.insert(45)
tree.insert(40)
tree.insert(550)
tree.insert(555)
tree.insert(451)
tree.insert(6)

tree.inorder(tree.root)
print('')
tree.sum_all()
print('')