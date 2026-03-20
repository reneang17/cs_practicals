import numpy as np

class connect_4(object):
    def __init__(self):
        self.board = [[-1]* 6 for j in range(6)]

        self.super_board = [[0]* 6 for j in range(12)]
        self.scores = [0,0]
        self.directions = [ [0,1], [0,-1], [1,0], [1,1], [1,-1]]

    def is_board_full(self):
        for i in self.board:
            for j in i:
                if j == -1:
                    return False
        else: return True

    def print_board(self):
        print(np.array(self.board))

    def connect(self, label,pos1, pos2):

        pos1=pos1
        pos2=pos2
        for di in self.directions:
            counter = 1
            while 0<= pos1 + di[0] < 6 and 0<=pos2 + di[1] <6:
                #print(pos1 , di[0]  , pos2 , di[1])
                if self.board[pos1 + di[0]][pos2+ di[1]] == self.board[pos1][pos2] :
                    counter +=1
                    pos1+= di[0]
                    pos2+= di[1]
                else: break
            if counter ==4: self.scores[label]+=1

    def throw(self, label, position):
        i = 0
        while i<6:
            if self.board[5-i][position] == -1:
                self.board[5-i][position] = label
                self.connect(label,5-i,position)
                return 'next'
            i+=1
        else:
            if self.is_board_full(): return 'gameover'
            else:
                return('invalid')


    def play_turn(self, label):
        while True and not self.is_board_full():
            print('Player {} Which position would you like?'.format(label))
            position = input()
            result = self.throw(label, int(position))
            self.print_board()
            print(self.scores)
            if (result == 'next') or self.is_board_full():
                return  self.is_board_full()

    def play(self):
        self.print_board()
        while not self.is_board_full():
            self.play_turn(0)
            state = self.play_turn(1)
        self.who_won()

    def who_won(self):
        if self.score[1]> self.score[0]:
            print("player 1 won")
        elif self.score[1]< self.score[0]:
            print("player 0 won")
        else:
            print("draw")

game = connect_4()
game.play()
