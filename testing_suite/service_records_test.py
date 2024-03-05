import pytest
import sys
import datetime
sys.path.append("..")
import Records


# pytest fixture just gives us a default object to work with in the other tests
@pytest.fixture
def s_obj():
    s = Records.ServiceRecord(123123, 123456789, 987654321, "2-23-2024", "dietitian", "199.99")
    return s

@pytest.fixture
def sc_obj():
    s = Records.ServiceRecord(111111, 999999999, 777777777, "10-11-2012", "some comments", "nutritionist", "69.99")
    return s

def test_init_exceptions():
    with pytest.raises(ValueError):
        p = Records.ProviderRecord("a", "b")
    with pytest.raises(ValueError):
        p = Records.ProviderRecord("a", "b", "c")
    with pytest.raises(ValueError):
        p = Records.MemberRecord(1,2,3,4,5,6,7)


def test_default_constructor():
    sr = Records.ServiceRecord()
    assert sr._service_code == None
    assert sr._mID == None
    assert sr._pID == None
    assert sr._comments == None
    assert sr._date_provided == None
    assert sr._name == None
    assert sr._fee == None
    curr_time = datetime.datetime.now().replace(microsecond=0)
    curr_time = curr_time.strftime("%m-%d-%Y %H:%M:%S")
    assert sr._current_datetime == curr_time




def test_copy_constructor(s_obj, sc_obj):
    sr = Records.ServiceRecord(s_obj)
    assert sr._name == s_obj._name
    assert sr._fee == s_obj._fee
    assert sr._service_code == s_obj._service_code
    assert sr._mID == s_obj._mID
    assert sr._pID == s_obj._pID
    assert sr._comments == s_obj._comments
    assert sr._comments == None
    assert sr._date_provided == s_obj.date_provided
    assert sr._current_datetime == s_obj.current_datetime
    sr = Records.ServiceRecord(sc_obj)
    assert sr._name == sc_obj._name
    assert sr._fee == sc_obj._fee
    assert sr._service_code == sc_obj._service_code
    assert sr._mID == sc_obj._mID
    assert sr._pID == sc_obj._pID
    assert sr._comments == sc_obj._comments
    assert sr._date_provided == sc_obj.date_provided
    assert sr._current_datetime == sc_obj.current_datetime
    assert sr._comments != None


def test_copy_constructor_exceptions(sc_obj):
    inputs = [1, "test", 3.14]
    sr = Records.MemberRecord()
    for i in inputs:
        with pytest.raises(ValueError):
            sr._copy_constructor(i)


def test_param_constructor():
    sr = Records.ServiceRecord(123123, 123456789, 987654321, "1-1-2025", "some comments", "service name", "201.99")
    assert sr._name == "service name"
    assert sr._fee == "201.99"
    assert sr._service_code == 123123
    assert sr._pID == 123456789
    assert sr._mID == 987654321
    assert sr._comments == "some comments"
    assert sr._date_provided == "01-01-2025"
    curr_time = datetime.datetime.now().replace(microsecond=0)
    curr_time = curr_time.strftime("%m-%d-%Y %H:%M:%S")
    assert sr._current_datetime == curr_time

    sr = Records.ServiceRecord(666666, 999999999, 111111111, "12-12-1999", "service", "199.99")
    assert sr._name == "service"
    assert sr._fee == "199.99"
    assert sr._service_code == 666666
    assert sr._pID == 999999999
    assert sr._mID == 111111111
    assert sr._comments == None
    assert sr._date_provided == "12-12-1999"
    curr_time = datetime.datetime.now().replace(microsecond=0)
    curr_time = curr_time.strftime("%m-%d-%Y %H:%M:%S")
    assert sr._current_datetime == curr_time


def test_eq_ne(s_obj, sc_obj):
    sr = Records.ServiceRecord(s_obj)
    assert sr == s_obj
    sr.mID = 121212121
    assert sr != s_obj
    sr = Records.ServiceRecord(sc_obj)
    assert sr == sc_obj
    sr.pID = 676767555
    assert sr != sc_obj

def test_eq_ne_exceptions(s_obj):
    inputs = [1, "test", 3.14]
    for i in inputs:
        with pytest.raises(ValueError):
            if (s_obj == i):
                print()
        with pytest.raises(ValueError):
            if (s_obj != i):
                print()


def test_convert_date(s_obj):
    test_date = s_obj.convert_date("9-5-2020")
    assert test_date == "09-05-2020"

def test_convert_date_exceptions(s_obj):
    inputs = [1, "13-5-2020", "-1-5-2020", "2", "12-34-2020", "12--1-2020", "12-20-00000", "12-20-99999", 1234, "test"]
    for i in inputs:
        with pytest.raises(ValueError):
            s_obj.convert_date(i)