# Box for the user name entry.


import tkinter
from tkinter import messagebox


class NameEntry:

    def __init__(self, parent):
        self.pop = tkinter.Toplevel(parent)
        self.pop.geometry("220x50+700+400")
        self.pop.resizable(width=False, height=False)
        self.pop.title("Name")
        self.pop.attributes("-topmost", True)
        self.pop.grab_set()
        self.pop.wm_transient(parent)
        self.pop.bind("<Return>", self.__get_name)
        self.pop.protocol("WM_DELETE_WINDOW", self.__get_name)
        top_frame = tkinter.Frame(self.pop)
        self.box = tkinter.Entry(top_frame, bd=2)
        label = tkinter.Label(top_frame, text="Enter your name:  ")
        self.box.focus_set()
        self.button = tkinter.Button(self.pop, text="Submit", command=self.__get_name)
        self.user_name = ""

        top_frame.pack(side="top")
        label.pack(side="left")
        self.box.pack(side="left")
        self.button.pack(side="bottom")

    # Returns the user name from the entry box.
    def __get_name(self, event=None):
        if self.box.get() == "":
            self.user_name = "USER"
        elif len(self.box.get()) > 10:
            tkinter.messagebox.showinfo("Name too long", "Please enter a name shorter" +
                                        " than 10 characters.")
            self.box.delete("0", "end")
            return
        else:
            self.user_name = self.box.get()
        self.pop.destroy()

    # Returns the user name.
    def get_name(self):
        return self.user_name

    # Returns the Toplevel object.
    def window(self):
        return self.pop
