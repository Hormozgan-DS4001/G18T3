from data_structure import BD


class File:
    def __init__(self, name: str, address: str, size: int):
        self.name = name
        self.address = address
        self.size = size


class Core:
    def __init__(self):
        self.memory = 0
        self.size_files = 0
        self.file_list = BD()

    def add_file(self, name: str, address: str, size: int):
        temp = File(name, address, size)
        self.file_list.insert(temp, size)
        self.size_files += temp.size

    def delete_file(self):
        while self.size_files >= self.memory:
            deleted = self.file_list.delete()
            yield deleted
            self.size_files -= deleted.size

    def change_memory(self, size: int):
        self.memory = size

    def show_files(self):
        self.file_list.traverse_bst()

    def send_memory(self):
        return self.size_files, self.memory

    def show_small_to_large(self):
        self.file_list.traverse_bst()

    def show_large_to_small(self):
        a = []
        a.append(self.file_list.traverse_bst())
        for i in a[::-1]:
            yield a[i-1]

    def order_by_oldest(self):
        self.file_list.traverse_dll()

    def order_by_newest(self):
        a = []
        a.append(self.file_list.traverse_dll())
        for i in a[::-1]:
            yield a[i - 1]
