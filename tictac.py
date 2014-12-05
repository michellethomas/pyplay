#-------------------------------------------------------------------------------
# Name:        tictac
# Purpose:     Implement a game of Tic Tac Toe
#
# Author:
#-------------------------------------------------------------------------------

import math
import tkinter
import random

class Game(object):
    """
    Enter the class docstring here
    """

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent
        # Add your instance variables  if needed here
        # Examples are the color assignments or things that don't need to
        # change after restarts.
        self.tile_size = 50
        self.game_play = {}
        self.initialize_game()

    def initialize_game(self):
        # These are the initializations that need to happen
        # at the beginning and after restarts
        self.frame=tkinter.Frame(self.parent)
        self.frame.grid()
        restart_button = tkinter.Button(self.frame, text = 'Restart',
                                                width = 20,
                                                command = self.restart)
        restart_button.grid()
        self.canvas = tkinter.Canvas(self.frame,
                                     width= self.tile_size * 3,
                                     height= self.tile_size* 3)
        self.canvas.grid()
        for row in range(3):
            for column in range(3):
                self.game_play[(self.tile_size*column, self.tile_size*row)] = 'blank'
                self.canvas.create_rectangle(self.tile_size*column,
                                            self.tile_size * row,
                                            self.tile_size * (column + 1),
                                            self.tile_size * (row + 1),
                                            fill = 'white')
        self.canvas.bind("<Button-1>", self.play)

    def restart(self):
        """ Reinitialize the game and board after restart button is pressed """
        self.frame.destroy()
        self.initialize_game()

    def computer_play(self):
        computer_play_x = random.randint(0,2)*self.tile_size
        computer_play_y = random.randint(0,2)*self.tile_size
        if self.game_play[(computer_play_x, computer_play_y)] == 'blank':
            self.canvas.create_rectangle(computer_play_x,
                                        computer_play_y,
                                        computer_play_x+self.tile_size,
                                        computer_play_y+self.tile_size,
                                        fill = 'blue')
            self.game_play[(computer_play_x, computer_play_y)] = 'computer'
        else:
#TODO: check if there is a square left to play (otherwise max recursion)
            self.computer_play()


    def play(self, event):
        """  Enter method docstring here """
        # This method is invoked when the user clicks on a square.
        # If the square is already taken, do nothing.
        round_x = int(self.tile_size * math.floor(float(event.x)/self.tile_size))
        round_y = int(self.tile_size * math.floor(float(event.y)/self.tile_size))
        if self.game_play[(round_x, round_y)] == 'blank':
            self.canvas.create_rectangle(round_x,
                                        round_y,
                                        round_x+self.tile_size,
                                        round_y+self.tile_size,
                                        fill = 'purple')
            self.game_play[(round_x, round_y)] = 'user'
            self.computer_play()
            print(self.game_play)


    def check_game(self):
        """  Enter method docstring here """
        # Check if the game is won or lost
        user_total = 0
        computer_total = 0
        for pair, result in self.game_play.iteritems():



def main():
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a Game object
    game = Game(root)
    # Enter the main event loop
    root.mainloop()

if __name__ == '__main__':
    main()
