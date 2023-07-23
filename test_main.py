import pytest
from main import divide


def test_divide():
    assert divide(4, 2) == 2
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(4, 0)
