from unittest import TestCase
import game
from unittest.mock import patch
import io


class TestXpChecker(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_xp_checker_paladin_two(self, mock_output):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 1001, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95, 'Class_Level': 'Squire',
                          'Passive_Power': 'Blessing of the Light'}
        game.xp_checker(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 1, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Health': 1100, 'Max_Health': 1100, 'Damage': 105,
                           'Class_Level': 'Commander', 'Passive_Power': 'Blessing of the Light'}
        actual_print = mock_output.getvalue()
        expected_print = """\nYou have levelled up.
You are now level 2.
Your champion is now a Commander.
Your current Health is 1100.
Your maximum Health is 1100.
Your damage is 105.
XP required to level up is 999.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_xp_checker_paladin_three(self, mock_output2):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 1200, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Class_Level': 'Commander'}
        game.xp_checker(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 200, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Health': 1100, 'Max_Health': 1100, 'Damage': 105,
                           'Class_Level': 'Prince'}
        actual_print = mock_output2.getvalue()
        expected_print = """\nYou have levelled up.
You are now level 3.
Your champion is now a Prince.
Your current Health is 1100.
Your maximum Health is 1100.
Your damage is 105.
XP required to level up is 800.

You sense Gul'Dan at the edge of the Barrens, on top of the Blackrock Mountain. You must make your there to finally \
taste the sweet revenge you have longed for.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_xp_checker_warrior_two(self, mock_output):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 1001, 'Level-Up-XP': 1000,
                          'Class': 'Warrior', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95}
        game.xp_checker(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 1, 'Level-Up-XP': 1000,
                           'Class': 'Warrior', 'Health': 1100, 'Max_Health': 1100, 'Damage': 105,
                           'Class_Level': 'Taskmaster'}
        actual_print = mock_output.getvalue()
        expected_print = """\nYou have levelled up.
You are now level 2.
Your champion is now a Taskmaster.
Your current Health is 1100.
Your maximum Health is 1100.
Your damage is 105.
XP required to level up is 999.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_xp_checker_warrior_three(self, mock_output2):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 1200, 'Level-Up-XP': 1000,
                          'Class': 'Warrior', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Class_Level': 'Taskmaster'}
        game.xp_checker(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 200, 'Level-Up-XP': 1000,
                           'Class': 'Warrior', 'Health': 1100, 'Max_Health': 1100, 'Damage': 105,
                           'Class_Level': 'Warlord'}
        actual_print = mock_output2.getvalue()
        expected_print = """\nYou have levelled up.
You are now level 3.
Your champion is now a Warlord.
Your current Health is 1100.
Your maximum Health is 1100.
Your damage is 105.
XP required to level up is 800.

You sense Gul'Dan at the edge of the Barrens, on top of the Blackrock Mountain. You must make your there to finally \
taste the sweet revenge you have longed for.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_xp_checker_shaman_two(self, mock_output):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 1001, 'Level-Up-XP': 1000,
                          'Class': 'Shaman', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95}
        game.xp_checker(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 1, 'Level-Up-XP': 1000,
                           'Class': 'Shaman', 'Health': 1100, 'Max_Health': 1100, 'Damage': 105,
                           'Class_Level': 'Windlord'}
        actual_print = mock_output.getvalue()
        expected_print = """\nYou have levelled up.
You are now level 2.
Your champion is now a Windlord.
Your current Health is 1100.
Your maximum Health is 1100.
Your damage is 105.
XP required to level up is 999.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_xp_checker_shaman_three(self, mock_output2):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 1200, 'Level-Up-XP': 1000,
                          'Class': 'Shaman', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Class_Level': 'Windlord'}
        game.xp_checker(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 200, 'Level-Up-XP': 1000,
                           'Class': 'Shaman', 'Health': 1100, 'Max_Health': 1100, 'Damage': 105,
                           'Class_Level': 'Deathseer'}
        actual_print = mock_output2.getvalue()
        expected_print = """\nYou have levelled up.
You are now level 3.
Your champion is now a Deathseer.
Your current Health is 1100.
Your maximum Health is 1100.
Your damage is 105.
XP required to level up is 800.

You sense Gul'Dan at the edge of the Barrens, on top of the Blackrock Mountain. You must make your there to finally \
taste the sweet revenge you have longed for.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_xp_checker_rogue_two(self, mock_output):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 1001, 'Level-Up-XP': 1000,
                          'Class': 'Rogue', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95}
        game.xp_checker(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 1, 'Level-Up-XP': 1000,
                           'Class': 'Rogue', 'Health': 1100, 'Max_Health': 1100, 'Damage': 105,
                           'Class_Level': 'Assassin'}
        actual_print = mock_output.getvalue()
        expected_print = """\nYou have levelled up.
You are now level 2.
Your champion is now a Assassin.
Your current Health is 1100.
Your maximum Health is 1100.
Your damage is 105.
XP required to level up is 999.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_xp_checker_rogue_three(self, mock_output2):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 1200, 'Level-Up-XP': 1000,
                          'Class': 'Rogue', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Class_Level': 'Assassin'}
        game.xp_checker(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 200, 'Level-Up-XP': 1000,
                           'Class': 'Rogue', 'Health': 1100, 'Max_Health': 1100, 'Damage': 105,
                           'Class_Level': 'Nightslayer'}
        actual_print = mock_output2.getvalue()
        expected_print = """\nYou have levelled up.
You are now level 3.
Your champion is now a Nightslayer.
Your current Health is 1100.
Your maximum Health is 1100.
Your damage is 105.
XP required to level up is 800.

You sense Gul'Dan at the edge of the Barrens, on top of the Blackrock Mountain. You must make your there to finally \
taste the sweet revenge you have longed for.\n"""
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    def test_xp_checker_no_change(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 200, 'Level-Up-XP': 1000,
                          'Class': 'Rogue', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Class_Level': 'Assassin'}
        game.xp_checker(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 200, 'Level-Up-XP': 1000,
                           'Class': 'Rogue', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                           'Class_Level': 'Assassin'}
        self.assertEqual(actual_change, expected_change)
