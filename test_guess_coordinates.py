from unittest import TestCase
import game


class TestGuessCoordinates(TestCase):

    def test_guess_coordinates(self):
        actual_return = game.guess_coordinates()
        expected_return = [(4, 4), (4, 9), (4, 15), (4, 20), (9, 4), (9, 9), (9, 15), (9, 20), (15, 4), (15, 9),
                           (15, 15), (15, 20), (20, 4), (20, 9), (20, 15), (20, 20)]
        self.assertEqual(actual_return, expected_return)
