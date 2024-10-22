import pytest
from main import allowed_file, predict


def test_allowed_file():
    assert allowed_file("cool_pic.jpeg")


def test_disallowed_file():
    assert not allowed_file("boring_spreadsheet.xlsx")


def test_predict():
    assert predict("static/grand_budapest_hotel-0136_cropped.jpg") > 0
