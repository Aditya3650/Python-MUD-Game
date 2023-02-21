from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestMakeGameBoss(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_game_boss(self, mock_output):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        actual_return = game.make_game_boss(character_info)
        expected_return = {'Enemy_Health': 2500, 'Enemy_Damage': 119}
        actual_print = mock_output.getvalue()
        expected_print = "\nYou face the leader of the Horde, Gul'dan.\n"
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(actual_print, expected_print)
