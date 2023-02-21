from unittest import TestCase
import game


class TestSetDamageAndPassive(TestCase):

    def test_set_health_for_paladin(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin'}
        game.set_damage_and_passive(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Damage': 95, 'Passive_Power': 'Blessing of the Light'}
        self.assertEqual(actual_change, expected_change)

    def test_set_health_for_warrior(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Warrior'}
        game.set_damage_and_passive(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Warrior', 'Damage': 80, 'Passive_Power': 'Bloodlust'}
        self.assertEqual(actual_change, expected_change)

    def test_set_health_for_shaman(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Shaman'}
        game.set_damage_and_passive(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Shaman', 'Damage': 110, 'Passive_Power': 'Lightning Bolt'}
        self.assertEqual(actual_change, expected_change)

    def test_set_health_for_rogue(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Rogue'}
        game.set_damage_and_passive(character_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Rogue', 'Damage': 120, 'Passive_Power': 'Poisoned Daggers'}
        self.assertEqual(actual_change, expected_change)
