from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestBossDead(TestCase):

    def test_boss_dead_false(self):
        character_info = {'Health': 100}
        boss_info = {'Enemy_Health': 100}
        actual_return = game.boss_dead(character_info, boss_info)
        expected_return = False
        self.assertEqual(actual_return, expected_return)

    def test_boss_dead_character_also_dead(self):
        character_info = {'Health': 0}
        boss_info = {'Enemy_Health': 0}
        actual_return = game.boss_dead(character_info, boss_info)
        expected_return = False
        self.assertEqual(actual_return, expected_return)

    def test_boss_dead_character_dead_boss_alive(self):
        character_info = {'Health': 0}
        boss_info = {'Enemy_Health': 10}
        actual_return = game.boss_dead(character_info, boss_info)
        expected_return = False
        self.assertEqual(actual_return, expected_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_dead_true(self, mock_output):
        character_info = {'Health': 100}
        boss_info = {'Enemy_Health': 0}
        actual_return = game.boss_dead(character_info, boss_info)
        expected_return = True
        actual_print = mock_output.getvalue()
        expected_print = "\nGul'dan is dead. Your soul is at peace finally.\n"
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(actual_print, expected_print)
