import pytest
from finding import finding


def test_single_case():
    assert finding([42]) == 42
