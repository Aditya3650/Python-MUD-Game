from unittest import TestCase
import game


class TestGuessingGameRunner(TestCase):

    def test_guessing_game_runner_false(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Name': 'Aditya'}
        actual_return = game.guessing_game_runner(character)
        expected_return = False
        self.assertEqual(actual_return, expected_return)

    def test_guessing_game_runner_true(self):
        character = {'X-coordinate': 4, 'Y-coordinate': 4, 'Name': 'Aditya'}
        actual_return = game.guessing_game_runner(character)
        expected_return = True
        self.assertEqual(actual_return, expected_return)
