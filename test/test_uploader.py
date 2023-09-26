import pytest
import repackage
import os
from unittest.mock import patch

repackage.up()
import pioneer_uploader


current_directory = os.path.dirname(os.path.abspath(__file__))
test_file_path = os.path.join(current_directory, "test_file.lua")


@patch("logging.error")
def test_few_arguments(mock_logging_error):
    test_args = [
        ["less then", "five", "arguments"],
        ["parameter", "still", "less", "arguments"],
        [""],
        ["parameter", "test_file.lua"],
    ]
    expected_errors = [
        "not enough values to unpack (expected 4, got 2)",
        "not enough values to unpack (expected 4, got 3)",
        "not enough values to unpack (expected 4, got 0)",
        "not enough values to unpack (expected 4, got 1)",
    ]
    for i in range(len(test_args)):
        with patch("sys.argv", test_args[i]):
            pioneer_uploader.main()
        args, _ = mock_logging_error.call_args
        assert isinstance(args[0], ValueError)
        assert str(args[0]) == expected_errors[i]


@patch("logging.error")
def test_missing_file(mock_logging_error):
    test_args = [
        [
            "parameter",
            "invalid_file_path.aaa",
            "invalid_ip",
            "invalid_port",
            "invalid_mode",
        ],
        ["parameter", "some_file.lua", "invalid_ip", "invalid_port", "invalid_mode"],
        ["parameter", "8888", "invalid_ip", "invalid_port", "invalid_mode"],
        ["parameter", "some_file.luac", "invalid_ip", "invalid_port", "invalid_mode"],
    ]
    for i in range(len(test_args)):
        with patch("sys.argv", test_args[i]):
            pioneer_uploader.main()
        args, _ = mock_logging_error.call_args
        assert isinstance(args[0], FileNotFoundError)
        assert str(args[0]) == "Can not find program file"


@patch("logging.error")
def test_invalid_ip(mock_logging_error):
    test_args = [
        ["parameter", test_file_path, "127.3.not.ip", "port", "mode"],
        ["parameter", test_file_path, "127.3.43254.00", "port", "mode"],
        ["parameter", test_file_path, "8888", "port", "mode"],
        ["parameter", test_file_path, "serial", "port", "mode"],
    ]
    for i in range(len(test_args)):
        with patch("sys.argv", test_args[i]):
            pioneer_uploader.main()
        args, _ = mock_logging_error.call_args
        assert isinstance(args[0], ValueError)
        assert str(args[0]) == "Invalid IP address"


@patch("logging.error")
def test_invalid_port(mock_logging_error):
    test_args = [
        ["parameter", test_file_path, "127.0.0.1", "43242342", "mode"],
        ["parameter", test_file_path, "127.0.0.1", "127.0.0.1", "mode"],
        ["parameter", test_file_path, "127.0.0.1", "udpin", "mode"],
        ["parameter", test_file_path, "127.0.0.1", "port", "mode"],
    ]
    expected_errors = [
        "Invalid port",
        "invalid literal for int() with base 10: '127.0.0.1'",
        "invalid literal for int() with base 10: 'udpin'",
        "invalid literal for int() with base 10: 'port'",
    ]
    for i in range(len(test_args)):
        with patch("sys.argv", test_args[i]):
            pioneer_uploader.main()
        args, _ = mock_logging_error.call_args
        assert isinstance(args[0], ValueError)
        assert str(args[0]) == expected_errors[i]


@patch("logging.error")
def test_invalid_mode(mock_logging_error):
    test_args = [
        ["parameter", test_file_path, "127.0.0.1", "8888", "8888"],
        ["parameter", test_file_path, "127.0.0.1", "8888", "udpin"],
        ["parameter", test_file_path, "127.0.0.1", "8888", "serial"],
        ["parameter", test_file_path, "127.0.0.1", "8888", "127.0.0.1"],
    ]
    for i in range(len(test_args)):
        with patch("sys.argv", test_args[i]):
            pioneer_uploader.main()
        args, _ = mock_logging_error.call_args
        assert isinstance(args[0], ValueError)
        assert str(args[0]) == "Invalid mode. Choose 'wifi' or 'usb'"


if __name__ == "__main__":
    pytest.main()
