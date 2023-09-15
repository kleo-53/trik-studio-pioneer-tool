import pytest
import pioneer_uploader
from unittest.mock import patch


@patch("logging.error")
def test_without_file(mock_logging_error):
    test_args = [
        "parameter",
        "invalid_file_path",
        "invalid_ip",
        "invalid_port",
        "invalid_mode"
    ]
    with patch("sys.argv", test_args):
        pioneer_uploader.main()
    mock_logging_error.assert_called_once_with("Can not find program file")


@patch("logging.error")
def test_few_arguments(mock_logging_error):
    test_args = ["less then", "five", "arguments"]
    with patch("sys.argv", test_args):
        pioneer_uploader.main()
    mock_logging_error.assert_called_once_with("Invalid arguments")


if __name__ == "__main__":
    pytest.main()
