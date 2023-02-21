from unittest import TestCase
import game


class TestIncreaseHealthAndXp(TestCase):
    def test_increase_health_and_xp(self):
        character_info = {'Health': 0, 'Current-XP': 0}
        game.increase_health_and_xp(character_info)
        actual_change = character_info
        expected_change = {'Health': 5, 'Current-XP': 10}
        self.assertEqual(actual_change, expected_change)
