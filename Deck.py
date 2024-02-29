import random
from Card import *

"""
Deck class

This class represents a deck of playing cards. It has a list of cards and a method to draw a card from the deck.
"""
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for _ in range(4) for rank in Card.ranks for suit in Card.suits]
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()