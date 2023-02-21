from unittest import TestCase
import game
from unittest.mock import patch
import io


class TestIsAlive(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_alive_print_statement(self, mock_output):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Health': 500}
        actual_return = game.is_alive(character)
        expected_return = True
        actual_print = mock_output.getvalue()
        expected_print = "Your current Health is 500.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_return, expected_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_not_alive_print_statement(self, mock_output):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Health': 0}
        actual_return = game.is_alive(character)
        expected_return = False
        actual_print = mock_output.getvalue()
        expected_print = "You have succumbed to your injuries. Your skills could not match your resolve.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_return, expected_return)
