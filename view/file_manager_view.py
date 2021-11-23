from configure import Frame, Button, LabelFrame, Label, Tk, Entry, Scale
from add_file_view import AddFile
from tkinter import ttk
import tkinter


class FileManagerPanel(Tk):
    def __init__(self, callback_new, callback_old, callback_largest, callback_smallest, callback_memory,
                 callback_delete, callback_upload, callback_get_memory):
        super(FileManagerPanel, self).__init__()
        self.callback_new = callback_new
        self.callback_old = callback_old
        self.callback_largest = callback_largest
        self.callback_smallest = callback_smallest
        self.callback_memory = callback_memory
        self.callback_delete = callback_delete
        self.callback_upload = callback_upload
        self.callback_get_mem = callback_get_memory

        self.size_mem, self.full_mem = self.callback_get_mem()

        frm_console = Frame(self)
        frm_console.grid(row=0, column=0)
        my_canvas = tkinter.Canvas(frm_console)
        my_canvas.pack(side="left", fill="both", expand=1)
        my_scroll = ttk.Scrollbar(frm_console, orient="vertical", command=my_canvas.yview)
        my_scroll.pack(side="right", fill="y")
        my_canvas.config(yscrollcommand=my_scroll.set)
        my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox("all")))
        self.frm = Frame(my_canvas)
        my_canvas.create_window((0, 0), window=self.frm, anchor="nw")

        frm_btn = Frame(self)
        frm_btn.grid(row=1, column=0)
        Button(frm_btn, text="Upload", command=self.add_file).grid(row=0, column=0)
        Button(frm_btn, text="Change Memory", command=self.change_memory).grid(row=0, column=1)

        self.frm_mem = Frame(self)
        self.scale = Scale(self.frm_mem, width=18, length=122, from_=1, to=2048, orient="horizontal")
        self.scale.grid(row=0, column=0)
        Button(self.frm_mem, text="Ok", command=self.update_memory).grid(row=1, column=0)

        frm_tree = Frame(self)
        frm_tree.grid(row=3, column=0)
        self.result_sort = self.callback_new
        self.option_var = tkinter.StringVar()
        self.option_var.set("Newest to Oldest")
        tkinter.OptionMenu(frm_tree, self.option_var, ["Newest to Oldest", "Oldest to Newest", "Largest to Smallest",
                                                       "Smallest to Largest"],
                           command=self.result_om).grid(row=1, column=0, sticky="w")

        self.tree = ttk.Treeview(frm_tree, show="headings", selectmode="brows", height=10)
        self.tree["columns"] = ("name", "address", "size")
        self.tree.heading("name", text="Name")
        self.tree.heading("address", text="Address")
        self.tree.heading("size", text="Size")
        self.tree.grid(row=1, column=0)
        Label(self, text=f"{self.full_mem} GB of {self.size_mem} GB Used")

    def result_om(self):
        res = self.option_var.get()
        if res == "Newest to Oldest":
            self.result_sort = self.callback_new
        elif res == "Oldest to Newest":
            self.result_sort = self.callback_old
        elif res == "Largest to Smallest":
            self.result_sort = self.callback_largest
        else:
            self.result_sort = self.callback_smallest
        self.show_all()

    def change_memory(self):
        self.frm_mem.grid(row=2, column=0)

    def update_memory(self):
        strong = self.scale.get()
        self.callback_memory(strong)
        for node in self.callback_delete():
            Label(self.frm, text=f"Remove File - Name:{node.name} Size:{node.size} Address:{node.address}") \
                .pack(side="top").after(10000)
        self.frm_mem.grid_forget()
        self.update_label()

    def add_file(self):
        name = AddFile(self, "File Name: ", "Upload File").get_result()
        address = AddFile(self, "File Address: ", "Upload File").get_result()
        size = AddFile(self, "File Size: ", "Upload File").get_result()
        self.callback_upload(name, address, size)
        Label(self.frm, text=f"Upload File - Name:{name} Size:{size} Address:{address}").pack(side="top").after(10000)
        for node in self.callback_delete():
            Label(self.frm, text=f"Remove File - Name:{node.name} Size:{node.size} Address:{node.address}") \
                .pack(side="top").after(10000)
        self.update_label()

    def show_all(self):
        self.tree.delete(*self.tree.get_children())
        for i in self.result_sort():
            item = (i.name, i.address, i.size)
            self.tree.insert("", "end", value=item)

    def update_label(self):
        self.size_mem, self.full_mem = self.callback_get_mem()
