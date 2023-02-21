from unittest import TestCase
import game


class TestSetClass(TestCase):

    def test_set_class_to_paladin(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
        class_number = 1
        game.set_class(class_number, character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin'}
        self.assertEqual(actual_change, expected_change)

    def test_set_class_to_warrior(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
        class_number = 2
        game.set_class(class_number, character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Warrior'}
        self.assertEqual(actual_change, expected_change)

    def test_set_class_to_shaman(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
        class_number = 3
        game.set_class(class_number, character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Shaman'}
        self.assertEqual(actual_change, expected_change)

    def test_set_class_to_rogue(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
        class_number = 4
        game.set_class(class_number, character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Rogue'}
        self.assertEqual(actual_change, expected_change)
