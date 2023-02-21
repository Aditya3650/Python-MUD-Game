from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestMakeMap(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_map_boss_invisible(self, mock_output):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 0}
        game.make_map(4, 4, character_info)
        actual_print = mock_output.getvalue()
        expected_print = """\n|_#_|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|\n\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_map_boss_visible(self, mock_output):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3}
        game.make_map(4, 4, character_info)
        actual_print = mock_output.getvalue()
        expected_print = """\n|_#_|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|_💀_|\n\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_map_boss_and_minigame_visible(self, mock_output):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3}
        game.make_map(6, 6, character_info)
        actual_print = mock_output.getvalue()
        expected_print = """\n|_#_|___|___|___|___|___|
|___|___|___|___|___|___|
|___|___|___|___|___|___|
|___|___|___|___|___|___|
|___|___|___|___|_🕎|___|
|___|___|___|___|___|_💀_|\n\n"""
        self.assertEqual(actual_print, expected_print)
