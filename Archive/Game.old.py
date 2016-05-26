# CPT 101-100 - Final Project: Tic-Tac-Toe, written by Michel Salazar-Garcia


import tkinter
from tkinter import messagebox
import random


# Global pseudo-constants for the dynamic python ID of the labels.
S4 = ""
S9 = ""
S2 = ""

S3 = ""
S5 = ""
S7 = ""

S8 = ""
S1 = ""
S6 = ""

# Global pseudo-constant dictionary for the dynamic square IDs.
squares_ids = {}

# Global pseudo-constant lists for the squares marked by user and
# machine.
user_marks = list()
machine_marks = list()

# Global pseudo-constant to determine who starts.
machine_starts = False


class Game:

    def __init__(self):
        # Initializes the main windows with a locked size.
        self.main_window = tkinter.Tk()
        self.main_window.resizable(width=False, height=False)
        self.main_window.geometry("600x650")

        # Initializes the top information frame and its 2 labes.
        self.instructions_frame = tkinter.Frame(self.main_window, width=600,
                                                height=50)
        self.label1 = tkinter.Label(self.instructions_frame,
                                    text="Welcome to Tic Tac Toe")

        border = 2
        font = "Tahoma"

        # Initializes the top 3 squares. (a1, b1, c1 = s4, s9, s2)
        self.top_frame = tkinter.Frame(self.main_window, width=600, height=200)
        self.s4 = tkinter.Label(self.top_frame, bd=border, relief="solid", text="",
                                height=2, width=4, font=(font, 62))
        self.s4.bind("<Button-1>", self.right_click)
        self.s9 = tkinter.Label(self.top_frame, bd=border, relief="solid", text="",
                                height=2, width=4, font=(font, 62))
        self.s9.bind("<Button-1>", self.right_click)
        self.s2 = tkinter.Label(self.top_frame, bd=border, relief="solid", text="",
                                height=2, width=4, font=(font, 62))
        self.s2.bind("<Button-1>", self.right_click)

        # Initializes the middle 3 squares. (a2, b2, c2 = s3, s5, s7)
        self.middle_frame = tkinter.Frame(self.main_window, width=600, height=200)
        self.s3 = tkinter.Label(self.middle_frame, bd=border, relief="solid", text="",
                                height=2, width=4, font=(font, 62))
        self.s3.bind("<Button-1>", self.right_click)
        self.s5 = tkinter.Label(self.middle_frame, bd=border, relief="solid", text="",
                                height=2, width=4, font=(font, 62))
        self.s5.bind("<Button-1>", self.right_click)
        self.s7 = tkinter.Label(self.middle_frame, bd=border, relief="solid", text="",
                                height=2, width=4, font=(font, 62))
        self.s7.bind("<Button-1>", self.right_click)

        # Initializes the bottom 3 squares. (a3, b3, c3 = s8, s1, s6)
        self.bottom_frame = tkinter.Frame(self.main_window, width=600, height=200)
        self.s8 = tkinter.Label(self.bottom_frame, bd=border, relief="solid", text="",
                                height=2, width=4, font=(font, 62))
        self.s8.bind("<Button-1>", self.right_click)
        self.s1 = tkinter.Label(self.bottom_frame, bd=border, relief="solid", text="",
                                height=2, width=4, font=(font, 62))
        self.s1.bind("<Button-1>", self.right_click)
        self.s6 = tkinter.Label(self.bottom_frame, bd=border, relief="solid", text="",
                                height=2, width=4, font=(font, 62))
        self.s6.bind("<Button-1>", self.right_click)

        global S4, S9, S2, S3, S5, S7, S8, S1, S6

        # Packs the information frame and its 2 labels.
        self.instructions_frame.pack(side="top")
        self.label1.pack(side="top")

        # Packs the top 3 squares inside the top frame.
        # Determines the dynamic ID of each square and assigns it to
        # the global pseudo-constants.
        self.top_frame.pack(side="top")
        self.s4.pack(side="left")
        S4 = str(self.s4.info).split(".")[-1].rstrip(">>")
        self.s9.pack(side="left")
        S9 = str(self.s9.info).split(".")[-1].rstrip(">>")
        self.s2.pack(side="left")
        S2 = str(self.s2.info).split(".")[-1].rstrip(">>")

        # Packs the middle 3 squares inside the middle frame.
        # Determines the dynamic ID of each square and assigns it to
        # the global pseudo-constants.
        self.middle_frame.pack(side="top")
        self.s3.pack(side="left")
        S3 = str(self.s3.info).split(".")[-1].rstrip(">>")
        self.s5.pack(side="left")
        S5 = str(self.s5.info).split(".")[-1].rstrip(">>")
        self.s7.pack(side="left")
        S7 = str(self.s7.info).split(".")[-1].rstrip(">>")

        # Packs the bottom 3 squares inside the bottom frame.
        # Determines the dynamic ID of each square and assigns it to
        # the global pseudo-constants.
        self.bottom_frame.pack(side="top")
        self.s8.pack(side="left")
        S8 = str(self.s8.info).split(".")[-1].rstrip(">>")
        self.s1.pack(side="left")
        S1 = str(self.s1.info).split(".")[-1].rstrip(">>")
        self.s6.pack(side="left")
        S6 = str(self.s6.info).split(".")[-1].rstrip(">>")

        # Assigns each dynamic square ID to the dictionary after formatting it.
        global squares_ids
        squares = [self.s1, self.s2, self.s3, self.s4, self.s5,
                   self.s6, self.s7, self.s8, self.s9]
        for i in range(len(squares)):
            squares_ids[i] = str(squares[i]).split(".")[-1].rstrip(">>")

        tkinter.mainloop()

    # Writes and X on the clicked square.
    def right_click(self, event):
        caller_id = str(event.widget).split(".")[-1]
        font_color = "blue"
        if caller_id == S4:
            self.s4.config(text="X", fg=font_color)
            caller = 4
        elif caller_id == S9:
            self.s9.config(text="X", fg=font_color)
            caller = 9
        elif caller_id == S2:
            self.s2.config(text="X", fg=font_color)
            caller = 2
        elif caller_id == S3:
            self.s3.config(text="X", fg=font_color)
            caller = 3
        elif caller_id == S5:
            self.s5.config(text="X", fg=font_color)
            caller = 5
        elif caller_id == S7:
            self.s7.config(text="X", fg=font_color)
            caller = 7
        elif caller_id == S8:
            self.s8.config(text="X", fg=font_color)
            caller = 8
        elif caller_id == S1:
            self.s1.config(text="X", fg=font_color)
            caller = 1
        else:
            self.s6.config(text="X", fg=font_color)
            caller = 6
        
        # Adds the selected square to the list for the user.
        user_marks.append(caller)

        # If the user won:
        if self.check_win("user"):
            self.display_result("user")
            # If it's the machine's turn to start:
            if not machine_starts:
                return

        # If no line-completing squares are found for the machine, searches
        # for line-completing squares for the user:
        if self.machine_click("machine") == "no candidates approved":
            # If no line-completing square are found for the user:
            if self.machine_click("user") == "no candidates approved":
                # If there are no line-completing squares for either the user
                # or the machine and more than 6 squares are marked after
                # the machine marks its square, it's a match.
                print(user_marks, machine_marks)  ################
                print(len(user_marks) + len(machine_marks))  #############
                if len(user_marks) + len(machine_marks) > 6:
                    print("match1")  #############
                    self.display_result("none")
                    # If it's the machine's turn to start:
                    if machine_starts:
                        self.machine_click(choose_random=True)
                # If there are no line-completing squares for either the user
                # or the machine and more than 6 squares are marked after
                # the machine marks its square, the machines chooses a random
                # square.
                else:
                    self.machine_click(choose_random=True)

        # If the machine won:
        if self.check_win("machine"):
            self.display_result("machine")
            # If it's the machine's turn to start:
            if machine_starts:
                self.machine_click(choose_random=True)
        # If the board is full:
        elif len(user_marks) + len(machine_marks) > 8:
            self.display_result("none")
            # If it's the machine's turn to start:
            if machine_starts:
                self.machine_click(choose_random=True)

        # If more than 6 squares are marked after
        # the machine marks its square:
        print(user_marks, machine_marks)################
        print(len(user_marks) + len(machine_marks))#############
        if len(user_marks) + len(machine_marks) > 6:
            # If no line-completing squares are found for the machine, searches
            # for line-completing squares for the user:
            if self.machine_click("machine", mark_square=False) == "no candidates approved":
                # If no line-completing square are found for the user:
                if self.machine_click("user", mark_square=False) == "no candidates approved":
                    # If more than 6 squares are marked after the machine marks its
                    # square and there are no line-completing squares for either the user
                    # or the machine, it's a match.
                    print("match2")#############
                    self.display_result("none")
                    # If it's the machine's turn to start:
                    if machine_starts:
                        self.machine_click(choose_random=True)

    def machine_click(self, candidates_for="machine", choose_random=False,
                      mark_square=True):
        if candidates_for == "machine":
            list1 = machine_marks[:]
            list2 = user_marks[:]
        else:
            list1 = user_marks[:]
            list2 = machine_marks[:]

        chosen_square = 0
        # Makes the machine select a random square.
        if choose_random:
            while 1:
                chosen_square = random.randint(1, 9)
                if str(chosen_square) not in str(machine_marks) and \
                                str(chosen_square) not in str(user_marks):
                    break
        else:
            exit_loop = False
            for line in ["492", "357", "816", "438", "951", "276", "456", "258"]:
                if exit_loop:
                    break
                line_squares = list()
                for square in line:
                    if square in str(list1):
                        line_squares.append(square)

                if len(line_squares) == 2:
                    candidate = 15 - (int(line_squares[0]) + int(line_squares[1]))
                    if candidate not in list2:
                        chosen_square = candidate
                        exit_loop = True
                        break

            if chosen_square == 0:
                return "no candidates approved"

        if mark_square:
            self.machine_select(chosen_square)
            machine_marks.append(chosen_square)
            print("Chosen square is", chosen_square)##################

        return "foo"  # Prevents TypeError

    def machine_select(self, chosen_square):
        font_color = "red"
        if chosen_square == 4:
            self.s4.config(text="O", fg=font_color)
        elif chosen_square == 9:
            self.s9.config(text="O", fg=font_color)
        elif chosen_square == 2:
            self.s2.config(text="O", fg=font_color)
        elif chosen_square == 3:
            self.s3.config(text="O", fg=font_color)
        elif chosen_square == 5:
            self.s5.config(text="O", fg=font_color)
        elif chosen_square == 7:
            self.s7.config(text="O", fg=font_color)
        elif chosen_square == 8:
            self.s8.config(text="O", fg=font_color)
        elif chosen_square == 1:
            self.s1.config(text="O", fg=font_color)
        elif chosen_square == 6:
            self.s6.config(text="O", fg=font_color)

    # Checks explicitly if a party won.
    @staticmethod
    def check_win(who):
        if who == "machine":
            marked_squares = machine_marks[:]
        else:
            marked_squares = user_marks[:]

        for line in ["492", "357", "816", "438", "951", "276", "456", "258"]:
            line_squares = list()
            for square in line:
                if square in str(marked_squares):
                    line_squares.append(square)
            if len(line_squares) == 3:
                return True
                
        return False

    # Displays who's the winner.
    def display_result(self, winner):
        self.main_window.bell()
        if winner == "user":
            tkinter.messagebox.showinfo("Meh", "You win.")
        elif winner == "machine" :
            tkinter.messagebox.showinfo("Hasta la vista", "The machine beats its creator.")
        else:
            tkinter.messagebox.showinfo("Cat game", "It's a match!")

        global machine_starts
        if machine_starts:
            machine_starts = False
        else:
            machine_starts = True

        self.clear_board()

    # Clears the board.
    def clear_board(self):
        self.s4.config(text="")
        self.s9.config(text="")
        self.s2.config(text="")
        self.s3.config(text="")
        self.s5.config(text="")
        self.s7.config(text="")
        self.s8.config(text="")
        self.s1.config(text="")
        self.s6.config(text="")

        # Recycles the global pseudo-constant lists for the squares marked
        # by the user and machine.
        global user_marks, machine_marks
        user_marks = list()
        machine_marks = list()
