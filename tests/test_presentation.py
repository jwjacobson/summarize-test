import pytest

def test_assertion():
    assert 1 == 1

@pytest.mark.xfail(reason="Designed to fail")
def test_assertion_fail():
    assert 1 == 2