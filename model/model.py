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
        pass

    def delete_file(self):
        while self.size_files >= self.memory:
            deleted = self.file_list.delete()
            yield deleted
            self.size_files -= deleted.size

    def change_memory(self, size: int):
        self.memory = size




