from unittest import TestCase
import game


class TestMoveCharacter(TestCase):
    def test_move_character_east(self):
        direction = '1'
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        game.move_character(character, direction)
        expected_change_in_character = {'X-coordinate': 1, 'Y-coordinate': 2}
        self.assertEqual(character, expected_change_in_character)

    def test_move_character_south(self):
        direction = '2'
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        game.move_character(character, direction)
        expected_change_in_character = {'X-coordinate': 2, 'Y-coordinate': 1}
        self.assertEqual(character, expected_change_in_character)

    def test_move_character_west(self):
        direction = '3'
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        game.move_character(character, direction)
        expected_change_in_character = {'X-coordinate': 1, 'Y-coordinate': 0}
        self.assertEqual(character, expected_change_in_character)

    def test_move_character_north(self):
        direction = '4'
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        game.move_character(character, direction)
        expected_change_in_character = {'X-coordinate': 0, 'Y-coordinate': 1}
        self.assertEqual(character, expected_change_in_character)
