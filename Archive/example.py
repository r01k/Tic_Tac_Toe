
import tkinter, time


class Square:

    def __init__(self, location):
        self.square = tkinter.Label(location, bd=2, relief="solid", text="",
                                    height=2, width=4, font=("Tahoma", 62))
        self.square.pack(side="left")

    # Marks a blue X if the square is clicked.
    def mark_x(self):
        self.square.config(text="X", fg="blue")

    # Marks a red "O" (the machine mark).
    def mark_o(self):
        self.square.config(text="O", fg="red")


# Dictionary to store the square objects.
squares_dct = {}


class Board:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("600x300+500+80")
        self.main_window.bind("<Button-1>", self.square_clicked)
        top_frame = tkinter.Frame(self.main_window, width=600, height=200)

        # Initializes 2 square objects.
        squares_dct["a1"] = Square(top_frame)
        squares_dct["b1"] = Square(top_frame)

        top_frame.pack(side="top")
        tkinter.mainloop()

    @staticmethod
    # event is a required tkinter event object passed by the .bind function.
    def square_clicked(event):
        squares_dct["a1"].mark_x()
        # time.sleep(1)
        squares_dct["b1"].mark_o()


Board()
