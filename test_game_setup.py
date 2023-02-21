from unittest import TestCase
import game
from unittest.mock import patch


class TestGameSetup(TestCase):

    @patch('builtins.input', side_effect=['Aditya', '1'])
    def test_game_setup_paladin(self, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
        game.game_setup(character_info)
        actual_change = character_info
        expected_change = {'Class': 'Paladin',
                           'Class_Level': 'Squire',
                           'Current-XP': 0,
                           'Damage': 95,
                           'Health': 1000,
                           'Level': 1,
                           'Level-Up-XP': 1000,
                           'Max_Health': 1000,
                           'Name': 'Aditya',
                           'Passive_Power': 'Blessing of the Light',
                           'X-coordinate': 0,
                           'Y-coordinate': 0}
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['Aditya', '2'])
    def test_game_setup_warrior(self, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
        game.game_setup(character_info)
        actual_change = character_info
        expected_change = {'Class': 'Warrior',
                           'Class_Level': 'Recruit',
                           'Current-XP': 0,
                           'Damage': 80,
                           'Health': 1200,
                           'Level': 1,
                           'Level-Up-XP': 1000,
                           'Max_Health': 1200,
                           'Name': 'Aditya',
                           'Passive_Power': 'Bloodlust',
                           'X-coordinate': 0,
                           'Y-coordinate': 0}
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['Aditya', '3'])
    def test_game_setup_shaman(self, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
        game.game_setup(character_info)
        actual_change = character_info
        expected_change = {'Class': 'Shaman',
                           'Class_Level': 'Novice',
                           'Current-XP': 0,
                           'Damage': 110,
                           'Health': 900,
                           'Level': 1,
                           'Level-Up-XP': 1000,
                           'Max_Health': 900,
                           'Name': 'Aditya',
                           'Passive_Power': 'Lightning Bolt',
                           'X-coordinate': 0,
                           'Y-coordinate': 0}
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['Aditya', '4'])
    def test_game_setup_rogue(self, _):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
        game.game_setup(character_info)
        actual_change = character_info
        expected_change = {'Class': 'Rogue',
                           'Class_Level': 'Shadow',
                           'Current-XP': 0,
                           'Damage': 120,
                           'Health': 800,
                           'Level': 1,
                           'Level-Up-XP': 1000,
                           'Max_Health': 800,
                           'Name': 'Aditya',
                           'Passive_Power': 'Poisoned Daggers',
                           'X-coordinate': 0,
                           'Y-coordinate': 0}
        self.assertEqual(actual_change, expected_change)
