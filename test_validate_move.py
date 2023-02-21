from unittest import TestCase
import game


class TestValidateMove(TestCase):
    def test_validate_move_invalid(self):
        board = game.make_board(3, 3)
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 2}
        direction = '3'
        actual_value = game.validate_move(board, character, direction)
        expected_value = False
        self.assertEqual(actual_value, expected_value)

    def test_validate_move_valid(self):
        board = game.make_board(3, 3)
        character = {'X-coordinate': 1, 'Y-coordinate': 2, 'HP': 2}
        direction = '3'
        actual_value = game.validate_move(board, character, direction)
        expected_value = True
        self.assertEqual(actual_value, expected_value)
