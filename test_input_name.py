from unittest import TestCase
from unittest.mock import patch
import game


class TestInputName(TestCase):

    @patch('builtins.input', side_effect=['Aditya'])
    def test_input_name(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
        game.input_name(character)
        actual_value = character
        expected_value = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Name': 'Aditya'}
        self.assertEqual(actual_value, expected_value)
