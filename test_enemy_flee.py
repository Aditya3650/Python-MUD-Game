import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestEnemyFlee(TestCase):

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_flee_true(self, mock_output, _):
        actual_return = game.enemy_flee()
        expected_return = True
        actual_print = mock_output.getvalue()
        expected_print = "\nThe Ogre has fled from your wrath. Continue your journey in search of Gul'dan.\n"
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(actual_print, expected_print)

    @patch('random.randint', return_value=2)
    def test_enemy_flee_false_one(self, _):
        actual_return = game.enemy_flee()
        expected_return = False
        self.assertEqual(actual_return, expected_return)

    @patch('random.randint', return_value=3)
    def test_enemy_flee_false_two(self, _):
        actual_return = game.enemy_flee()
        expected_return = False
        self.assertEqual(actual_return, expected_return)

    @patch('random.randint', return_value=4)
    def test_enemy_flee_false_three(self, _):
        actual_return = game.enemy_flee()
        expected_return = False
        self.assertEqual(actual_return, expected_return)

    @patch('random.randint', return_value=5)
    def test_enemy_flee_false_four(self, _):
        actual_return = game.enemy_flee()
        expected_return = False
        self.assertEqual(actual_return, expected_return)
