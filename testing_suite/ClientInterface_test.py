import pytest
import sys
sys.path.append("..")
from ClientInterface import *
from Records import *

@pytest.fixture
def ci():
    ci = ClientInterface()
    return ci

@pytest.fixture
def member():
    a = Address("Test Street", "Test City", "OR", 99999)
    m = MemberRecord("Test Nmae", 100112136, a)
    return m

def test_verify_member_exists(ci):
    assert ci.verify_member_exists(100112136) == True
    assert ci.verify_member_exists(111111111) == False


def test_verify_provider_exists(ci):
    assert ci.verify_provider_exists(101127287) == True
    assert ci.verify_provider_exists(111111111) == False

def test_get_member(ci, member):
    m = ci.get_member(100112136)
    assert m.name == member.name
    assert m.ID == member.ID
    assert m.street == member.street
    assert m.city == member.city
    assert m.state == member.state
    assert m.zip == member.zip
    assert m.is_suspended == member.is_suspended
