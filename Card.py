"""
Card class

This class represents a playing card. It has a rank and a suit.
"""
class Card:

    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"