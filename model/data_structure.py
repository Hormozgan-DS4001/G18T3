

class BST:
    class _Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.parent = None
            self.next = None
            self.prev = None
            self.data = data

    def __init__(self):
        self.root = None
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, data):
        new_node = self._Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.root = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self._insert_bst(self.root, new_node)
        self.length += 1

    def _insert_bst(self, root, node):
        if root is None:
            return node
        if root.data < node.data:
            r_child = self._insert_bst(root.right, node)
            root.right = r_child
            r_child.parent = root
        else:
            l_child = self._insert_bst(root.left, node)
            root.left = l_child
            l_child.parent = root
        return root

    @staticmethod
    def successor(node):
        t = node
        p = None
        while t.left:
            p = t
            t = t.left
        return t, p

    def delete(self):
        del_node = self.head
        deleted = self.head.data
        self.length -= 1
        if self.length == 0:
            self.tail = None
            self.head = None
            self.root = None
            return
        else:
            self.head = self.head.next
            self.head.prev = None
        if del_node.left is None and del_node.right is None:
            if del_node.data > del_node.parent.data:
                del_node.parent.right = None
            else:
                del_node.parent.left = None
        elif del_node.left and del_node.right:
            suc, pare = self.successor(del_node.right)
            if pare:
                pare.left = suc.right
            else:
                del_node.right = suc.right
            del_node.data = suc.data
        else:
            child = del_node.left if del_node.left else del_node.right
            del_node.data = child
        return deleted

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)




