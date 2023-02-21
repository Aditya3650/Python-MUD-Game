from unittest import TestCase
import game
from unittest.mock import patch
import io


class TestFinalMessageNotFinish(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_message_not_finish(self, mock_output):
        game.final_message_not_finish()
        actual_output = mock_output.getvalue()
        expected_output = "Thanks for playing this game, come again later!\n"
        self.assertEqual(actual_output, expected_output)
