from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestCheckForFoes(TestCase):

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_foes_True(self, mock_output, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0}
        actual_return = game.check_for_foes(character_info)
        expected_return = True
        actual_print = mock_output.getvalue()
        expected_print = """\nAlas, you have encountered a foe in the wild.
You do not wish to harm any being other than Gul'dan, but you have no choice now.\n"""
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(actual_print, expected_print)

    @patch('random.randint', return_value=2)
    def test_check_for_foes_False(self, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0}
        actual_return = game.check_for_foes(character_info)
        expected_return = False
        self.assertEqual(actual_return, expected_return)

    @patch('random.randint', return_value=1)
    def test_check_for_foes_character_on_coordinates_list(self, _):
        character_info = {'X-coordinate': 4, 'Y-coordinate': 4}
        actual_return = game.check_for_foes(character_info)
        expected_return = False
        self.assertEqual(actual_return, expected_return)
