import pytest
from finding import finding


def test_formate_case():
    with pytest.raises(ValueError):
        finding(["Hello", 2, 5, 6, 2, 5, "World"]) 
