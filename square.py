# Square objects (9 will be created).


import tkinter


class Square:

    def __init__(self, location, letter_color="red"):
        self.square = tkinter.Label(location, bd=2, relief="solid", text="",
                                    height=2, width=4, font=("Tahoma", 62))
        self.square.pack(side="left")
        self.__mark_count = 0
        self.__id = str(self.square.info).rstrip(">>").split(" ")[-1]
        self.__letter_color = letter_color

    # Marks a blue X if the square is clicked.
    def mark_x(self):
        self.square.config(text="X", fg="blue")
        self.__mark_count += 1

    # Changes the color of the machine's marks.
    def set_color(self, new_color):
        self.__letter_color = new_color

    # Returns the text of the square.
    def get_text(self):
        return self.square.cget("text")

    # Marks a red "O" (the machine mark).
    def mark_o(self):
        self.square.config(text="O", fg=self.__letter_color)
        self.__mark_count += 1

    # Returns the id of the square as a string float.
    def id(self):
        return self.__id

    # Returns the times the square has been clicked.
    def get_mark_count(self):
        return self.__mark_count

    # Clears the square and resets the clicks counter.
    def clear(self):
        self.square.config(text="")
        self.__mark_count = 0
