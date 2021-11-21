class File:
    def __init__(self, name: str, address: str, size: int,  left=None, right=None, next = None, prev = None):
        self.name = name
        self.address = address
        self.size = size
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
            if key == troot.size:
                return True
            elif key < troot.size:
                return self.rsearch(troot.left,key)
            elif key > troot.size:
                return self.rsearch(troot.right,key)
        else:
            return False

    def insert(self, n, add, s):
        temp = None
        troot = self.root
        while troot:
            temp = troot
            if s == troot.size:
                return
            elif s < troot.size:
                troot = troot.left
            elif s > troot.size:
                troot = troot.right

        f = File(n, add, s)
        if self.root:
            if s < temp.size:
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
        while p and p.size != e:
            pp = p
            if e < p.size:
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
            p.size = s.size
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

    def printlist(self):

        temp = self.head
        while temp.left:
            temp = temp.left

        while temp.next is not None:
            print(temp.size)
            temp = temp.next

# in-order traverse - sort from the smallest to the largest one
    def inorder(self, troot):
        current = troot

        while current is not None:
            if current.left is None:
                yield current.size
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
                    yield current.size
                    current = current.right

    def sum_all(self):
        sum = 0
        for v in self.inorder(tree.root):
            sum += v
        print(sum)

    def preorder(self, troot):
        if troot:
            print(troot.size,end=' ')
            self.preorder(troot.left)
            self.preorder(troot.right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.size, end=' ')

    def addBT(self, troot):
        if troot is None:
            return 0
        return(troot.size + self.addBT(troot.left) + self.addBT(troot.right))

tree = BinarySearchTree()
tree.insert('f1', 'fsfs', 45)
tree.insert('f5461', 'nrf', 40)
tree.insert('eheh', 'hereh', 550)
tree.insert('eheh', 'thrh', 555)
tree.insert('efwsf', 'htrhr', 451)
tree.insert('fsfs', 'nfg', 6)

tree.inorder(tree.root)
print('')
tree.sum_all()
print('')
