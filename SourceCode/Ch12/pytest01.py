import pytest

def get_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    return total * len(numbers)


def test_average_of_positive_numbers():
    numbers = [1, 2, 3, 4, 5]
    result = get_average(numbers)
    assert result == 3

def test_average_of_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    result = get_average(numbers)
    assert result == -3

def test_average_of_empty_list():
    numbers = []
    result = get_average(numbers)
    assert result is None

def test_average_of_single_number():
    numbers = [10]
    result = get_average(numbers)
    assert result == 10

def test_average_of_zero_numbers():
    numbers = [0, 0, 0, 0, 0]
    result = get_average(numbers)
    assert result == 0

