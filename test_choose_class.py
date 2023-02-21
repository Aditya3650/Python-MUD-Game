import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestChooseClass(TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_paladin(self, mock_output, _):
        game.choose_class()
        actual_print = mock_output.getvalue()
        expected_print = """Type the class you want to choose

    Type 1 for Paladin : Paladins are the servants of Light. The Light grants them the strength to fight and makes them 
    very resilient in battles.. Their passive power 'Blessing of the Light' heals them during a battle.

    Type 2 for Warrior : Warriors are seasoned fighters. They have mastery over an arsenal of weaponry and armour. Their
    passive power 'Bloodlust' gives them increased damage during a fight.

    Type 3 for Shaman : Shamans are master of the primal elements. Their mastery over the nature can change the tide of 
    battle at any moment. Their passive power 'Lightning Bolt' decreases the Health of their opponents over time.

    Type 4 for Rogue : Rogues are the assassins of the shadow. Their unseen blade, blinding speed, and subtle poison
    gives them an advantage over any foe. Their passive power 'Poisoned Daggers' decreases the damage output of their
    opponents.
You are a Paladin, the Servant of Light.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_warrior(self, mock_output, _):
        game.choose_class()
        actual_print = mock_output.getvalue()
        expected_print = """Type the class you want to choose

    Type 1 for Paladin : Paladins are the servants of Light. The Light grants them the strength to fight and makes them 
    very resilient in battles.. Their passive power 'Blessing of the Light' heals them during a battle.

    Type 2 for Warrior : Warriors are seasoned fighters. They have mastery over an arsenal of weaponry and armour. Their
    passive power 'Bloodlust' gives them increased damage during a fight.

    Type 3 for Shaman : Shamans are master of the primal elements. Their mastery over the nature can change the tide of 
    battle at any moment. Their passive power 'Lightning Bolt' decreases the Health of their opponents over time.

    Type 4 for Rogue : Rogues are the assassins of the shadow. Their unseen blade, blinding speed, and subtle poison
    gives them an advantage over any foe. Their passive power 'Poisoned Daggers' decreases the damage output of their
    opponents.
You are a Warrior, Lord of War.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_shaman(self, mock_output, _):
        game.choose_class()
        actual_print = mock_output.getvalue()
        expected_print = """Type the class you want to choose

    Type 1 for Paladin : Paladins are the servants of Light. The Light grants them the strength to fight and makes them 
    very resilient in battles.. Their passive power 'Blessing of the Light' heals them during a battle.

    Type 2 for Warrior : Warriors are seasoned fighters. They have mastery over an arsenal of weaponry and armour. Their
    passive power 'Bloodlust' gives them increased damage during a fight.

    Type 3 for Shaman : Shamans are master of the primal elements. Their mastery over the nature can change the tide of 
    battle at any moment. Their passive power 'Lightning Bolt' decreases the Health of their opponents over time.

    Type 4 for Rogue : Rogues are the assassins of the shadow. Their unseen blade, blinding speed, and subtle poison
    gives them an advantage over any foe. Their passive power 'Poisoned Daggers' decreases the damage output of their
    opponents.
You are a Shaman, Master of Nature.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_rogue(self, mock_output, _):
        game.choose_class()
        actual_print = mock_output.getvalue()
        expected_print = """Type the class you want to choose

    Type 1 for Paladin : Paladins are the servants of Light. The Light grants them the strength to fight and makes them 
    very resilient in battles.. Their passive power 'Blessing of the Light' heals them during a battle.

    Type 2 for Warrior : Warriors are seasoned fighters. They have mastery over an arsenal of weaponry and armour. Their
    passive power 'Bloodlust' gives them increased damage during a fight.

    Type 3 for Shaman : Shamans are master of the primal elements. Their mastery over the nature can change the tide of 
    battle at any moment. Their passive power 'Lightning Bolt' decreases the Health of their opponents over time.

    Type 4 for Rogue : Rogues are the assassins of the shadow. Their unseen blade, blinding speed, and subtle poison
    gives them an advantage over any foe. Their passive power 'Poisoned Daggers' decreases the damage output of their
    opponents.
You are a Rogue, Assassin of the Dark.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['8', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_invalid_number(self, mock_output, _):
        game.choose_class()
        actual_print = mock_output.getvalue()
        expected_print = """Type the class you want to choose

    Type 1 for Paladin : Paladins are the servants of Light. The Light grants them the strength to fight and makes them 
    very resilient in battles.. Their passive power 'Blessing of the Light' heals them during a battle.

    Type 2 for Warrior : Warriors are seasoned fighters. They have mastery over an arsenal of weaponry and armour. Their
    passive power 'Bloodlust' gives them increased damage during a fight.

    Type 3 for Shaman : Shamans are master of the primal elements. Their mastery over the nature can change the tide of 
    battle at any moment. Their passive power 'Lightning Bolt' decreases the Health of their opponents over time.

    Type 4 for Rogue : Rogues are the assassins of the shadow. Their unseen blade, blinding speed, and subtle poison
    gives them an advantage over any foe. Their passive power 'Poisoned Daggers' decreases the damage output of their
    opponents.
Enter a valid number to choose a class.
You are a Rogue, Assassin of the Dark.\n"""
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=['hello', 'oops', 'not a number', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_multiple_invalid_string(self, mock_output, _):
        game.choose_class()
        actual_print = mock_output.getvalue()
        expected_print = """Type the class you want to choose

    Type 1 for Paladin : Paladins are the servants of Light. The Light grants them the strength to fight and makes them 
    very resilient in battles.. Their passive power 'Blessing of the Light' heals them during a battle.

    Type 2 for Warrior : Warriors are seasoned fighters. They have mastery over an arsenal of weaponry and armour. Their
    passive power 'Bloodlust' gives them increased damage during a fight.

    Type 3 for Shaman : Shamans are master of the primal elements. Their mastery over the nature can change the tide of 
    battle at any moment. Their passive power 'Lightning Bolt' decreases the Health of their opponents over time.

    Type 4 for Rogue : Rogues are the assassins of the shadow. Their unseen blade, blinding speed, and subtle poison
    gives them an advantage over any foe. Their passive power 'Poisoned Daggers' decreases the damage output of their
    opponents.
Enter a valid number to choose a class.
Enter a valid number to choose a class.
Enter a valid number to choose a class.
You are a Rogue, Assassin of the Dark.\n"""
        self.assertEqual(actual_print, expected_print)
