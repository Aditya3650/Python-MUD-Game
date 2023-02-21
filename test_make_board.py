from unittest import TestCase
from unittest.mock import patch
import game


class TestMakeBoard(TestCase):

    @patch('random.choice', return_value='the streets of Stormwind')
    def test_make_board_2x2(self, _):
        actual_dictionary = game.make_board(rows=3, columns=3)
        expected_dictionary = {(0, 0): "on the way to find Gul'dan, the Warlock", (0, 1): 'the streets of Stormwind',
                               (0, 2): 'the streets of Stormwind', (1, 0): 'the streets of Stormwind',
                               (1, 1): 'the streets of Stormwind', (1, 2): 'the streets of Stormwind',
                               (2, 0): 'the streets of Stormwind', (2, 1): 'the streets of Stormwind',
                               (2, 2): "at the foot of the Blackrock Mountain, the lair of Gul'dan"}
        self.assertEqual(expected_dictionary, actual_dictionary)

    @patch('random.choice', return_value='over the ashes of Outland')
    def test_make_board_3x3(self, _):
        actual_dictionary = game.make_board(rows=2, columns=2)
        expected_dictionary = {(0, 0): "on the way to find Gul'dan, the Warlock", (0, 1): 'over the ashes of Outland',
                               (1, 0): 'over the ashes of Outland',
                               (1, 1): "at the foot of the Blackrock Mountain, the lair of Gul'dan"}
        self.assertEqual(expected_dictionary, actual_dictionary)

    @patch('random.choice', return_value='outside the Scholomance Academy')
    def test_make_board_2x3(self, _):
        actual_dictionary = game.make_board(rows=2, columns=3)
        expected_dictionary = {(0, 0): "on the way to find Gul'dan, the Warlock",
                               (0, 1): 'outside the Scholomance Academy', (0, 2): 'outside the Scholomance Academy',
                               (1, 0): 'outside the Scholomance Academy', (1, 1): 'outside the Scholomance Academy',
                               (1, 2): "at the foot of the Blackrock Mountain, the lair of Gul'dan"}
        self.assertEqual(expected_dictionary, actual_dictionary)

    @patch('random.choice', return_value='lost in the catacombs of Uldum')
    def test_make_board_3x2(self, _):
        actual_dictionary = game.make_board(rows=3, columns=2)
        expected_dictionary = {(0, 0): "on the way to find Gul'dan, the Warlock",
                               (0, 1): 'lost in the catacombs of Uldum', (1, 0): 'lost in the catacombs of Uldum',
                               (1, 1): 'lost in the catacombs of Uldum', (2, 0): 'lost in the catacombs of Uldum',
                               (2, 1): "at the foot of the Blackrock Mountain, the lair of Gul'dan"}
        self.assertEqual(expected_dictionary, actual_dictionary)
