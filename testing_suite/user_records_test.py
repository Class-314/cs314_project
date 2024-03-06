
import pytest
import sys
sys.path.append("..")
import Records


# pytest fixture just gives us a default object to work with in the other tests
@pytest.fixture
def a_obj():
    a = Records.Address("10 Main St.", "Portland", "OR", "97035")
    return a

@pytest.fixture
def u_obj(a_obj):
    u = Records.UserRecord("Richard Simmons", 123456789, a_obj)
    return u


def test_init_exceptions():
    with pytest.raises(ValueError):
        u = Records.UserRecord("a", "b")
    with pytest.raises(ValueError):
        u = Records.UserRecord("a", "b", "c", "d")
    with pytest.raises(ValueError):
        u = Records.UserRecord(1,2,3,4,5,6,7)



def test_default_constructor():
    ur = Records.UserRecord()
    assert ur._name == None
    assert ur._ID == None


def test_copy_constructor(u_obj, a_obj):
    ur = Records.UserRecord(u_obj)
    assert ur._name == "Richard Simmons"
    assert ur._ID == 123456789
    # Inheritance testing, not strictly necessary
    ad = Records.Address(u_obj)
    assert ad == a_obj
    # assert ur._street == "10 Main St."
    # assert ur._city == "Portland"
    # assert ur._state == "OR"
    # assert ur._zip == 97035

def test_copy_constructor_exceptions(u_obj, a_obj):
    u = Records.UserRecord()
    with pytest.raises(ValueError):
        u._copy_constructor(1)
    with pytest.raises(ValueError):
        u._copy_constructor("test")
    with pytest.raises(ValueError):
        u._copy_constructor(3.14)


def test_param_constructor(a_obj):
    # param with address object
    ur = Records.UserRecord("Bill Gates", 999999123, a_obj)
    assert ur._name == "Bill Gates"
    assert ur._ID == 999999123
    ad = Records.Address(ur)
    assert ad == a_obj
    
    # param with individual fields
    ur = Records.UserRecord("Alan Turing", 123123123, "1 main st.", "portland", "or", 97202)
    assert ur._name == "Alan Turing"
    assert ur._ID == 123123123
    ad = Records.Address(ur)
    ad2 = Records.Address("1 main st.", "portland", "OR", 97202)
    assert ad == ad2

    # param with uncapitalized input field and string ID
    ur = Records.UserRecord("jake smith", "111111123", a_obj)
    assert ur._name == "Jake Smith"
    assert ur._ID == 111111123


def test_eq_ne(u_obj):
    ur = Records.UserRecord(u_obj)
    assert ur == u_obj
    ur.name = "no"
    assert ur != u_obj
    ur = Records.UserRecord(u_obj)
    ur.ID = 585858123
    assert ur != u_obj

def test_eq_ne_exceptions(u_obj, a_obj):
    inputs = [1, 3.1419, a_obj]
    for i in inputs:
        with pytest.raises(ValueError):
            if (u_obj == i):
                print()
        with pytest.raises(ValueError):
            if (u_obj != i):
                print()


def test_setters(u_obj):
    u_obj.name = "richard hendrix"
    assert u_obj.name == "Richard Hendrix"
    u_obj.ID = "808080123"
    assert u_obj.ID == 808080123

def test_setters_exceptions(u_obj):
    inputs = [1, 12312, 1231234, 123123, "1", "12312", "12341234"]

    with pytest.raises(ValueError):
        u_obj.name = 1
    
    for i in inputs:
        print(i) #if you want to see print statements in the test, use the -s flag: pytest -s
        with pytest.raises(ValueError):
            u_obj.ID = i
    
    # with pytest.raises(ValueError):
    #     u_obj.ID = 1
    # with pytest.raises(ValueError):
    #     u_obj.ID = 12312
    # with pytest.raises(ValueError):
    #     u_obj.ID = 1231234
    # with pytest.raises(ValueError):
    #     u_obj.ID = "1"
    # with pytest.raises(ValueError):
    #     u_obj.ID = "12312"
    # with pytest.raises(ValueError):
    #     u_obj.ID = "12341234"
    # with pytest.raises(ValueError):
    #     u_obj.ID = None