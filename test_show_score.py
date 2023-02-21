from unittest import TestCase
import game
from unittest.mock import patch
import io


class TestShowScore(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_score(self, mock_output):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 200, 'Level-Up-XP': 1000,
                          'Class': 'Rogue', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Class_Level': 'Assassin', 'Name': 'Aditya', 'Passive_Power': 'Poisoned Daggers'}
        game.show_score(character_info)
        actual_print = mock_output.getvalue()
        expected_print = "Name: Aditya, Level: 2, Class: Rogue, Class_Level: Assassin, Passive: Poisoned Daggers, " \
                         "Health: 1000, Max Health: 1000, Current XP: 200, XP Required For Level Up: 800\n"
        self.assertEqual(actual_print, expected_print)
