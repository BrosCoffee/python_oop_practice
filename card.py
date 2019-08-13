import random

suit = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
val = {'Ace': 10, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
       '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

class Card:

    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def __str__(self):
        return "{} of {}".format(self.val, self.suit)

    # def __lt__(self, other):
    #
    # # return comparison
    # def __le__(self, other):
    #
    # # return comparison
    # def __eq__(self, other):
    #
    # # return comparison
    # def __ne__(self, other):
    #
    # # return comparison
    # def __gt__(self, other):
    #
    # # return comparison
    # def __ge__(self, other):
    #
    # # return comparison

    def value(self):
        return val.values('{}'.format(self.val))



class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def __str__(self):
        return "It is a deck of cards."

    def build(self):
        for s in suit:
            for n in val:
                self.cards.append(Card(s, n))



class Player:

    def __init__(self):
        pass

# card_1 = Card('Spades', 'Ace')
# card_1.show()

deck_1 = Deck()
card_1 = random.choice(deck_1.cards)
card_2 = random.choice(deck_1.cards)
card_3 = random.choice(deck_1.cards)

print(card_1)
print(card_2)
# print(card_1.value > card_2.value)

'''
when print() it will print 'X of X'
when compare two cards: card_1 == card_2: False, card_1 > card_2: True
'''