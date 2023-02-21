from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestDescribeCurrentLocation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_starting(self, mock_output):
        board = game.make_board(rows=2, columns=2)
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Name': 'Aditya'}
        game.describe_current_location(board, character)
        actual_output = mock_output.getvalue()
        expected_output = "Aditya is on the way to find Gul'dan, the Warlock at (0, 0).\n\n"
        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_ending(self, mock_output):
        board = game.make_board(rows=2, columns=2)
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Name': 'Aditya'}
        game.describe_current_location(board, character)
        actual_output = mock_output.getvalue()
        expected_output = "Aditya is at the foot of the Blackrock Mountain, the lair of Gul'dan at (1, 1).\n\n"
        self.assertEqual(actual_output, expected_output)

    @patch('random.choice', return_value='on the streets of Stormwind')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_somewhere_middle(self, mock_output, _):
        board = game.make_board(rows=2, columns=2)
        character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Name': 'Aditya'}
        game.describe_current_location(board, character)
        actual_output = mock_output.getvalue()
        expected_output = 'Aditya is on the streets of Stormwind at (1, 0).\n\n'
        self.assertEqual(actual_output, expected_output)
