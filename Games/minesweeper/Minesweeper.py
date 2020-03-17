"""A command line version of Minesweeper"""
import random
import re
import time
from string import ascii_lowercase

class Cell():
    def __init__(self):
        self.visible = False
        self.flagged = False
        self.value = -1

    def __str__(self):
        if self.flagged:
            return  'f'
        elif self.visible:
            return  self.value
        else:
            return  "H"


class Board():
    def __init__(self, side, n_mines):
        self.side = side
        self.n_mines= n_mines
        self.board = [[ Cell() for i in range(side)] for j in range(side)]
        self.start = self.getrandomcell()

    def print_board(self):
        for row in self.board:
            print(*row, sep='\t')

    def getneighbors(self, row, col ):
        side = self.side
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif -1 < (row + i) < side and -1 < (col + j) < side:
                    neighbors.append((row + i, col + j))
        return neighbors

    def getrandomcell(self):
        a = random.randint(0, self.side - 1)
        b = random.randint(0, self.side - 1)
        return (a, b)

    def drawmines(self):
        mines = []
        count = 0
        while count < self.n_mines:
            coords = self.getrandomcell()
            cell = self.board[coords[0]][coords[1]]
            if cell.value == 'X':
                continue
            cell.value = 'X'
            count+=1

    def drawnumbers(self):
        for rowno, row in enumerate(self.board):
            for colno, cell in enumerate(row):
                if cell.value != 'X':
                    values = [self.board[r][c].value for r, c in self.getneighbors(rowno, colno)]
                    (self.board[rowno][colno]).value = str(values.count('X'))

class Minesweeper():
    def __init__(self, gridsize, nmines):
        self.gameover= False
        self.lost = False
        self.game = Board(gridsize, nmines)
        self.game.drawmines()
        self.game.drawnumbers()
        self.size = gridsize
        self.nmines = nmines

    def read_turn(self):
        size = self.size
        get_turn = True
        self.game.print_board()
        while get_turn:
            inp= input('Enter "nm" to reveal cell n of nmf to flag that cell:')
            if 1<len(inp)<=3 and inp[0].isdigit() and inp[1].isdigit()  and (
                -1 < int(inp[0]) < size) and (-1 < int(inp[1]) < size):
                cell = self.game.board[int(inp[0])][int(inp[1])]

                if not cell.visible:
                    if len(inp) == 3 and inp[2]=='f':
                        return int(inp[0]), int(inp[1]), inp[2]
                    elif len(inp) == 2:
                        return int(inp[0]), int(inp[1])
            print('Invalid. Try again:')

    def reveal_zeros(self, i, j):
        nei = self.game.getneighbors(i,j)
        for i,j in nei:
            cell = self.game.board[i][j]
            if int(cell.value)==0:
                if not cell.visible:
                    cell.visible = True
                    self.reveal_zeros(i,j)

    def check_state(self):
        st = 0
        for i in range(self.size):
            for j in range(self.size):
                cell = self.game.board[i][j]
                if cell.value != 'X' and cell.visible:
                    st +=1
        if st== (self.size**2 - self.nmines):
            return True


    def play(self):
        while not self.gameover:
            turn = self.read_turn()
            cell = self.game.board[turn[0]][turn[1]]

            if len(turn)==3:
                if not cell.flagged: cell.flagged = True
                else: cell.flagged = False


            elif len(turn) == 2:

                cell.visible = True
                if cell.value == 'X':
                    self.gameover = True
                    self.game.print_board()
                    print("Game Over")
                    break
                if int(cell.value) == 0: # Works thanks to int()
                    self.reveal_zeros(*turn)

            if self.check_state():
                print('You won!!!!')
                print('Wohoooooo!!!!')
                break
if __name__ == "__main__":
    Minesweeper(5,10).play()
