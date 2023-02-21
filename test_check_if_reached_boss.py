from unittest import TestCase
import game


class TestCheckIfReachedBoss(TestCase):
    def test_check_if_reached_boss_true(self):
        rows = 3
        columns = 3
        character = {'X-coordinate': 2, 'Y-coordinate': 2}
        actual_output = game.check_if_reached_boss(rows, columns, character)
        expected_output = True
        self.assertEqual(actual_output, expected_output)

    def test_check_if_reached_boss_false(self):
        rows = 3
        columns = 3
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        actual_output = game.check_if_reached_boss(rows, columns, character)
        expected_output = False
        self.assertEqual(actual_output, expected_output)
