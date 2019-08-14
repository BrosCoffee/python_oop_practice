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

    @property
    def value(self):
        return val[self.val]

class Deck:

    def __init__(self, deck_num):
        self.deck_num = deck_num
        self.cards = []
        while self.deck_num > 0:
            self.build()
            self.deck_num -= 1

    def __str__(self):
        return "It is a deck of cards."

    def build(self):
        for s in suit:
            for n in val:
                self.cards.append(Card(s, n))

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return "Hi, my name is {}.".format(self.name)

    def draw_card(self):
        self.hand.append(random.choice(Deck(3).cards)) # Using 3 decks of cards.

# deck_1 = Deck(3) # Using 3 decks of cards # See line 46
# for i in deck_1.cards:
#     print(i)
# print(len(deck_1.cards)) # How many cards in the big deck


# class Game:
#     player_list = []
#     def __init__(self, *args):
#         for i in args:
#             self.player_list.append(Player(i))
#     def __str__(self):
#         for i in self.player_list:
#             print(i)
#
#
# game_1 = Game('Ray', 'Mei')
# print(game_1)


player_1 = Player('Ray')
print(player_1)

player_1.draw_card()
player_1.draw_card()
player_1.draw_card()

total = 0
for card in player_1.hand:
    print(card)
    total += card.value
print("Total points of the hand is: {}".format(total))


# card_1 = random.choice(deck_1.cards)
# card_2 = random.choice(deck_1.cards)
# card_3 = random.choice(deck_1.cards)
#
# print("Card_1:", card_1)
# print("Card_2:", card_2)
# print("Card_3:", card_3)
# print("Card_1's value:", card_1.value)
# print("Is card_2 > card_3:", card_2.value > card_3.value)
# print("card_1 + card_2 + card_3:", card_1.value + card_2.value + card_3.value)
# '''
# 1. when print() it will print 'X of X --> line 13, 14
# 2. when compare two cards: card_1.value == card_2.value >>> False,
#    card_1.value > card_2.value >>> True --> line 16- 18
# '''