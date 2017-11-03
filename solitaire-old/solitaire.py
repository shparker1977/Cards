import deck
import unittest


class Solitaire:

    def __init__(self):

        self.game_deck = deck.Deck()
        self.suit_stacks = [[],[],[],[]]
        self.game_stacks = [[],[],[],[],[],[],[]]

        faceup_deal = 0
        for x in range(7):
            for stack in range(7):
                if stack > faceup_deal:
                    # Deal a card face down
                    self.game_stacks[stack].append([self.game_deck.deal_card(), 'DOWN'])
                elif stack == faceup_deal:
                    # Deal a card face up
                    self.game_stacks[stack].append([self.game_deck.deal_card(), 'UP'])
                else:
                    pass
            faceup_deal += 1



class TestSolitaireFunctions(unittest.TestCase):
    def test_deal(self):
        test_solitaire = Solitaire()
        for stack in test_solitaire.game_stacks:
            self.assertEqual(stack[-1][1], 'UP')






if __name__ == "__main__":
    unittest.main()
