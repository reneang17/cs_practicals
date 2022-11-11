
#based on from https://civilengineering-softstudies.com/1525-class-based-tic-tac-toe-game-only-in-77-lines-of-python-code.html

import os
os.system("clear")

class Board():
    def __init__(self):
       self.cells = ["", "", "", "", "", "", "", "", "", ""]

    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print('__________')
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print('__________')
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == "":
            self.cells[cell_no] = player


    def is_winner(self, player):

        # diagonals
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
                return True
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
                return True

        for i in [1,4,7]:
            if self.cells[i] == player and self.cells[i+1] == player and self.cells[i+2] == player:
                return True
        for i in [1,2,3]:
            if self.cells[i] == player and self.cells[i+3] == player and self.cells[i+6] == player:
                return True

    def reset(self):
        self.cells = ["", "", "", "", "", "", "", "", "", ""]

    def read_turn(self, player):
        x_choice = input("\n {}) Please choose 1-9.>".format(player))
        while x_choice not in ['1','2','3','4','5','6','7','8','9'] or (x_choice in ['1','2','3','4','5','6','7','8','9']
        and self.cells[int(x_choice)] != ''):
            self.refresh_screen()
            x_choice = input("\n {}) Invalid cell, please choose anorther 1-9.>".format(player))


        return int(x_choice)

    def refresh_screen(self):
        #clear the screen
        os.system("clear")
        print("Welcome to Tic-Tac-Toe \n")
        self.display()

    def one_turn(self, player):
        self.refresh_screen()
        x_choice = self.read_turn(player)
        self.update_cell(x_choice, player)

    def play(self):
        while True:
            self.one_turn('X')
            if self.is_winner('X'):
                print("\n X Wins! \n")
                play_again = input("Would you like to play again? (Y/N) > ").upper()
                if play_again == "Y":
                    self.reset()
                    continue
                else:
                    break
            self.one_turn('O')
            if self.is_winner('O'):
                print("\n X Wins! \n")
                play_again = input("Would you like to play again? (Y/N) > ").upper()
                if play_again == "Y":
                    self.reset()
                    continue
                else:
                    break
if __name__ == '__main__':
    board = Board()
    board.play()
