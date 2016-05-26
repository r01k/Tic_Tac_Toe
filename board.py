# Main module. Controls the whole execution.


import tkinter
from tkinter import messagebox
import boaster
import square
import name_entry
import random
from win32com.shell import shell, shellcon
import datetime
import winsound
import pickle
import time

squares_dct = {}
machine_starts = False

# Constant list for the machine mark random color selection on each game.
COLORS = ['snow', 'gainsboro', 'linen', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose',
    'deep sky blue', 'sky blue', 'steel blue',
    'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod',
    'yellow', 'gold', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'seashell2', 'seashell3', 'seashell4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4']


class Board:

    def __init__(self):
        self.start_time = time.time()
        # Application start time to determine if the boaster instance
        # needs to be closed when exiting.
        self.main_window = tkinter.Tk()
        self.main_window.resizable(width=False, height=False)
        self.main_window.wm_title("Tic Tac Toe")
        self.main_window.geometry("600x690+500+80")
        self.main_window.bind("<Button-1>", self.square_clicked)
        self.main_window.protocol("WM_DELETE_WINDOW", self.confirm_quit)
        self.hist_score_window = ""
        self.main_window.after(3000, lambda: self.show_history())
        
        instructions_frame = tkinter.Frame(self.main_window)

        user_label = tkinter.Label(instructions_frame, fg="blue", font=("Tahoma", 15),
                                   text="USER:")
        self.user_score = tkinter.StringVar()
        self.user_score.set(0)
        user_score_label = tkinter.Label(instructions_frame, fg="blue",
                                         font=("Tahoma", 15), textvariable=self.user_score)
        self.historic_score = list()
        buffer = " " * 10
        left_buffer_label = tkinter.Label(instructions_frame, text=buffer)
        welcome_label = tkinter.Label(instructions_frame, height=2, width=25,
                                      text=" " * 8 + "Welcome to Tic Tac Toe",
                                      font=("Tahoma", 15))
        right_buffer_label = tkinter.Label(instructions_frame, text=buffer)
        machine_label = tkinter.Label(instructions_frame, fg="red", font=("Tahoma", 15),
                                      text="MACHINE:")
        self.machine_score = tkinter.StringVar()
        self.machine_score.set(0)
        machine_score_label = tkinter.Label(instructions_frame, fg="red",
                                            font=("Tahoma", 15), textvariable=self.machine_score)
        
        top_frame = tkinter.Frame(self.main_window, width=600, height=200)
        middle_frame = tkinter.Frame(self.main_window, width=600, height=200)
        bottom_frame = tkinter.Frame(self.main_window, width=600, height=200)

        # Sets the initial color of the machine marks.
        square_letter_color = COLORS[random.randint(0, len(COLORS) - 1)]
        # Generates the 9 squares.
        squares_dct[4] = square.Square(top_frame, square_letter_color)
        squares_dct[9] = square.Square(top_frame, square_letter_color)
        squares_dct[2] = square.Square(top_frame, square_letter_color)

        squares_dct[3] = square.Square(middle_frame, square_letter_color)
        squares_dct[5] = square.Square(middle_frame, square_letter_color)
        squares_dct[7] = square.Square(middle_frame, square_letter_color)

        squares_dct[8] = square.Square(bottom_frame, square_letter_color)
        squares_dct[1] = square.Square(bottom_frame, square_letter_color)
        squares_dct[6] = square.Square(bottom_frame, square_letter_color)
        
        instructions_frame.pack(side="top")
        user_label.pack(side="left")
        user_score_label.pack(side="left")
        left_buffer_label.pack(side="left")
        welcome_label.pack(side="left")
        right_buffer_label.pack(side="left")
        machine_label.pack(side="left")
        machine_score_label.pack(side="right")
            
        top_frame.pack(side="top")
        middle_frame.pack(side="top")
        bottom_frame.pack(side="top")

        # Waits for the user's name from the pop window.
        self.user_name = name_entry.NameEntry(self.main_window)
        self.main_window.wait_window(self.user_name.window())
        self.user_name = self.user_name.get_name().upper()
        user_label.config(text=self.user_name + ":")
        buffer = " " * (10 - (len(self.user_name) - 4))
        left_buffer_label.config(text=buffer)
        right_buffer_label.config(text=buffer)

        tkinter.mainloop()

    # Initializes the historic score announcement.
    def show_history(self):
        self.hist_score_window = boaster.Boaster()

    # Drives the execution after each mouse click.
    def square_clicked(self, event):
        # Check if the click was not on a square.
        if self.out_of_board(event):
            return

        # Check if the clicked square is already marked.
        if not self.already_marked(event.widget):
            # Marks an blue X in the square.
            self.mark_x(event.widget)
            # Check if the user just won.
            if not self.check_win("user"):
                # Search for a line-completing square for the machine.
                if self.search_completing("machine") != "nothing found":
                    squares_dct[self.search_completing("machine")].mark_o()
                # Search for a line-completing square for the user.
                elif self.search_completing("user") != "nothing found":
                    squares_dct[self.search_completing("user")].mark_o()
                # Search for a free corner.
                elif self.search_corners() != "nothing found":
                    squares_dct[self.search_corners()].mark_o()
                # Check if the centre is free.
                elif squares_dct[5].get_text() == "":
                    squares_dct[5].mark_o()
                # Search for a free side
                elif self.search_sides() != "nothing found":
                    squares_dct[self.search_sides()].mark_o()

                # Check if the machine just won.
                if not self.check_win("machine"):
                    # Check if the board is full.
                    if self.board_full():
                        self.display_result("none")

    # Checks if the click was not on a square.
    @staticmethod
    def out_of_board(event):
        for n in range(1, 10):
            if squares_dct[n].id() == str(event.widget):
                return False
        return True

    # Returns True if the clicked square is already marked.
    @staticmethod
    def already_marked(caller_id):
        caller_id = str(caller_id)
        for square_number, square_obj in squares_dct.items():
            if caller_id == square_obj.id():
                if square_obj.get_mark_count() > 1:
                    winsound.PlaySound("SystemHand", winsound.SND_ASYNC)
                    return True
        return False

    # Marks a blue X in the square.
    @staticmethod
    def mark_x(caller_id):
        caller_id = str(caller_id)
        for square_number, square_obj in squares_dct.items():
            if caller_id == square_obj.id():
                square_obj.mark_x()

    # Checks explicitly if "who" won.
    def check_win(self, who="machine"):
        for line in ["492", "357", "816", "438", "951", "276", "456", "258"]:
            line_squares = list()
            for square_number in line:
                if square_number in str(self.check_marks(who)):
                    line_squares.append(square_number)

            if len(line_squares) == 3:
                # Updates the score.
                if who == "machine":
                    self.machine_score.set(int(self.machine_score.get()) + 1)
                else:
                    self.user_score.set(int(self.user_score.get()) + 1)
                self.display_result(who)
                return True
        return False

    # Displays the outcome of each game.
    def display_result(self, winner):
        self.main_window.bell()
        if winner == "user":
            self.main_window.config(bg="blue")
            tkinter.messagebox.showinfo("Meh", "You win.")
        elif winner == "machine":
            self.main_window.config(bg="red")
            tkinter.messagebox.showinfo("Hasta la vista", "The machine beats it" +
                                        "creator.")
        else:
            tkinter.messagebox.showinfo("Cat game", "It's a match!")
        self.new_game()
        if machine_starts:
            squares_dct[self.search_corners()].mark_o()

    # Returns a list with which squares are marked for "who".
    @staticmethod
    def check_marks(who="machine"):
        if who == "user":
            mark = "X"
        else:
            mark = "O"

        marked_squares = list()
        for number, square_obj in squares_dct.items():
            # Gets the text of the square.
            if square_obj.get_text() == mark:
                marked_squares.append(number)
        return marked_squares

    # Returns the square number that will complete a line for "who".
    def search_completing(self, who="machine"):
        if who == "machine":
            other_party = "user"
        else:
            other_party = "machine"

        for line in ["492", "357", "816", "438", "951", "276", "456", "258"]:
            line_squares = list()
            for square_number in line:
                if square_number in str(self.check_marks(who)):
                    line_squares.append(square_number)

            if len(line_squares) == 2:
                candidate = 15 - (int(line_squares[0]) + int(line_squares[1]))
                if candidate not in self.check_marks(other_party):
                    return candidate
        return "nothing found"

    # Returns the number of a random free corner.
    @staticmethod
    def search_corners():
        squares_list = list()
        for n in range(2, 10, 2):
            if squares_dct[n].get_text() == "":
                squares_list.append(n)
        if len(squares_list) == 1:
            return squares_list[0]
        elif len(squares_list) > 1:
            return squares_list[random.randint(0, len(squares_list) - 1)]
        else:
            return "nothing found"

    # Returns the number of a random free side.
    @staticmethod
    def search_sides():
        squares_list = list()
        if squares_dct[1].get_text() == "":
            squares_list.append(1)
        if squares_dct[3].get_text() == "":
            squares_list.append(3)
        if squares_dct[7].get_text() == "":
            squares_list.append(7)
        if squares_dct[9].get_text() == "":
            squares_list.append(9)

        if len(squares_list) == 1:
            return squares_list[0]
        elif len(squares_list) > 1:
            return squares_list[random.randint(0, len(squares_list) - 1)]
        else:
            return "nothing found"

    # Checks if the board is full.
    @staticmethod
    def board_full():
        counter = 0
        for n in range(1, 10):
            if squares_dct[n].get_text() != "":
                counter += 1
        if counter == 9:
            return True
        else:
            return False

    # Clears the board and resets the squares clicks counter.
    def new_game(self):
        # Decides who starts next game.
        global machine_starts
        if machine_starts:
            machine_starts = False
        else:
            machine_starts = True

        # Sets the new color of the machine marks.
        new_color = COLORS[random.randint(0, len(COLORS) - 1)]
        # Clears the squares.
        for n in range(1, 10):
            squares_dct[n].clear()
            squares_dct[n].set_color(new_color)
        self.main_window.config(bg="SystemButtonFace")

    # Confirms windows closure and saves current scores.
    def confirm_quit(self):
        winsound.PlaySound("SystemQuestion", winsound.SND_ASYNC)
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            # Prevents an exception if the boaster window has already been closed.
            try:
                self.hist_score_window.destroy_me()
            except:
                pass
            if int(self.user_score.get()) > 0 or int(self.machine_score.get()) > 0:
                empty = False
                historic_score = open("histcore.dat", "rb")
                try:
                    score = pickle.load(historic_score)
                except EOFError:
                    empty = True
                historic_score.close()             
                historic_score = open("histcore.dat", "wb")
                if not empty:
                    pickle.dump([int(self.user_score.get()) + score[0],
                                 int(self.machine_score.get()) + score[1]], historic_score)
                else:
                    score = open("histcore.dat", "wb")
                    pickle.dump([int(self.user_score.get()), int(self.machine_score.get())], score)
                historic_score.close()
                
                file_name = shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0) +\
                            "\Tic Tac Toe Score " + datetime.datetime.now().strftime\
                    ("%Y-%m-%d_%H.%M.%d") + ".txt"
                score_file = open(file_name, "w")
                score_file.writelines(self.user_name + ": " + self.user_score.get() +
                                      "\nMACHINE: " + self.machine_score.get())
                score_file.close()
                tkinter.messagebox.showinfo("Score", "Current score was saved to your Desktop")
            self.main_window.destroy()
