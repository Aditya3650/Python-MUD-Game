from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestBossGame(TestCase):

    @patch('builtins.input', side_effect=['1', 'no'])
    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_game_both_attack(self, mock_output, _, __):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        boss_info = {'Enemy_Health': 2500, 'Enemy_Damage': 119}
        game.boss_game(character_info, boss_info)
        actual_change = character_info, boss_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 881, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 2405, 'Enemy_Damage': 119})
        actual_print = mock_output.getvalue()
        expected_print = "\nYou invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. " \
                         "You gain Health amounting to 33." \
                         "\nYou both attack each other." \
                         "\nYour health is 881 and your enemy has 2405 health remaining.\n" \
                         """\nDo you still wish to fight Gul'Dan?
    Press 5 to Fight
    Press any other button to Flee""" \
                         "\nYou decide to flee from Gul'dan's sorcery. Train and come back stronger!\n"
        self.assertEqual(actual_change, expected_change)
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['1', 'no'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_game_character_attack(self, mock_output, _, __):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        boss_info = {'Enemy_Health': 2500, 'Enemy_Damage': 119}
        game.boss_game(character_info, boss_info)
        actual_change = character_info, boss_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 2405, 'Enemy_Damage': 119})
        actual_print = mock_output.getvalue()
        expected_print = "\nYou invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. " \
                         "You gain Health amounting to 33." \
                         "\nYour enemy misses an attack but you hurt him." \
                         "\nYour health is 1000 and your enemy has 2405 health remaining.\n" \
                         """\nDo you still wish to fight Gul'Dan?
    Press 5 to Fight
    Press any other button to Flee""" \
                         "\nYou decide to flee from Gul'dan's sorcery. Train and come back stronger!\n"
        self.assertEqual(actual_change, expected_change)
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['1', 'no'])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_game_enemy_attack(self, mock_output, _, __):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        boss_info = {'Enemy_Health': 2500, 'Enemy_Damage': 119}
        game.boss_game(character_info, boss_info)
        actual_change = character_info, boss_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 881, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 2500, 'Enemy_Damage': 119})
        actual_print = mock_output.getvalue()
        expected_print = "\nYou invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. " \
                         "You gain Health amounting to 33." \
                         "\nYou miss your attack but your enemy lands a blow." \
                         "\nYour health is 881 and your enemy has 2500 health remaining.\n" \
                         """\nDo you still wish to fight Gul'Dan?
    Press 5 to Fight
    Press any other button to Flee""" \
                         "\nYou decide to flee from Gul'dan's sorcery. Train and come back stronger!\n"
        self.assertEqual(actual_change, expected_change)
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['1', 'no'])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_game_no_attack(self, mock_output, _, __):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        boss_info = {'Enemy_Health': 2500, 'Enemy_Damage': 119}
        game.boss_game(character_info, boss_info)
        actual_change = character_info, boss_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 2500, 'Enemy_Damage': 119})
        actual_print = mock_output.getvalue()
        expected_print = "\nYou invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. " \
                         "You gain Health amounting to 33." \
                         "\nBoth of you miss your attacks." \
                         "\nYour health is 1000 and your enemy has 2500 health remaining.\n" \
                         """\nDo you still wish to fight Gul'Dan?
    Press 5 to Fight
    Press any other button to Flee""" \
                         "\nYou decide to flee from Gul'dan's sorcery. Train and come back stronger!\n"
        self.assertEqual(actual_change, expected_change)
        self.assertEqual(actual_print, expected_print)
