import sys

# setting path
sys.path.append('../')

# importing
from addition import addition
from custom_assertions import is_positive
from subtraction import subtraction
from multiplication import multiplication
import pytest


@pytest.mark.skip
def test_division_by_zero():
    assert 10 / 0 == 0  # Will be skipped

def test_add(capsys):  # Inject the `capsys` fixture
    print("2 + 3 =", addition(2, 3))
    captured = capsys.readouterr()
    assert captured.out == "2 + 3 = 5\n"

@pytest.mark.ricky
@pytest.mark.parametrize("input1, input2, expected", [
    (3, 2, 1),
    (1, 1, 0),
    (20, 10, 10)
])
def test_sub(input1, input2, expected):
    result = subtraction(input1, input2)
    assert result == expected, f"Subtraction of {input1} and {input2} expected to be {expected}, but got {result}"

def test_add_fixture(some_number):
    # Use the fixture value in the test
    result = multiplication(some_number, 2)
    assert result == 84

def test_positive_number():
  assert is_positive(-3)  # Using the custom assertion

def test_negative_number():
  with pytest.raises(AssertionError):
    assert is_positive(-2)  # This will raise an error
