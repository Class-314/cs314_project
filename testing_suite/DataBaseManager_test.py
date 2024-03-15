import pytest
import os
import sys
sys.path.append("..")
from DataBaseManager import *
# from unittest.mock import patch, mock_open


#________________________ Constructor  Methods   ____________________#

def test_init():


    # Instantiate the DatabaseManager class
    db_manager = DatabaseManager()

    # # Assert that the methods were called during initialization
    # assert db_manager.IDs # Assuming IDs is modified by load_IDs
    # assert db_manager.directory # Assuming directory is modified by load_directory
    # # assert db_manager.SR_count == 0 # Assuming SR_count is modified by load_SR_count








#____________________ getter methods ____________________#



#get provider method tests

def test_get_P_record_valid_ID():
    pass

def test_get_P_record_invalid_ID():
    pass



#get member  method tests

def test_get_M_record_valid_ID():
    pass

def test_get_M_record_invalid_ID():
    pass



#get service directory entry method tests

def test_get_directory_service_valid_ID():
    pass

def test_get_directory_service_invalid_ID():
    pass


#____________________ eddit methods ____________________#











#____________________ add methods ____________________#







#____________________ remove methods ____________________#


"""
# Mock the file content for load_IDs, load_directory, and load_SR_count
mocked_file_content = "mocked content"

@patch("builtins.open", mock_open(read_data=mocked_file_content))
def test_DatabaseManager_initialization():
    # Instantiate the DatabaseManager class
    db_manager = DatabaseManager()

    # Assert that the methods were called during initialization
    assert db_manager.IDs # Assuming IDs is modified by load_IDs
    assert db_manager.directory # Assuming directory is modified by load_directory
    assert db_manager.SR_count == 0 # Assuming SR_count is modified by load_SR_count



def test_load_IDs():
    # Mock the file content
    mocked_file_content = "key1 value1\nkey2 value2\nkey3 value3"
    mocked_open_function = mock_open(read_data=mocked_file_content)

    # Patch the open function to use the mocked version
    with patch("builtins.open", mocked_open_function):
        instance = YourClass() # Create an instance of your class
        instance.Registerd_IDs_relative_path = "path/to/your/file.txt" # Set the file path
        instance.IDs = {} # Initialize the IDs dictionary

        # Call the method under test
        result = instance.load_IDs()

        # Assert that the method returns True
        assert result is True

        # Assert that the IDs dictionary contains the expected keys
        assert "key1" in instance.IDs
        assert "key2" in instance.IDs
        assert "key3" in instance.IDs



"""
