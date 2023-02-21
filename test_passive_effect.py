from unittest import TestCase
import game


class TestPassiveEffect(TestCase):

    def test_passive_effect_paladin_not_max(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 100, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.passive_effect(character_info, enemy_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Health': 133, 'Max_Health': 1000, 'Damage': 95,
                           'Passive_Power': 'Blessing of the Light'}
        self.assertEqual(actual_change, expected_change)

    def test_passive_effect_paladin_max(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.passive_effect(character_info, enemy_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                           'Passive_Power': 'Blessing of the Light'}
        self.assertEqual(actual_change, expected_change)

    def test_passive_effect_warrior(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Warrior', 'Health': 100, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Bloodlust'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.passive_effect(character_info, enemy_info)
        actual_change = character_info
        expected_change = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                           'Class': 'Warrior', 'Health': 100, 'Max_Health': 1000, 'Damage': 105,
                           'Passive_Power': 'Bloodlust'}
        self.assertEqual(actual_change, expected_change)

    def test_passive_effect_shaman(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Shaman', 'Health': 100, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Lightning Bolt'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.passive_effect(character_info, enemy_info)
        actual_change = enemy_info
        expected_change = {'Enemy_Health': 450, 'Enemy_Damage': 48}
        self.assertEqual(actual_change, expected_change)

    def test_passive_effect_rogue(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Rogue', 'Health': 100, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Lightning Bolt'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.passive_effect(character_info, enemy_info)
        actual_change = enemy_info
        expected_change = {'Enemy_Health': 500, 'Enemy_Damage': 38}
        self.assertEqual(actual_change, expected_change)
