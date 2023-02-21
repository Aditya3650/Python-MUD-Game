from unittest import TestCase
import game


class TestClassLevel(TestCase):

    def test_class_level_paladin_one(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Class_Level': 'Squire'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_paladin_two(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Class_Level': 'Squire'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Class_Level': 'Commander'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_paladin_three(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Class_Level': 'Commander'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Class_Level': 'Prince'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_warrior_one(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Warrior'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Warrior', 'Class_Level': 'Recruit'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_warrior_two(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Warrior', 'Class_Level': 'Recruit'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Warrior', 'Class_Level': 'Taskmaster'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_warrior_three(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Warrior', 'Class_Level': 'Taskmaster'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Warrior', 'Class_Level': 'Warlord'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_shaman_one(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Shaman'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Shaman', 'Class_Level': 'Novice'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_shaman_two(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Shaman', 'Class_Level': 'Novice'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Shaman', 'Class_Level': 'Windlord'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_shaman_three(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Shaman', 'Class_Level': 'Windlord'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Shaman', 'Class_Level': 'Deathseer'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_rogue_one(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Rogue'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Rogue', 'Class_Level': 'Shadow'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_rogue_two(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Rogue', 'Class_Level': 'Shadow'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Rogue', 'Class_Level': 'Assassin'}
        self.assertEqual(actual_change, expected_change)

    def test_class_level_rogue_three(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Rogue', 'Class_Level': 'Assassin'}
        game.class_level(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Rogue', 'Class_Level': 'Nightslayer'}
        self.assertEqual(actual_change, expected_change)
