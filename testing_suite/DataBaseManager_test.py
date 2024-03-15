from DataBaseManager import *
import pytest
from unittest.mock import patch, mock_open


@pytest.fixture
def address():
    return Address("Sw carrot RD", "Clackamas", "OR", "97015")

@pytest.fixture
def provider_record(address):
    return ProviderRecord("George Bush", 888888888, address)

@pytest.fixture
def member_record(address):
    return MemberRecord("Jeb Bush", 999999999, address)


@pytest.fixture
def service_record(member_record, provider_record):
    return ServiceRecord("123456", 888888888, 999999999, "01-23-2024", "destroyer of worlds", 123)

#________________________ Constructor  Methods   ____________________#

def test_instantiation_DBManager():
    try:
        db_manager = DatabaseManager()
    except ValueError:
        pytest.fail("ValueError occurred during instantiation")
    else:
        assert isinstance(db_manager, DatabaseManager), "db_manager is not an instance of DatabaseManager"

#____________________ member record method tests ____________________#

def test_add_mmember_record(member_record):
    db_manager = DatabaseManager()

    assert db_manager.add_member_record(member_record), "Failed to add member record"
    assert db_manager.get_member_record(member_record), "Failed to get member record"
    assert db_manager.edit_member_record(member_record), "Failed to eddit member record"
    assert db_manager.remove_member_record(member_record), "Failed to remove record"


    assert db_manager.Hpytest_remove_latest_entry(), "Failed to remove latest ID add to Database"

#____________________ provider record method tests ____________________#

def test_add_pmember_record(provider_record):
    db_manager = DatabaseManager()

    assert db_manager.add_provider_record(provider_record), "Failed to add  record"
    assert db_manager.get_provider_record(provider_record), "Failed to get member record"
    assert db_manager.edit_provider_record(provider_record), "Failed to eddit member record"
    assert db_manager.remove_provider_record(provider_record), "Failed to remove record"

    assert db_manager.Hpytest_remove_latest_entry(), "Failed to remove latest ID add to Database"

#____________________ service record method tests ____________________#

def test_sr_record(provider_record,member_record,service_record):
    db_manager = DatabaseManager()

    assert db_manager.add_provider_record(provider_record), "Failed to add member record"
    assert db_manager.add_member_record(member_record), "Failed to add provider record"

    assert db_manager.add_service_record(service_record)

    assert db_manager.remove_provider_record(provider_record), "Failed to remove record"
    assert db_manager.remove_member_record(member_record), "Failed to remove record"

    assert db_manager.Hpytest_remove_latest_entry(), "Failed to remove latest ID add to Database"
    assert db_manager.Hpytest_remove_latest_entry(), "Failed to remove latest ID add to Database"

    assert db_manager.Hpytest_remove_latest_SR_record(service_record), "Failed to remove remove SR file and de-increment SR file count"

def test_directory():
    pass