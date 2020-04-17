import random
class Card:
    cards =[]
    suits = ['Hearts','Diamonds','Clubs','Spades']
    values = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    for suit in suits:
        for value in values:
            cards.append([suit, value])
class Deck:
    def __init__(self):
        self.card = Card.cards.copy()
    def deal(self):
        if len(self.card) != 0:
            card = random.choice(self.card)
            print(card)
            (self.card).remove(card)
            
        else:
            print('all cards dealt')

    def shuffle(self):
        if len(self.card) == 52:
            random.shuffle(self.card)
        else:
            print('cards less than 52')
    
    def cards_left(self):
        print(len(self.card))

card_1 = Deck()
card_1.shuffle()
card_1.deal()
card_1.cards_left()
