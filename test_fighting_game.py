from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestFightingGame(TestCase):

    @patch('builtins.input', side_effect=['1', 'no'])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fighting_game_one_round_enemy_damages(self, mock_output, _, __):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.fighting_game(character_info, enemy_info)
        actual_change = character_info, enemy_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 400, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 952, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 500, 'Enemy_Damage': 48})
        actual_print = mock_output.getvalue()
        expected_print = "You face a Boulderfist Ogre. This should not be a problem for a strong Champion like you.\n" \
                         "\nYou invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. " \
                         "You gain Health amounting to 33." \
                         "\nYou miss your attack but your enemy lands a blow." \
                         "\nYour health is 952 and your enemy has 500 health remaining.\n" \
                         """\nDo you still wish to fight the Ogre?
    Press 5 to Continue Fighting
    Press any other button to Flee""" \
                         "\nYou decide to flee from the Ogre. Live to fight another day!" \
                         "\nYou managed to get away without taking any damage.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['1', 'no'])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fighting_game_one_round_both_miss(self, mock_output, _, __):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.fighting_game(character_info, enemy_info)
        actual_change = character_info, enemy_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 400, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 500, 'Enemy_Damage': 48})
        actual_print = mock_output.getvalue()
        expected_print = "You face a Boulderfist Ogre. This should not be a problem for a strong Champion like you.\n" \
                         "\nYou invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. " \
                         "You gain Health amounting to 33." \
                         "\nBoth of you miss your attacks." \
                         "\nYour health is 1000 and your enemy has 500 health remaining.\n" \
                         """\nDo you still wish to fight the Ogre?
    Press 5 to Continue Fighting
    Press any other button to Flee""" \
                         "\nYou decide to flee from the Ogre. Live to fight another day!" \
                         "\nYou managed to get away without taking any damage.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['1', 'no'])
    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fighting_game_one_round_both_attack(self, mock_output, _, __):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.fighting_game(character_info, enemy_info)
        actual_change = character_info, enemy_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 400, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 952, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 405, 'Enemy_Damage': 48})
        actual_print = mock_output.getvalue()
        expected_print = "You face a Boulderfist Ogre. This should not be a problem for a strong Champion like you.\n" \
                         "\nYou invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. " \
                         "You gain Health amounting to 33." \
                         "\nYou both attack each other." \
                         "\nYour health is 952 and your enemy has 405 health remaining.\n" \
                         """\nDo you still wish to fight the Ogre?
    Press 5 to Continue Fighting
    Press any other button to Flee""" \
                         "\nYou decide to flee from the Ogre. Live to fight another day!" \
                         "\nYou managed to get away without taking any damage.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)

    @patch('builtins.input', side_effect=['1', 'no'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fighting_game_one_round_enemy_flees(self, mock_output, _, __):
        character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000,
                          'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                          'Passive_Power': 'Blessing of the Light'}
        enemy_info = {'Enemy_Health': 500, 'Enemy_Damage': 48}
        game.fighting_game(character_info, enemy_info)
        actual_change = character_info, enemy_info
        expected_change = ({'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 400, 'Level-Up-XP': 1000,
                            'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95,
                            'Passive_Power': 'Blessing of the Light'}, {'Enemy_Health': 405, 'Enemy_Damage': 48})
        actual_print = mock_output.getvalue()
        expected_print = "You face a Boulderfist Ogre. This should not be a problem for a strong Champion like you.\n" \
                         "\nYou invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. " \
                         "You gain Health amounting to 33." \
                         "\nYour enemy misses an attack but you hurt him." \
                         "\nYour health is 1000 and your enemy has 405 health remaining.\n" \
                         "\nThe Ogre has fled from your wrath. Continue your journey in search of Gul'dan.\n"
        self.assertEqual(actual_print, expected_print)
        self.assertEqual(actual_change, expected_change)
