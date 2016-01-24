import itertools
import random

class Deck:
    def __init__(self, num_decks=1):
        self.num_decks=num_decks
        self.suit = 'HDCS'
        self.rank = '23456789TJQKA'
        self.cards = [''.join(x) for x in itertools.product(self.rank, self.suit)] 

    def __len__(self):
        return len(self.cards)

    def display(self):
        print(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    # Deals the next card in the deck.  Returns 0 if deck is empty
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return 0

    def add_to_deck(self, card):
        # Add error checking (is card in deck, is card valid)
        self.cards.insert(0, card)
