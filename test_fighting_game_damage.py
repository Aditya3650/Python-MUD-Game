import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestFightingGameDamage(TestCase):

    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fighting_game_both_damage(self, mock_output, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.fighting_game_damage(character_info, enemy_info)
        actual_change = character_info, enemy_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 952, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 405, 'Enemy_Damage': 48})
        actual_print = mock_output.getvalue()
        expected_print = "You both attack each other." \
                         "\nYour health is 952 and your enemy has 405 health remaining.\n"
        self.assertEqual(actual_change, expected_change)
        self.assertEqual(actual_print, expected_print)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fighting_game_character_damage(self, mock_output, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.fighting_game_damage(character_info, enemy_info)
        actual_change = character_info, enemy_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 405, 'Enemy_Damage': 48})
        actual_print = mock_output.getvalue()
        expected_print = "Your enemy misses an attack but you hurt him." \
                         "\nYour health is 1000 and your enemy has 405 health remaining.\n"
        self.assertEqual(actual_change, expected_change)
        self.assertEqual(actual_print, expected_print)

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fighting_game_enemy_damage(self, mock_output, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.fighting_game_damage(character_info, enemy_info)
        actual_change = character_info, enemy_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 952, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 500, 'Enemy_Damage': 48})
        actual_print = mock_output.getvalue()
        expected_print = "You miss your attack but your enemy lands a blow." \
                         "\nYour health is 952 and your enemy has 500 health remaining.\n"
        self.assertEqual(actual_change, expected_change)
        self.assertEqual(actual_print, expected_print)

    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fighting_game_no_damage(self, mock_output, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.fighting_game_damage(character_info, enemy_info)
        actual_change = character_info, enemy_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 500, 'Enemy_Damage': 48})
        actual_print = mock_output.getvalue()
        expected_print = "Both of you miss your attacks." \
                         "\nYour health is 1000 and your enemy has 500 health remaining.\n"
        self.assertEqual(actual_change, expected_change)
        self.assertEqual(actual_print, expected_print)
