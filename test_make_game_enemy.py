from unittest import TestCase
import game


class TestMakeGameEnemy(TestCase):

    def test_make_game_enemy(self):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        actual_return = game.make_game_enemy(character_info)
        expected_return = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        self.assertEqual(actual_return, expected_return)
