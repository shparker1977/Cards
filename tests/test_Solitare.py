import unittest
from Solitaire import Solitaire

class TestSolitaire(unittest.TestCase):
    
    def test_new_game(self):
        test_game = Solitaire.Solitaire()
        self.assertEqual(len(test_game.deck), 24)
        self.assertEqual(len(test_game.row[0]), 1)
        self.assertEqual(len(test_game.row[1]), 2)
        self.assertEqual(len(test_game.row[2]), 3)
        self.assertEqual(len(test_game.row[3]), 4)
        self.assertEqual(len(test_game.row[4]), 5)
        self.assertEqual(len(test_game.row[5]),  6)
        self.assertEqual(len(test_game.row[6]), 7)
        self.assertEqual(len(test_game.end_stacks['H']), 0)
        self.assertEqual(len(test_game.end_stacks['D']), 0)
        self.assertEqual(len(test_game.end_stacks['S']), 0)
        self.assertEqual(len(test_game.end_stacks['C']), 0)


if __name__ == '__main__':
    unittest.main()
