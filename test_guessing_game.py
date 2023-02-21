from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestGuessingGame(TestCase):

    @patch('builtins.input', side_effect=['1', 'end'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_correct_answer_one_game(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 500, 'Max_Health': 1000, 'Current-XP': 100}
        game.guessing_game(character)
        actual_change = character
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 700, 'Max_Health': 1000, 'Current-XP': 400}
        actual_print = mock_output.getvalue()
        expected_print = """You come across the Bloodmage Thalnos. 
In order to commence on your quest, you have to play the Trade of Souls.
Answer correctly and gain the elixir of life,
Answer wrong and pay with your soul.\n
The Bloodmage flips The Three Headed Dice of Hrakkar.""" \
            "\n\nYou're right! The Bloodmage blesses your soul with the gift of life. " \
                         "You gain 200 Health." \
                         "\nYour current health is 700.\n" \
                         """\nDo you still wish to play the Soul Trade with Thalnos?
    Press 5 to Continue Playing
    Press any other button to Flee""" \
                         "\nYou decide to stop playing the Trade of Souls.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['3', 'end'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_wrong_answer_one_game(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 500, 'Max_Health': 1000, 'Current-XP': 100}
        game.guessing_game(character)
        actual_change = character
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 1, 'Health': 400, 'Max_Health': 1000, 'Current-XP': 400}
        actual_print = mock_output.getvalue()
        expected_print = """You come across the Bloodmage Thalnos. 
In order to commence on your quest, you have to play the Trade of Souls.
Answer correctly and gain the elixir of life,
Answer wrong and pay with your soul.\n
The Bloodmage flips The Three Headed Dice of Hrakkar.""" \
                         """\n\nWrong option! The correct side was option 1.
You feel your soul getting tapped and vitality being removed.
You lose 100 Health.""" \
                         "\nYour current health is 400.\n" \
                         """\nDo you still wish to play the Soul Trade with Thalnos?
    Press 5 to Continue Playing
    Press any other button to Flee""" \
                         "\nYou decide to stop playing the Trade of Souls.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)
