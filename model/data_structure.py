

class BD:

    class _Node:
        def __init__(self, data, key):
            self.left = None
            self.right = None
            self.parent = None
            self.next = None
            self.prev = None
            self.data = data
            self.key = key

    def __init__(self):
        self.root = None
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def traverse_bst(self, order: str = "inorder", t: "BD._Node" = Ellipsis):
        if t is Ellipsis:
            t = self.root
        if not t:
            return
        if order == "inorder":
            yield from self.traverse_bst("inorder", t.left)
            yield t.data
            yield from self.traverse_bst("inorder", t.right)
        elif order == "my_order":
            yield from self.traverse_bst("my_order", t.right)
            yield t.data
            yield from self.traverse_bst("my_order", t.left)

    def traverse_dll(self, reverse=False):
        if not reverse:
            t = self.head
            while t:
                yield t.data
                t = t.next
        else:
            t = self.tail
            while t:
                yield t.data
                t = t.prev

    def insert(self, data, key):
        new_node = self._Node(data, key)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.root = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self._insert_bst(new_node, key)
        self.length += 1

    def _insert_bst(self, node, key):
        t = self.root
        if not t:
            self.root = node
            return
        while True:
            if t.key > key:
                if t.left:
                    t = t.left
                else:
                    t.left = node
                    break
            if t.key < key:
                if t.right:
                    t = t.right
                else:
                    t.right = node
                    break

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
            return deleted
        else:
            self.head = self.head.next
            self.head.prev = None
        if del_node.left is None and del_node.right is None:
            if del_node.key > del_node.parent.key:
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





