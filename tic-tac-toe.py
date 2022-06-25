from tkinter import *
from tkmacosx import *
import time
import random


class TicTacToe:

    window = None

    # variables that hold the state of the game
    gameOver = False
    count = 0

    # 2D list that keeps track of x or o at each box
    gameState = [["", "", ""],
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

    # variables that hold the shape that the user and computer have
    user_shape = "o"
    computerShape = "x"

    # variables that hold the frame that will display gameplay options, gameplay state, and current score
    game_state_frame = None

    # variables that will be used for radio buttons
    radio_button_frame = None
    radio_button_label = None
    button_options = ["X", "O"]
    # x = IntVar()

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

        # creates radio buttons to select "X" or "O"
        for i in range(len(self.button_options)):
            Radiobutton(self.radio_button_frame, text=self.button_options[i], value=i, font=("Ariel", 16), width=10,
                        height=1, # variable=self.x, command=function
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
                # binds the "turn" function to run whenever the gameplay area is clicked
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

    # method that draws an x or an o onto a canvas
    def draw_shape(self, c, shape):

        # draws an "X" in the canvas
        if shape == "x":
            c.create_line(34, 34, 136, 136, fill="black", width=10)
            c.create_line(34, 136, 136, 34, fill="black", width=10)
        # draws an "O" in the canvas
        if shape == "o":
            c.create_oval(34, 34, 136, 136, fill="white", width=10)

    # method that runs whenever the gameplay area is clicked by the user
    def turn(self, r, c):

        # runs the user turn function
        self.user_turn(r, c)

        if not self.gameOver and self.count < 9:
            self.computer_turn()

        if self.count == 9:
            self.display_text = "Tie!"
            self.display_label["text"] = self.display_text

        print(self.count)

    def user_turn(self, r, c):

        if self.gameState[r][c] == "" and self.count < 9 and self.gameOver == False:

            self.draw_shape(c=self.canvases[r][c], shape=self.user_shape)
            self.gameState[r][c] = self.user_shape
            self.count += 1

        else:
            return

        if self.check_winner("x"):
            self.display_text = "X is Winner!"
            self.display_status["text"] = self.display_text

        elif self.check_winner("o"):
            self.display_text = "O is Winner!"
            self.display_status["text"] = self.display_text

    def computer_turn(self):

        possible_moves = []

        for r in range(3):
            for c in range(3):
                if self.gameState[r][c] == "":
                    possible_moves.append([r, c])

        temp = random.choice(possible_moves)
        self.draw_shape(c=self.canvases[temp[0]][temp[1]], shape=self.computerShape)
        self.gameState[temp[0]][temp[1]] = self.computerShape
        self.count += 1

        if self.check_winner("x"):
            self.display_text = "X is Winner!"
            self.display_status["text"] = self.display_text

        elif self.check_winner("o"):
            self.display_text = "O is Winner!"
            self.display_status["text"] = self.display_text

    # method checks if a given shape (X or O) has won the game yet
    def check_winner(self, shape):

        # checks possible winning combinations
        if (self.gameState[0][0] == self.gameState[0][1] == self.gameState[0][2] == shape or
            self.gameState[1][0] == self.gameState[1][1] == self.gameState[1][2] == shape or
            self.gameState[2][0] == self.gameState[2][1] == self.gameState[2][2] == shape or
            self.gameState[0][0] == self.gameState[1][0] == self.gameState[2][0] == shape or
            self.gameState[0][1] == self.gameState[1][1] == self.gameState[2][1] == shape or
            self.gameState[0][2] == self.gameState[1][2] == self.gameState[2][2] == shape or
            self.gameState[0][0] == self.gameState[1][1] == self.gameState[2][2] == shape or
           self.gameState[0][2] == self.gameState[1][1] == self.gameState[2][0] == shape):

            # if there is a winner, sets gameOver variable to True
            self.gameOver = True

        # returns True if there is a winner, and returns False if not
        return self.gameOver

    # method that restarts the game
    def restart(self):

        # self.gameOver = False
        # self.count = 0
        #
        # for list in self.canvases:
        #     for canv in list:
        #         canv.delete("all")

        pass

    # method that quits the current game and closes the widow
    def quit(self):

        pass

    # method that displays the game to be played
    def play(self):

        self.window.mainloop()


# main that runs and instantiates a tic-tac-toe game, then displays it to the screen
if __name__ == "__main__":
    myGame = TicTacToe()
    myGame.play()
