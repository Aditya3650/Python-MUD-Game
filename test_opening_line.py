from unittest import TestCase
import game
from unittest.mock import patch
import io


class TestOpeningLine(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_opening_line(self, mock_output):
        game.opening_line()
        actual_output = mock_output.getvalue()
        expected_output = """\nYou are in search of Gul'dan the Warlock, the leader of the Horde, who destroyed your \
clan. 
He was last seen at the top of the Blackrock Mountain, preparing for his next raid. You have trained all your life 
to defeat him. This is your chance to seek revenge for what he did.\n\n"""
        self.assertEqual(actual_output, expected_output)
