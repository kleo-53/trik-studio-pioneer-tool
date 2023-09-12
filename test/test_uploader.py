from pathlib import Path

import pytest
import pioneer_uploader
from unittest.mock import patch


@patch("logging.error")
def test_without_file(mock_logging_error):
    test_args = ["parameter", "invalid_file_path", "invalid_ip", "invalid_port", "invalid_mode"]
    with patch('sys.argv', test_args):
        pioneer_uploader.main()
    mock_logging_error.assert_called_once_with("Can not find program file")


@patch("logging.error")
def test_few_arguments(mock_logging_error):
    test_args = ["less then", "five", "arguments"]
    with patch('sys.argv', test_args):
        pioneer_uploader.main()
    mock_logging_error.assert_called_once_with("Invalid arguments")


@patch("logging.error")
def test_correct_arguments(mock_logging_error):
    current_file = Path(__file__).resolve()
    file = current_file.parent/'test_file.lua'
    print(file)
    test_args = ["parameter", file, "127.0.0.1", "8888", "wifi"]
    with patch('sys.argv', test_args):
        with pytest.raises(ConnectionResetError):
            pioneer_uploader.main()
    # mock_logging_error.assert_called_once_with(ConnectionResetError(10054,
    # 'An existing connection was forcibly closed by the remote host', None, 10054, None))


if __name__ == "__main__":
    pytest.main()
