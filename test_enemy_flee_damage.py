import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestEnemyFleeDamage(TestCase):

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_flee_damage_taken(self, mock_output, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.enemy_flee_damage(character_info, enemy_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Health': 952, 'Max_Health': 1000, 'Damage': 95,
                           'Passive_Power': 'Blessing of the Light'}
        actual_print = mock_output.getvalue()
        expected_print = "However, you were damaged while fleeing the battle.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_flee_damage_not_taken_one(self, mock_output, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.enemy_flee_damage(character_info, enemy_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                           'Passive_Power': 'Blessing of the Light'}
        actual_print = mock_output.getvalue()
        expected_print = "You managed to get away without taking any damage.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_flee_damage_not_taken_two(self, mock_output, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.enemy_flee_damage(character_info, enemy_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                           'Passive_Power': 'Blessing of the Light'}
        actual_print = mock_output.getvalue()
        expected_print = "You managed to get away without taking any damage.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_flee_damage_not_taken_three(self, mock_output, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.enemy_flee_damage(character_info, enemy_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                           'Passive_Power': 'Blessing of the Light'}
        actual_print = mock_output.getvalue()
        expected_print = "You managed to get away without taking any damage.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_flee_damage_not_taken_four(self, mock_output, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.enemy_flee_damage(character_info, enemy_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                           'Passive_Power': 'Blessing of the Light'}
        actual_print = mock_output.getvalue()
        expected_print = "You managed to get away without taking any damage.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)
