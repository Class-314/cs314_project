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
def s_obj(a_obj):
    s = Records.ServiceRecord(123123, 123456789, 987654321, "2-23-2024")
    return s


def test_init_exceptions():
    with pytest.raises(ValueError):
        p = Records.ProviderRecord("a", "b")
    with pytest.raises(ValueError):
        p = Records.ProviderRecord("a", "b", "c")
    with pytest.raises(ValueError):
        p = Records.MemberRecord(1,2,3,4,5,6,7)