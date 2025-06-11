import pytest
from finding import finding

def test_no_list_case():
    with pytest.raises(ValueError):
        finding("not a list ;)") 