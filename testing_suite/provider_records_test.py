
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
def p_obj(a_obj):
    p = Records.ProviderRecord("Richard Simmons", 123456123, a_obj)
    return p


def test_init_exceptions():
    with pytest.raises(ValueError):
        p = Records.ProviderRecord("a", "b")
    with pytest.raises(ValueError):
        p = Records.ProviderRecord("a", "b", "c", "d")
    with pytest.raises(ValueError):
        p = Records.MemberRecord(1,2,3,4,5,6,7)



def test_default_constructor():
    pr = Records.ProviderRecord()
    assert pr._num_consultations == 0
    assert pr._total_payment == 0.00


def test_copy_constructor(p_obj, a_obj):
    pr = Records.ProviderRecord(p_obj)
    assert pr._num_consultations == p_obj._num_consultations
    assert pr._total_payment == p_obj._total_payment

    p_obj._num_consultations = 10
    p_obj._total_payment = 199.99
    pr = Records.ProviderRecord(p_obj)
    assert pr._num_consultations == 10
    assert pr._total_payment == 199.99


def test_copy_constructor_exceptions(p_obj, a_obj):
    inputs = [1, "test", 3.14, a_obj]
    pr = Records.ProviderRecord()
    for i in inputs:
        with pytest.raises(ValueError):
            pr._copy_constructor(i)


def test_param_constructor(a_obj):
    pr = Records.ProviderRecord("Dick Nixon", 999999123, a_obj)
    assert pr._name == "Dick Nixon"
    assert pr._ID == 999999123
    assert pr._num_consultations == 0
    assert pr._total_payment == 0
    a = Records.Address(pr)
    assert a == a_obj

    pr = Records.ProviderRecord("\n\n\n\nDick Nixon", 999999123, a_obj)
    assert pr._name == "Dick Nixon"

def test_setters(p_obj):
    assert p_obj._num_consultations == 0
    assert p_obj._total_payment == 0.0
    p_obj.num_consultations = 99
    assert p_obj._num_consultations == 99
    p_obj.total_payment = 999.99
    assert p_obj._total_payment == 999.99
    p_obj.name = "\t\t\tName"
    assert p_obj._name == "Name"

def test_setters_exceptions(p_obj, a_obj):
    inputs = ["1", "test", a_obj]
    for i in inputs:
        with pytest.raises(ValueError):
            p_obj.num_consultations = i
        with pytest.raises(ValueError):
            p_obj.total_payment = i

    with pytest.raises(ValueError):
        p_obj.num_consultations = 3.14
    with pytest.raises(ValueError):
        p_obj.total_payment = 9

def test_add_consultation(p_obj):
    assert p_obj.num_consultations == 0
    p_obj.add_consultation()
    assert p_obj.num_consultations == 1
    for i in range(10):
        p_obj.add_consultation()
    assert p_obj.num_consultations == 11

def test_add_payment(p_obj):
    assert p_obj.total_payment == 0.0
    p_obj.add_payment(90.00)
    p_obj.add_payment(0.10)
    p_obj.add_payment(9.90)
    assert p_obj.total_payment == 100.00

def test_add_payment_exceptions(p_obj, a_obj):
    assert p_obj.total_payment == 0.0
    with pytest.raises(ValueError):
        p_obj.add_payment("test")
    with pytest.raises(TypeError):
        p_obj.add_payment(a_obj)