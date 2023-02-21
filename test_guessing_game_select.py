from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestGuessingGameSelect(TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_select_correct_answer(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 500, 'Max_Health': 1000}
        game.guessing_game_select(character)
        actual_change = character
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 700, 'Max_Health': 1000}
        actual_print = mock_output.getvalue()
        expected_print = "\nYou're right! The Bloodmage blesses your soul with the gift of life. " \
                         "You gain 200 Health." \
                         "\nYour current health is 700.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['1'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_select_correct_answer_health_already_max(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 1000, 'Max_Health': 1000}
        game.guessing_game_select(character)
        actual_change = character
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 1000, 'Max_Health': 1000}
        actual_print = mock_output.getvalue()
        expected_print = "\nYou're right! The Bloodmage blesses your soul with the gift of life. " \
                         "You gain 200 Health." \
                         "\nYour current health is 1000.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_select_wrong_answer(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 500, 'Max_Health': 1000}
        game.guessing_game_select(character)
        actual_change = character
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 400, 'Max_Health': 1000}
        actual_print = mock_output.getvalue()
        expected_print = """\nWrong option! The correct side was option 1.
You feel your soul getting tapped and vitality being removed.
You lose 100 Health.""" \
                         "\nYour current health is 400.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_select_wrong_answer_health_below_zero(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 50, 'Max_Health': 1000}
        game.guessing_game_select(character)
        actual_change = character
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': -50, 'Max_Health': 1000}
        actual_print = mock_output.getvalue()
        expected_print = """\nWrong option! The correct side was option 1.
You feel your soul getting tapped and vitality being removed.
You lose 100 Health.""" \
                         "\nYour current health is -50.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['bruh'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_select_invalid_answer(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 500, 'Max_Health': 1000}
        game.guessing_game_select(character)
        actual_change = character
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 400, 'Max_Health': 1000}
        actual_print = mock_output.getvalue()
        expected_print = """\nWrong option! The correct side was option 1.
You feel your soul getting tapped and vitality being removed.
You lose 100 Health.""" \
                         "\nYour current health is 400.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)
