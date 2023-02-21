from unittest import TestCase
import game
from unittest.mock import patch
import io


class TestFinalGameFinish(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_message_finish(self, mock_output):
        game.final_message_finish()
        actual_output = mock_output.getvalue()
        expected_output = "Congratulations! You have completed your quest for vengeance. Thanks for playing the game!\n"
        self.assertEqual(actual_output, expected_output)
