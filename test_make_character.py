from unittest import TestCase
import game


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        actual_dictionary = game.make_character()
        expected_dictionary = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
        self.assertEqual(expected_dictionary, actual_dictionary)
