from unittest import TestCase
import game


class TestSetHealth(TestCase):

    def test_set_health_for_paladin(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin'}
        game.set_health(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000}
        self.assertEqual(actual_change, expected_change)

    def test_set_health_for_warrior(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Warrior'}
        game.set_health(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Warrior', 'Health': 1200, 'Max_Health': 1200}
        self.assertEqual(actual_change, expected_change)

    def test_set_health_for_shaman(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Shaman'}
        game.set_health(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Shaman', 'Health': 900, 'Max_Health': 900}
        self.assertEqual(actual_change, expected_change)

    def test_set_health_for_rogue(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Rogue'}
        game.set_health(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Rogue', 'Health': 800, 'Max_Health': 800}
        self.assertEqual(actual_change, expected_change)
