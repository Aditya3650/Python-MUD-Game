from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestInvalidMove(TestCase):

    @patch('random.choice', return_value='Oh no, there is a wall there.')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_move_reason_one(self, mock_output, _):
        game.invalid_move()
        actual_print = mock_output.getvalue()
        expected_print = "Oh no, there is a wall there. Move in some other direction.\n"
        self.assertEqual(actual_print, expected_print)

    @patch('random.choice', return_value='You stand at the edge of a cliff.')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_move_reason_two(self, mock_output, _):
        game.invalid_move()
        actual_print = mock_output.getvalue()
        expected_print = "You stand at the edge of a cliff. Move in some other direction.\n"
        self.assertEqual(actual_print, expected_print)

    @patch('random.choice', return_value='You are at a dead-end.')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_move_reason_three(self, mock_output, _):
        game.invalid_move()
        actual_print = mock_output.getvalue()
        expected_print = "You are at a dead-end. Move in some other direction.\n"
        self.assertEqual(actual_print, expected_print)

    @patch('random.choice', return_value='You are in front of a deadly swamp.')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_move_reason_four(self, mock_output, _):
        game.invalid_move()
        actual_print = mock_output.getvalue()
        expected_print = "You are in front of a deadly swamp. Move in some other direction.\n"
        self.assertEqual(actual_print, expected_print)
