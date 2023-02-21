import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestFightOrFlee(TestCase):

    @patch('builtins.input', side_effect=['5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_flee_fight(self, mock_output, _):
        actual_return = game.fight_or_flee()
        expected_return = True
        actual_print = mock_output.getvalue()
        expected_print = """\nDo you wish to fight the foe?
    Press 5 to Fight
    Press 6 to Flee
You decide to fight the foe.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_return, expected_return)

    @patch('builtins.input', side_effect=['6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_flee_flee(self, mock_output, _):
        actual_return = game.fight_or_flee()
        expected_return = False
        actual_print = mock_output.getvalue()
        expected_print = """\nDo you wish to fight the foe?
    Press 5 to Fight
    Press 6 to Flee
You decide to flee from the foe.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_return, expected_return)

    @patch('builtins.input', side_effect=['1', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_flee_invalid_int(self, mock_output, _):
        actual_return = game.fight_or_flee()
        expected_return = False
        actual_print = mock_output.getvalue()
        expected_print = """\nDo you wish to fight the foe?
    Press 5 to Fight
    Press 6 to Flee
Enter a valid number to fight or flee from the foe.
You decide to flee from the foe.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_return, expected_return)

    @patch('builtins.input', side_effect=['hello', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_flee_invalid_string(self, mock_output, _):
        actual_return = game.fight_or_flee()
        expected_return = False
        actual_print = mock_output.getvalue()
        expected_print = """\nDo you wish to fight the foe?
    Press 5 to Fight
    Press 6 to Flee
Enter a valid number to fight or flee from the foe.
You decide to flee from the foe.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_return, expected_return)
