import tkinter

win = tkinter.Tk()
def varian(win):
    print(optoin_var.get())

optoin_var = tkinter.StringVar(win)
optoin_var.set("new to old")
mode = ["newest to oldest", "oldest to newest", "largest to smallest", "smallest to largest"]
om = tkinter.OptionMenu(win, optoin_var, *mode, command=varian)
om.grid(row=0, column=0)
win.mainloop()

