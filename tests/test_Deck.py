import unittest
from Deck import Deck

class TestDeckMethods(unittest.TestCase):

    # Test that a deck has 52 cards
    def test_deck(self):
        self.test_deck = Deck.Deck()
        self.assertEqual(len(self.test_deck.cards), 52)

    # Test shuffle cards
    def test_shuffle(self):
        self.test_deck = Deck.Deck()
        self.assertEqual(self.test_deck.cards, ['2H', '2D', '2C', '2S', '3H', '3D', '3C', '3S', '4H', '4D', '4C', '4S', '5H', '5D', '5C', '5S', '6H', '6D', '6C', '6S', '7H', '7D', '7C', '7S', '8H', '8D', '8C', '8S', '9H', '9D', '9C', '9S', 'TH', 'TD', 'TC', 'TS', 'JH', 'JD', 'JC', 'JS', 'QH', 'QD', 'QC', 'QS', 'KH', 'KD', 'KC', 'KS', 'AH', 'AD', 'AC', 'AS'])
        self.test_deck.shuffle()
        self.assertNotEqual(self.test_deck.cards, ['2H', '2D', '2C', '2S', '3H', '3D', '3C', '3S', '4H', '4D', '4C', '4S', '5H', '5D', '5C', '5S', '6H', '6D', '6C', '6S', '7H', '7D', '7C', '7S', '8H', '8D', '8C', '8S', '9H', '9D', '9C', '9S', 'TH', 'TD', 'TC', 'TS', 'JH', 'JD', 'JC', 'JS', 'QH', 'QD', 'QC', 'QS', 'KH', 'KD', 'KC', 'KS', 'AH', 'AD', 'AC', 'AS'])

    # Test deal cards until deck is empty
    def test_deal(self):
        self.test_deck = Deck.Deck()
        sample_deck = self.test_deck.cards[:]
        first_deal = self.test_deck.deal()
        self.assertIn(first_deal, sample_deck)
        while len(self.test_deck.cards) > 0:
            dealt_card = self.test_deck.deal()
        self.assertEqual(self.test_deck.deal(), 0)   

    # Test return card to deck
    def test_return_card(self):
        self.test_deck = Deck.Deck()
        first_card = self.test_deck.deal()
        self.assertEqual(len(self.test_deck.cards), 51)
        self.test_deck.add_to_deck(first_card)
        self.assertEqual(len(self.test_deck.cards), 52)

if __name__ == '__main__':
    unittest.main() 
