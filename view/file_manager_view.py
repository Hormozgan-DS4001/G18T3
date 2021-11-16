from configure import Frame, Button, LabelFrame, Label, Tk, Entry
from tkinter import ttk


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

        









