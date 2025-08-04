import os

import pytest

from src.decorators import my_function


def test_my_function_console_output(capsys):
    my_function(2, 3)
    captured = capsys.readouterr()
    assert "Функция my_function ок." in captured.out


def test_my_function_file_output():
    my_function(2, 3)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        content = file.read()
    assert "Функция wrapper ок." in content
    os.remove("mylog.txt")
