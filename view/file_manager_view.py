from configure import Frame, Button, LabelFrame, Label, Tk, Entry
from add_file_view import AddFile
from tkinter import ttk
import tkinter


class FileManagerPanel(Tk):
    def __init__(self, callback_new, callback_old, callback_more, callback_less, callback_memory,
                 callback_delete, callback_upload):
        super(FileManagerPanel, self).__init__()
        self.callback_new = callback_new
        self.callback_old = callback_old
        self.callback_more = callback_more
        self.callback_less = callback_less
        self.callback_memory = callback_memory
        self.callback_delete = callback_delete
        self.callback_upload = callback_upload
        frm_console = Frame(self)
        frm_console.grid(row=0, column=0)
        my_canvas = tkinter.Canvas(self)
        my_canvas.pack(side="left", fill="both", expand=1)
        my_scroll = ttk.Scrollbar(self, otient="vertical", command=my_canvas.yview)
        my_scroll.pack(side="right", fill="y")
        my_canvas.config(yscrollcommand=my_scroll.set)
        my_canvas.bind("<configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox("all")))
        self.frm = Frame(my_canvas)
        my_canvas.create_window((0, 0), window=self.frm, anchor="nw")

    def update_memory(self, text):
        pass

    def add_file(self):
        pass

    def change_memory(self):
        pass

    def next_page(self):
        pass

    def prev_page(self):
        pass



