
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
def m_obj(a_obj):
    m = Records.MemberRecord("Richard Simmons", 123456123, a_obj)
    return m


def test_init_exceptions():
    with pytest.raises(ValueError):
        m = Records.MemberRecord("a", "b")
    with pytest.raises(ValueError):
        m = Records.MemberRecord("a", "b", "c", "d")
    with pytest.raises(ValueError):
        m = Records.MemberRecord(1,2,3,4,5,6,7)



def test_default_constructor():
    mr = Records.MemberRecord()
    assert mr._is_suspended == False


def test_copy_constructor(m_obj, a_obj):
    mr = Records.MemberRecord(m_obj)
    assert mr._is_suspended == False
    m_obj.suspend_membership()
    mr = Records.MemberRecord(m_obj)
    assert mr._is_suspended == True

def test_copy_constructor_exceptions(m_obj, a_obj):
    inputs = [1, "test", 3.14, a_obj]
    m = Records.MemberRecord()
    for i in inputs:
        with pytest.raises(ValueError):
            m._copy_constructor(i)


def test_param_constructor(a_obj):
    mr = Records.MemberRecord("Dick Nixon", 999999123, a_obj)
    assert mr._name == "Dick Nixon"
    assert mr._ID == 999999123
    assert mr._is_suspended == False
    a = Records.Address(mr)
    assert a == a_obj



def test_convert_status(m_obj):
    assert m_obj.convert_status() == "Active"
    m_obj._is_suspended = True
    assert m_obj.convert_status() == "Suspended"

def test_suspend_membership(m_obj):
    assert m_obj.is_suspended == False
    m_obj.suspend_membership()
    assert m_obj.is_suspended == True
    m_obj.activate_membership()
    assert m_obj.is_suspended == False

def test_setters(m_obj):
    assert m_obj.is_suspended == False
    m_obj.is_suspended = True
    assert m_obj.is_suspended == True

def test_setters_exceptions(m_obj, a_obj):
    inputs = [1, "2", 3.14, a_obj]
    for i in inputs:
        with pytest.raises(ValueError):
            m_obj.is_suspended = i