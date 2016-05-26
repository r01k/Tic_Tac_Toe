# Message announcing the historic score.


import tkinter
import pickle
import random

COLORS = ["red", "yellow", "pink", "green", "purple", "orange",
          "blue"]


class Boaster:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.resizable(width=False, height=False)
        self.root.wm_title("")
        self.root.geometry("200x120+1300+200")

        self.label = tkinter.Label(self.root, text="HISTORIC SCORE:",
                                   font=("Tahoma", 17))
        self.users_score = tkinter.Label(self.root, text="HUMANS: ",
                                         font=("Tahoma", 15))
        self.machine_score = tkinter.Label(self.root, text="MACHINE: ",
                                           font=("Tahoma", 15))

        self.label.pack(side="top")
        self.users_score.pack()
        self.machine_score.pack()
        self.root.after(15000, lambda: self.root.destroy())
        self.change_color()
    
    # Changes the color of the main label randomly.
    def change_color(self, counter=1):
        try:
            historic_score = open("histcore.dat", "rb")
            score = pickle.load(historic_score)
            historic_score.close()
        except IOError:
            return
        
        self.label.config(fg=COLORS[random.randint(0, 6)])
        self.users_score.config(text="HUMANS: " + str(score[0]))
        self.machine_score.config(text="MACHINE: " + str(score[1]))
        # Prevents try to keep running the lambda after the window
        # has been destroyed by the .after method in __init__. This
        # causes a benign error when self.destroy_me is called before
        # the counter runs out.
        if counter < 50:
            # Recursive call.
            self.root.after(300, lambda: self.change_color(counter + 1))

    # Destroys the object.
    def destroy_me(self):
        self.root.destroy()
