import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_north(self, mock_output, _):
        game.get_user_choice()
        actual_print = mock_output.getvalue()
        expected_print = """\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)
You are moving East.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_east(self, mock_output, _):
        game.get_user_choice()
        actual_print = mock_output.getvalue()
        expected_print = """\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)
You are moving South.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_south(self, mock_output, _):
        game.get_user_choice()
        actual_print = mock_output.getvalue()
        expected_print = """\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)
You are moving West.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_west(self, mock_output, _):
        game.get_user_choice()
        actual_print = mock_output.getvalue()
        expected_print = """\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)
You are moving North.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['8', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_number(self, mock_output, _):
        game.get_user_choice()
        actual_print = mock_output.getvalue()
        expected_print = """\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)
Enter a valid number.
You are moving South.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['hello', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_string(self, mock_output, _):
        game.get_user_choice()
        actual_print = mock_output.getvalue()
        expected_print = """\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)
Enter a valid number.
You are moving West.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['score'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_score(self, mock_output, _):
        game.get_user_choice()
        actual_print = mock_output.getvalue()
        expected_print = """\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_quit_lowercase(self, mock_output, _):
        game.get_user_choice()
        actual_print = mock_output.getvalue()
        expected_print = """\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['QUIT'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_quit_uppercase(self, mock_output, _):
        game.get_user_choice()
        actual_print = mock_output.getvalue()
        expected_print = """\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['qUiT'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_quit_mixed_case(self, mock_output, _):
        game.get_user_choice()
        actual_print = mock_output.getvalue()
        expected_print = """\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)\n"""
        self.assertEqual(actual_print, expected_print)
