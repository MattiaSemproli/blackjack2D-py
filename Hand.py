from Card import *
from typing import List

"""
Hand class

The Hand class is used to represent a player's hand in the game of Blackjack. It has two methods:
- add_card: adds a card to the hand
- get_value: calculates the value of the hand based on the rules of Blackjack
"""
class Hand:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card):
        self.cards.append(card)

    def get_dealer_value_with_hidden_card(self):
        value = 0
        for i, card in enumerate(self.cards):
            if i == 0:
                continue
            if card.rank in ['J', 'Q', 'K']:
                value += 10
            elif card.rank == 'A':
                value += 11
            else:
                value += int(card.rank)
        return value

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.rank in ['J', 'Q', 'K']:
                value += 10
            elif card.rank == 'A':
                num_aces += 1
                value += 11
            else:
                value += int(card.rank)

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value