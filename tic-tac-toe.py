from tkinter import *


class TicTacToe:

    window = None
    count = 0

    userTurn = True
    gameOver = False

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

    # constructor for tic-tac-toe class
    def __init__(self):

        # creates the window in which the game will be placed
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("552x652")
        self.window.resizable(False, False)

        # creates frame that will display gameplay options and current score
        frame = Frame(self.window, bg="green", width=552, height=100, highlightbackground="black", highlightthickness=4)
        frame.grid(row=0, column=0, columnspan=3)

        # creates the frames that will hold the gameplay area
        for i in range(1, 4):
            for j in range(3):
                self.frames[i-1][j] = self.create_frame(r=i, c=j)
                self.canvases[i-1][j] = self.create_canvas(self.frames[i - 1][j])
                self.canvases[i-1][j].bind("<Button-1>", lambda e, row=i-1, col=j: self.user_turn(row, col))

        # for f in self.frames:
        #     print(f)

        # for c in self.canvases:
        #     print(c)

    # method that creates frame and adds it to the gameplay area
    def create_frame(self, r, c):

        # creates Frame object, adds it to window, and returns it
        frame = Frame(self.window, bg="white", width=170, height=170, highlightbackground="black", highlightthickness=4)
        # frame.bind("4", self.user_turn)  # left click
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

        c.delete("all")

        if shape == "x":
            c.create_line(40, 40, 160, 160, fill="black", width=10)
            c.create_line(40, 160, 160, 40, fill="black", width=10)
        if shape == "o":
            c.create_oval(40, 40, 160, 160, fill="white", width=10)

    def play(self):

        self.window.mainloop()

    def user_turn(self, r, c):

        print(r, c)

        # self.gameOver = True


# main that runs and instantiates a tic-tac-toe game, then displays it to the screen
if __name__ == "__main__":
    myGame = TicTacToe()
    myGame.play()
