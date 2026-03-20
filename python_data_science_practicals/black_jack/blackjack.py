import random
class BJ(object):
    def __init__(self, n_decks = 4):
        numbs = list(range(1,11))
        numbs.append('J')
        numbs.append('Q')
        numbs.append('K')
        self.deck  = []
        for i in range(n_decks):
            self.deck+= numbs
        self.vals = {i: (i if i<11 else 10) for i in  range(2,14) }
        self.vals[1] = 1
        self.vals['J'] = 10
        self.vals['Q'] = 10
        self.vals['K'] = 10
        self.dealer = []
        self.player = []

    def give_card(self,person):
        card =self.deck.pop()
        person +=[card]

    def scores(self, deck):
        _deck = deck.copy()
        scores = [sum([self.vals[i] for i in _deck])]
        while 1 in _deck:
            _deck.remove(1)
            _deck.append(2)
            _deck.append(9)
            scores.append(sum([self.vals[i] for i in _deck]))
        under_or_equal  = -1
        above = -1

        for i in scores:
            if i <= 21:
                under_or_equal = i
        for i in scores:
            if i > 21:
                above = i
                break
        if under_or_equal == -1 and above != -1:
            return above
        elif under_or_equal != -1:
            return under_or_equal
        else:
            print("Error tracking the score of {}".fortmat(deck))


    def start_game(self):
        self.give_card(game.player)
        self.give_card(game.player)
        self.give_card(game.dealer)
        self.give_card(game.dealer)

    def ask_player(self):
        print('Stay or not')

    def play_game(self):
        print('Dealer shuffles')
        random.shuffle(self.deck)
        print('Dealer gives cards')
        self.give_card(self.player)
        self.give_card(self.dealer)
        self.give_card(self.player)
        self.give_card(self.dealer)
        print('Dealer initial cards:')
        print('One hidden, the card up is {}'.format(self.dealer[-1]) )
        print('Your cards are:')
        print('Card hidden {} and card up {}'.format(self.player[0], self.player[-1]) )


        while True:
            print('Do you want another card (y/n)?')
            decision = input()
            if decision == 'n':
                break
            elif decision == 'y':
                self.give_card(self.player)
                print('Your deck is now {}'.format(self.player))
            if self.scores(self.player)>=21:
                break

        if self.scores(self.player) == 21:
            print("Black Jack! You win!")
            return

        elif self.scores(self.player) > 21:
            print('House wins')
            return

        print('Now house plays')
        print("House deck is: {}".format(self.dealer))
        while self.scores(self.dealer) <17 and self.scores(self.dealer) != 21:
            self.give_card(self.dealer)
            print("House deck is: {}".format(self.dealer))

        if self.scores(self.dealer) == 21:
            print("Black Jack! House wins!")
        elif self.scores(self.dealer) > 21:
            print('You win')
        elif self.scores(self.dealer) < self.scores(self.player) and self.scores(self.player) < 21:
            print('You win')
        elif self.scores(self.dealer) == self.scores(self.player) and self.scores(self.player) < 21:
            print('Draw')
        else:
            print('House wins!')

        print('The final cards were:')
        print('Player: {}'.format(self.player))
        print('Dealer: {}'.format(self.dealer))


if __name__ == '__main__':
    game = BJ()
    game.play_game()
