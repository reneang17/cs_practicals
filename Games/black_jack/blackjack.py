import random
class BJ(object):
    def __init__(self, n_decks = 4):
        numbs = list(range(1,14))
        self.deck  = [] 
        for i in range(n_decks):
            self.deck+= numbs
        

        self.vals = {i: (i if i<=11 else 10) for i in  range(2,14) }
        self.val1 = self.vals
        self.val2 = self.vals
        self.val1[1] = 1
        self.val2[1] = 11

        self.dealer = []
        self.player = []
        
    def give_card(self,person):
        card =self.deck.pop()
        person +=[card]
        
    def scores(self,deck):
        t1 = sum([self.val1[i] for i in deck])
        t2 = sum([self.val2[i] for i in deck])
        if t1 > 21 and t2 > 21:
            return min(t1,t2)
        else: return max(t1,t2)
        

        return (t1,t2)
    
    def start_game(self):
        self.give_card(game.player)
        self.give_card(game.player)
        self.give_card(game.dealer)
        self.give_card(game.dealer)
        
    def ask_player(self):
        print('Stay or not')
    
    def check(self,person):
        if self.scores(person) > 21:
            print('{} lost!'.format(person))
            return True
        elif self.scores(person) >= 21:
            print('Black Jack!')
            return True
        return False
    
    def play_game(self):
        print('Dealer shuffles')
        random.shuffle(self.deck)
        print('Dealer gives cards')
        self.give_card(self.player)
        self.give_card(self.dealer)
        self.give_card(self.player)
        self.give_card(self.dealer)
        
        print('You checked your cards !')
        print('Card hidden {} and card up {}'.format(self.player[0], self.player[-1]) )
        
        if self.check(self.player):
            return
        
        while True:
            print('Do you want one more card (y/n)?')
            decision = input()
            if decision == 'n':
                break
            elif decision == 'y':
                self.give_card(self.player)
                print('Your deck is now {}'.format(self.player))
            if self.check(self.player):
                return
            
        print('House plays')
        while sum(self.dealer) <17:
            self.give_card(self.dealer)
            
        self.check(self.dealer)
        print(self.dealer)
        
        if sum(self.player)> sum(self.dealer):
            print('you win')
        elif sum(self.player)< sum(self.dealer):
            print('dealer wins')
        else:
            print('draw')
            
            
            
        
        
game = BJ()
game.play_game()    