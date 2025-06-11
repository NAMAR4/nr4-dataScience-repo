import pytest
from finding import finding


def test_negative_case():
    assert finding([1, -2, 3, -4, 3, 1, -2]) == -4
