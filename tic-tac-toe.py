from tkinter import *
from tkmacosx import *
import time
import random


class TicTacToe:

    window = None

    # variables that hold the state of the game
    game_over = False
    is_user_turn = True
    tie = False
    count = 0

    # 2D list that keeps track of "X" or "O" at each box
    game_state = [["", "", ""],
                  ["", "", ""],
                  ["", "", ""]]

    # 2D list that holds the frames that make up the gameplay area
    frames = [[None, None, None],
              [None, None, None],
              [None, None, None]]

    # 2D list that holds the canvases that make up the gameplay area
    canvases = [[None, None, None],
                [None, None, None],
                [None, None, None]]

    # lists that keep track of winning squares
    w1 = []
    w2 = []
    w3 = []

    # variables that hold the shape that the user and computer have
    user_shape = "X"
    computer_shape = "O"

    # variables that hold the frame that will display gameplay options, gameplay state, and current score
    game_state_frame = None

    # variables that will be used for radio buttons
    radio_button_frame = None
    radio_button_label = None
    button_options = ["X", "O"]
    radio_var = None

    # variables that will be used to display the state of the game
    display_frame = None
    display_label = None
    display_status = None
    display_text = "Game in Progress "

    # variables to hold buttons that allow a user to quit or restart the game
    button_frame = None
    restart_button = None
    quit_button = None

    # constructor for tic-tac-toe class
    def __init__(self):

        # creates the window in which the game will be placed
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("552x652")
        self.window.resizable(False, False)

        # creates frame that will display gameplay options, gameplay state, and current score
        self.game_state_frame = Frame(self.window, highlightbackground="black", highlightthickness=4)
        self.game_state_frame.grid(row=0, column=0, columnspan=3)

        # creates radio button frame to select "X" or "O"
        self.radio_button_frame = Frame(self.game_state_frame, bg="black", highlightbackground="black",
                                        highlightthickness=4)
        self.radio_button_frame.grid(row=0, column=0)

        # creates label that tells player to select which shape to play as
        self.radio_button_label = Label(self.radio_button_frame, text="Player:", font=("Arial", 16), fg="black",
                                        bg="white", height=1, padx=27, pady=8)
        self.radio_button_label.grid(row=0, column=0)

        self.radio_var = IntVar()

        # creates radio buttons to select "X" or "O"
        for i in range(len(self.button_options)):
            Radiobutton(self.radio_button_frame, text=self.button_options[i], value=i, font=("Ariel", 16), width=10,
                        height=1, command=self.select_shape, variable=self.radio_var,
                        ).grid(row=i+1, column=0)

        # creates frame to hold labels that display the current state
        self.display_frame = Frame(self.game_state_frame, bg="black", highlightbackground="black", highlightthickness=4)
        self.display_frame.grid(row=0, column=1)

        # creates two labels to display the current state of the game
        self.display_label = Label(self.display_frame, text="GAME STATUS:", font=("Arial", 25), fg="black",
                                   bg="white", height=1, padx=56, pady=6)
        self.display_label.grid(row=0, column=1)
        self.display_status = Label(self.display_frame, text=self.display_text, font=("Arial", 25), fg="black",
                                    bg="#EEEEEE", height=1, padx=45, pady=7)
        self.display_status.grid(row=1, column=1)

        # creates button frame to allow user to restart or quit game
        self.button_frame = Frame(self.game_state_frame, bg="black", highlightbackground="black", highlightthickness=4)
        self.button_frame.grid(row=0, column=2)

        # creates restart button
        self.restart_button = Button(self.button_frame, text="Restart", font=("Arial", 20), command=self.restart,
                                     relief=RAISED, bd=5, fg="white", bg="blue", width=100, height=35,
                                     activebackground="light blue")
        self.restart_button.grid(row=0, column=2, columnspan=1)

        # creates quit button
        self.quit_button = Button(self.button_frame, text="Quit", font=("Arial", 20), command=self.quit,
                                  relief=RAISED, bd=5, fg="white", bg="red", width=100, height=35,
                                  activebackground="pink")
        self.quit_button.grid(row=1, column=2, columnspan=1)

        # creates the frames and canvases for the gameplay area
        for i in range(1, 4):
            for j in range(3):
                self.frames[i-1][j] = self.create_frame(r=i, c=j)
                self.canvases[i-1][j] = self.create_canvas(self.frames[i - 1][j])
                # binds the "turn" method to run whenever the gameplay area is clicked
                self.canvases[i-1][j].bind("<Button-1>", lambda e, row=i-1, col=j: self.turn(row, col))

    # method that creates frame and adds it to the gameplay area
    def create_frame(self, r, c):

        # creates Frame object, adds it to window, and returns it
        frame = Frame(self.window, bg="white", width=170, height=170, highlightbackground="black", highlightthickness=4)
        frame.grid(row=r, column=c)
        return frame

    # method that creates canvas and adds it to a given frame
    def create_canvas(self, f):

        # creates Canvas object, packs it into frame, and returns it
        canvas = Canvas(f, width=170, height=170, bg="white")
        canvas.pack()
        return canvas

    # method that runs whenever the gameplay area is clicked by the user
    def turn(self, r, c):

        # runs the user turn method
        self.user_turn(r, c)

        # if the user has made a move successfully, computer turn runs
        if not self.is_user_turn:
            self.computer_turn()

    # method that allows user to select a square to play
    def user_turn(self, r, c):

        # if game has ended, exit method and no more turns can be made
        if self.game_over:
            return

        # if place where user clicked is empty: draws shape, increases counter, and sets it to computer's turn
        if self.game_state[r][c] == "":
            self.draw_shape(c=self.canvases[r][c], shape=self.user_shape)
            self.game_state[r][c] = self.user_shape
            self.count += 1
            self.is_user_turn = False

        # if place where user clicked isn't empty, quits method and waits for user to click again
        else:
            return

        # checks to see if game is over (someone has won or a tie)
        self.check("X")
        if not self.game_over:
            self.check("O")

        # checks if there is a tie
        if self.count == 9 and not self.game_over:
            self.display_text = "Tie Game! "
            self.display_status["text"] = self.display_text
            self.display_status["padx"] = 87
            self.game_over = True
            self.tie = True

    # method that allows computer to select a square to play
    def computer_turn(self):

        # if game has ended, exit method and no more turns can be made
        if self.game_over:
            return

        # creates a list with all empty areas of the game
        possible_moves = []
        for r in range(3):
            for c in range(3):
                if self.game_state[r][c] == "":
                    possible_moves.append([r, c])

        # randomly selects an empty area for computer to draw a shape
        temp = random.choice(possible_moves)
        self.draw_shape(c=self.canvases[temp[0]][temp[1]], shape=self.computer_shape)
        self.game_state[temp[0]][temp[1]] = self.computer_shape
        self.count += 1
        self.is_user_turn = True

        # checks to see if game is over (someone has won or a tie)
        self.check("X")
        if not self.game_over:
            self.check("O")

        # checks if there is a tie
        if self.count == 9 and not self.game_over:
            self.display_text = "Tie Game! "
            self.display_status["text"] = self.display_text
            self.display_status["padx"] = 87
            self.game_over = True
            self.tie = True

    # method that draws an "X" or an "O" onto a canvas
    def draw_shape(self, c, shape):

        # draws an "X" in the canvas
        if shape == "X":
            c.create_line(34, 34, 136, 136, fill="black", width=10)
            c.create_line(34, 136, 136, 34, fill="black", width=10)
        # draws an "O" in the canvas
        if shape == "O":
            c.create_oval(34, 34, 136, 136, fill="white", width=10)

    # method checks if a given shape (X or O) has won the game yet
    def check(self, shape):

        # checks if a shape has won the game horizontally
        for i in range(3):
            if self.game_state[i][0] == self.game_state[i][1] == self.game_state[i][2] == shape:
                self.w1 = [i, 0]
                self.w2 = [i, 1]
                self.w3 = [i, 2]
                self.game_over = True

        # checks if a shape has won the game vertically
        for i in range(3):
            if self.game_state[0][i] == self.game_state[1][i] == self.game_state[2][i] == shape:
                self.w1 = [0, i]
                self.w2 = [1, i]
                self.w3 = [2, i]
                self.game_over = True

        # checks if a shape has won the game diagonally
        if self.game_state[0][0] == self.game_state[1][1] == self.game_state[2][2] == shape:
            self.w1 = [0, 0]
            self.w2 = [1, 1]
            self.w3 = [2, 2]
            self.game_over = True

        # checks if a shape has won the game diagonally
        elif self.game_state[0][2] == self.game_state[1][1] == self.game_state[2][0] == shape:
            self.w1 = [0, 2]
            self.w2 = [1, 1]
            self.w3 = [2, 0]
            self.game_over = True

        # runs if a given shape won
        if self.game_over:
            # displays the winner
            self.display_text = str(shape) + " is Winner!"
            self.display_status["text"] = self.display_text
            if shape == "X":
                self.display_status["padx"] = 82
            else:
                self.display_status["padx"] = 80

            # paints the winning squares a light green
            self.canvases[self.w1[0]][self.w1[1]]["bg"] = "light green"
            self.canvases[self.w2[0]][self.w2[1]]["bg"] = "light green"
            self.canvases[self.w3[0]][self.w3[1]]["bg"] = "light green"

    # method that allows user to select which shape they play as
    def select_shape(self):

        if self.radio_var.get() == 0:
            self.user_shape = "X"
            self.computer_shape = "O"
        elif self.radio_var.get() == 1:
            self.user_shape = "O"
            self.computer_shape = "X"

        self.restart()

    # method that restarts the game
    def restart(self):

        # clears all canvases
        for lc in self.canvases:
            for c in lc:
                c.delete("all")

        # resets display of game state
        self.display_text = "Game in Progress "
        self.display_status["text"] = self.display_text
        self.display_status["padx"] = 45

        # resets the colors of winning squares
        if self.game_over and not self.tie:
            self.canvases[self.w1[0]][self.w1[1]]["bg"] = "white"
            self.canvases[self.w2[0]][self.w2[1]]["bg"] = "white"
            self.canvases[self.w3[0]][self.w3[1]]["bg"] = "white"

            self.w1 = []
            self.w2 = []
            self.w3 = []

        # resets variables that keep track of game state
        self.game_over = False
        self.is_user_turn = False
        self.tie = False
        self.count = 0
        self.game_state = [["", "", ""],
                               ["", "", ""],
                               ["", "", ""]]

    # method that quits the current game and closes the widow
    def quit(self):

        self.window.destroy()

    # method that displays the game to be played
    def play(self):

        self.window.mainloop()


# main that runs and instantiates a tic-tac-toe game, then displays it to the screen
if __name__ == "__main__":
    myGame = TicTacToe()
    myGame.play()
