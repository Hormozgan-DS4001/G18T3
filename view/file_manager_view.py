from configure import Frame, Button, LabelFrame, Label, Tk, Entry, Scale
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
        frm_console = Frame(frm_console)
        frm_console.grid(row=0, column=0)
        my_canvas = tkinter.Canvas(self)
        my_canvas.pack(side="left", fill="both", expand=1)
        my_scroll = ttk.Scrollbar(self, otient="vertical", command=my_canvas.yview)
        my_scroll.pack(side="right", fill="y")
        my_canvas.config(yscrollcommand=my_scroll.set)
        my_canvas.bind("<configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox("all")))
        self.frm = Frame(my_canvas)
        my_canvas.create_window((0, 0), window=self.frm, anchor="nw")

        frm_btn = Frame(self)
        frm_btn.grid(row=1, column=0)
        Button(frm_btn, text="Upload", command=self.add_file()).grid(row=0, column=0)
        Button(frm_btn, text="Change Memory", command=self.change_memory()).grid(row=0, column=1)

        self.frm_mem = Frame(self)
        self.scale = Scale(self.frm_mem, width=18, length=122, from_=1, to=2048, orient="horizontal")
        self.scale.grid(row=0, column=0)
        Button(self.frm_mem, text="Ok", command=self.update_memory).grid(row=1, column=0)

    def change_memory(self):
        self.frm_mem.grid(row=2, column=0)

    def update_memory(self):
        strong = self.scale.get()

    def add_file(self):
        name = AddFile(self, "File Name: ", "Upload File").get_result()
        address = AddFile(self, "File Address: ", "Upload File").get_result()
        size = AddFile(self, "File Size: ", "Upload File").get_result()
        self.callback_upload(name, address, size)
        Label(self.frm, text=f"Upload File - Name:{name} Size:{size} Address:{address}").pack(side="top").after(10000)
        for node in self.callback_delete():
            Label(self.frm, text=f"Remove File - Name:{node.name} Size:{node.size} Address:{node.address}")\
                .pack(side="top").after(10000)

    def next_page(self):
        pass

    def prev_page(self):
        pass



