from data_structure import BST


class File:
    def __init__(self, name: str, address: str, size: int):
        self.name = name
        self.address = address
        self.size = size


class Core:
    def __init__(self):
        self.memory = 0
        self.file_list = BST()

    def add_file(self, name, address, size):
        pass

    def delete_file(self):
        pass

    def change_memory(self):
        pass




