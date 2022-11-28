import os
import random
#os.system("clear")

class Cell():
    def __init__(self):
        self.visible = False
        self.flagged = False
        self.value = -1

    def __str__(self):
        if self.flagged:
            return  'f'
        elif self.visible:
            return self.value
        else:
            return  "H"

class Board():
    def __init__(self, side, n_mines):
        self.side = side
        self.n_mines= n_mines
        self.board = [[ Cell() for i in range(side)] for j in range(side)]

    def print_board(self):
        print('Minesweeper')
        for row in self.board:
            print(*row, sep='\t')

    def getneighboors(self, row, col):
        neighbors = []
        for i in [row-1,row,row+1]:
            for j in [col-1,col,col+1]:
                if (i,j) != (row,col) and (0 <= i < self.side) and (0 <= j < self.side):
                    neighbors.append((i,j))
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
            else:
                cell.value = 'X'
            count+=1

    def drawnumbers(self):
        for rowno, row in enumerate(self.board):
            for colno, cell in enumerate(row):
                neighbors = self.getneighboors(rowno, colno)
                if cell.value != 'X':
                    values = [self.board[i][j].value for (i,j) in neighbors]
                    cell.value = str(values.count('X'))


class Minesweeper():
    def __init__(self, gridsize, nmines):
        self.game = Board(gridsize, nmines)
        self.game.drawmines()
        self.game.drawnumbers()
        self.size = gridsize
        self.nmines = nmines

    def read_turn(self):
        self.game.print_board()
        while True:
            inp= input('Enter "nm" to reveal cell n of nmf to flag that cell:')
            if 2<=len(inp)<=3 and inp[0].isdigit() and inp[1].isdigit()  and (
                0 <= int(inp[0]) < self.size) and (0 <=  int(inp[1]) < self.size):
                cell = self.game.board[int(inp[0])][int(inp[1])]

                if cell.visible is False:
                    if len(inp) == 3 and inp[2]=='f':
                        return int(inp[0]), int(inp[1]), inp[2]
                    elif len(inp) == 2:
                        return int(inp[0]), int(inp[1])
            print('Invalid. Try again:')
        os.system("clear")

    def reveal_zeros(self, i, j):
        neighbors = self.game.getneighboors(i,j)
        for (r,s) in neighbors:
            cell = self.game.board[r][s]
            if int(cell.value)==0:
                if cell.visible is False:
                    cell.visible = True
                    self.reveal_zeros(r,s)

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
        while True:
            turn = self.read_turn()
            cell = self.game.board[turn[0]][turn[1]]

            if len(turn)==3:
                if not cell.flagged: cell.flagged = True
                else: cell.flagged = False


            elif len(turn) == 2:

                cell.visible = True
                if cell.value == 'X':
                    print("Game Over")
                    for rowno, row in enumerate(self.game.board):
                        for colno, cell in enumerate(row):
                            cell.visible = True
                    self.game.print_board()

                    break
                if int(cell.value) == 0: # Works thanks to int()
                    self.reveal_zeros(*turn)

            if self.check_state():
                self.game.print_board()
                print('You won!!!!')
                print('Wohoooooo!!!!')
                break
            os.system("clear")
if __name__ == "__main__":
    Minesweeper(5,1).play()

#class Game(self):

#class Minesweeper(self):
