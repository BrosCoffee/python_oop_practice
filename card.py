import random

suit = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
num = {'Ace': 10, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
       '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

class Deck:

    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in suit:
            for n in num:
                self.cards.append('{} of {}'.format(n, s))

deck_1 = Deck()
card_1 = random.choice(deck_1.cards)
card_2 = random.choice(deck_1.cards)
card_3 = random.choice(deck_1.cards)

print(card_1)
print(card_2)
print(card_3)

'''
when print() it will print 'X of X'
when compare two cards: card_1 == card_2: False, card_1 > card_2: True
'''