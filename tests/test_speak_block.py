from unittest.mock import patch, Mock
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..speak_block import Speak


class TestExample(NIOBlockTestCase):

    @patch('pyttsx3.init')
    def test_process_signals(self, mock_init):
        """Messages are queued for every signal."""
        mock_engine = mock_init.return_value = Mock()
        blk = Speak()
        self.configure_block(blk, {
            "message": "{{ $bar }}",
            "volume": 0.5,
            "rate": 42,
        })
        blk.start()
        mock_init.assert_called_once_with()
        self.assertEqual(mock_engine.setProperty.call_count, 2)
        self.assertEqual(mock_engine.setProperty.call_args_list[0][0], ("rate", 42))
        self.assertEqual(mock_engine.setProperty.call_args_list[1][0], ("volume", 0.5))
        blk.process_signals([Signal({"bar": "nio foo foo"})])
        mock_engine.say.assert_called_once_with("nio foo foo")
        mock_engine.runAndWait.assert_called_once_with()
        blk.stop()
        mock_engine.stop.assert_called_once_with()
