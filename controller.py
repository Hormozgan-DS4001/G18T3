from model import Core
from view import FileManagerPanel
from pickle import load, dump
from os.path import exists as file_exists

if file_exists("database.bin"):
    file = open("database.bin", "rb")
    database = load(file)
    file.close()
else:
    database = Core()

win = FileManagerPanel(database.order_by_newest, database.order_by_oldest, database.show_large_to_small,
                       database.show_small_to_large, database.change_memory, database.delete_file, database.add_file,
                       database.send_memory)
win.mainloop()


file = open("database.bin", "wb")
dump(database, file)
file.close()




