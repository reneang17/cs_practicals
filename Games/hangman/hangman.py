import os
import random

class Display():

    def __init__(self, word):

        self.man =  "  O\n /|\\\n  /\\"
        self.parts = ["O", "|" , '/',"\\", "/" , "\\"]
        self.mid = len("  O\n /|\\")
        self.word_ = word
        self.switch = ['off'] * len(word)

    def turn_on(self, index):
        self.switch[index] = 'on'

    def pop(self):
        self.man = self.man.replace(self.parts.pop(), " ",1)


    def pop(self):
        self.man = self.man.replace(self.parts.pop(), " ",1)

    def __repr__(self):



        s= self.man[0:self.mid]
        s+=('\t'*3)

        for idx, i in enumerate(self.switch):
            if i == 'on':
                s+=' ' + self.word_[idx] + ' '
            else:
                s+= ' _ '
        s+= self.man[self.mid:]
        return s

class Hangman():

    def __init__(self):

        path = os.path.join('./','words.text')
        with open(path, 'r') as f:
            words = f.read().split('\n')

        self.word = random.choice(words)
        self.le = len(self.word)
        while len(self.word)<7:
            self.word = random.choice(words)
        self.word= self.word.lower()
        self.le_word = len(self.word)
        self.display = Display(self.word)
        self.n_parts = len(self.display.parts)

    def read_input(self):
        print(self.display)
        letter = input(f"Enter a letter: ")
        return letter

    def get_indices(self, letter):
        indices = []
        for idx, c in enumerate(self.word):
            if letter == c:
                indices.append(idx)
        return indices

    def play(self):
        cache = []
        while True:
            letter = self.read_input()
            indices = self.get_indices(letter)
            if indices:
                [self.display.turn_on(i) for i in indices]
                if letter not in cache:
                    self.le-=len(indices)
            elif letter not in cache:
                self.n_parts-=1
                self.display.pop()

            if self.n_parts==0:
                print(self.display)
                print("Game Over")
                print(f'The word was {self.word}')
                break
            elif self.le ==0 :
                print(self.display)
                print("You made it!!!!")
                break
            cache.append(letter)

if __name__ == '__main__':
    hangman = Hangman()
    hangman.play()
