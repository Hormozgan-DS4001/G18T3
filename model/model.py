from ds import BinarySearchTree
BST = BinarySearchTree()

class File:
    def __init__(self, name: str, address: str, size: float):
        self.name = name
        self.address = address
        self.size = size


class Core:
    def __init__(self):
        self.BST = BinarySearchTree()
        self.memory = 0

    def add_file(self, n, add, s):
        temp = File(n,add, s)
        self.BST.insert(temp)
        change_memory(s)

    def show_files(self):
        self.BST.sum_all()

    def delete_file(self):
        pass

    def change_memory(self):
        pass


tree = Core()
tree.add_file('samin', 'D:', 256)
tree.show_files()
