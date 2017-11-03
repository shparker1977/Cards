import random
import unittest
import itertools
import sys
from PyQt4.QtGui import *

class Deck:

    def __init__(self):
        self.deck = []
        self.suits = ['D', 'H', 'S', 'C']
        self.numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                '10', 'J', 'Q', 'K']
        self.deck += [''.join(x) for x in itertools.product(self.suits, self.numbers)]

    def deal_card(self):
        """
        Returns a card from the deck.  Returns -1 if there are no cards left
        """
        if len(self.deck) > 0:
            if len(self.deck) == 1:
                dealt_card = self.deck.pop()
                return dealt_card
            else:
                dealt_card = self.deck.pop(random.randrange(0,len(self.deck) -1 , 1))
                return dealt_card
        else:
            return -1

    def return_card(self, card):
        if card not in self.deck:
            self.deck.append(card)
        else:
            return -1

    def __repr__(self):
        if len(self.deck):
            return self.deck
        else:
            return "No Cards left"




class TestDeckFunctions(unittest.TestCase):
    # create deck and check size and count of each card
    def test_cards(self):
        test_deck = Deck()
        self.assertEqual(len(test_deck.deck), 52)
        self.assertEqual(test_deck.deck.count('H4'), 1)

    # Create deck and deal 52 cards  try to deal another card and expect -1
    def test_deal(self):
        test_deck = Deck()
        for i in range(52):
            test_deck.deal_card()
        self.assertEqual(test_deck.deal_card(), -1)

    # Create deck and test deal and return
    def test_return(self):
        test_deck = Deck()
        dealt_cards = []
        for i in range(36):
            dealt_cards.append(test_deck.deal_card())
        card_to_return = dealt_cards.pop()
        self.assertNotIn(card_to_return, test_deck.deck)
        test_deck.return_card(card_to_return)
        self.assertIn(card_to_return, test_deck.deck)
        self.assertNotIn(card_to_return, dealt_cards)

    def test_image_creation(selfself):
        test_deck = Deck()
        test_card = test_deck.deal_card()
        app = QApplication(sys.argv)
        win = QWidget()
        l1 = QLabel()
        pixmap = QPixmap("images/" + test_card + ".png")
        l1.setPixmap(pixmap)
        vbox = QVBoxLayout()
        vbox.addWidget(l1)
        win.setLayout(vbox)
        win.setWindowTitle("Playing Card")
        win.show()
        sys.exit(app.exec_())




if __name__ == '__main__':
    unittest.main()
