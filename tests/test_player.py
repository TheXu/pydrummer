import pytest

from pydrummer.player import Player


@pytest.fixture
def player():
    return Player()

def test_settings_created_on_construction():
    print("test_settings_created_on_construction")
    assert player().settings is not None
