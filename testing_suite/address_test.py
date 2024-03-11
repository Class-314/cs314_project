
import pytest
import sys
sys.path.append("..")
import Records


# pytest fixture just gives us a default object to work with in the other tests
@pytest.fixture
def setup():
    a = Records.Address("10 Main St.", "Portland", "OR", "97035")
    return a

# testing the exceptions in __init__
def test_init_raises_exceptions():
    with pytest.raises(ValueError) as e:
        obj = Records.Address("a")
    assert str(e.value) == "Other is not of type Address in copy constructor"

    with pytest.raises(ValueError)as e:
        obj = Records.Address("a", "b")
    assert str(e.value) == "Incorrect number of arguments when initializing Address"

# Constructor testing

def test_default_constructor():
    obj = Records.Address()
    assert obj._street == None
    assert obj._city == None
    assert obj._state == None
    assert obj._zip == None

def test_param_constructor():
    # Default Test
    obj = Records.Address("10 Main St.", "Portland", "OR", "97035")
    assert obj._street == "10 Main St."
    assert obj._city == "Portland"
    assert obj._state == "OR"
    assert obj._zip == 97035

    # Capitalization Test
    o2 = Records.Address("1 st.", "medford", "or", 97222)
    assert o2._street == "1 St."
    assert o2._city == "Medford"
    assert o2._state == "OR"
    assert o2._zip == 97222


def test_copy_constructor(setup):
    obj = Records.Address(setup)
    assert obj._street == "10 Main St."
    assert obj._city == "Portland"
    assert obj._state == "OR"
    assert obj._zip == 97035


# __str__ exception testing
def test_str_raises_exception(setup):
    obj = Records.Address()
    with pytest.raises(ValueError):
        print(obj)


def test_eq_ne(setup):
    a = Records.Address(setup)
    assert a == setup
    a.city = "test_city"
    assert a != setup

def test_eq_raises_exception(setup):
    with pytest.raises(ValueError):
        if (setup == 2):
            print()


# getters/setters testing
def test_getters(setup):
    assert setup.street == "10 Main St."
    assert setup.city == "Portland"
    assert setup.state == "OR"
    assert setup.zip == 97035

def test_setters(setup):
    setup.street = "main st."
    setup.city = "medford"
    setup.state = "ca"
    setup.zip = "22990"
    assert setup._street == "Main St."
    assert setup._city == "Medford"
    assert setup._state == "CA"
    assert setup._zip == 22990
    setup.street = "\t\tMain st."
    assert setup._street == "Main St."
    setup.city = "\n\nPortland"
    assert setup.city == "Portland"



def test_setters_raise_exceptions(setup):
    with pytest.raises(ValueError) as e:
        setup.state = "oregon"
    assert str(e.value) == "Invalid input when setting state"

    with pytest.raises(ValueError) as e:
        setup.zip = "test"
    assert str(e.value) == "Invalid input when setting zip"

    with pytest.raises(ValueError) as e:
        setup.zip = "1"
    assert str(e.value) == "Invalid input when setting zip"

    with pytest.raises(ValueError) as e:
        setup.zip = 1234
    assert str(e.value) == "Invalid input when setting zip"
    