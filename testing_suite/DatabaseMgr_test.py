import pytest
import sys
from unittest.mock import patch
import io
sys.path.append("..")
import DatabaseMgr

#constructor testing
def test_default_constructor():
    obj = DatabaseMgr.DatabaseMgr()

    assert obj._service_dir == []
    assert obj._active_members == []
    assert obj._active_providers == []

def test_copy_constructor():
    obj = DatabaseMgr.DatabaseMgr()
    obj._service_dir = ['Service1', 'Service2', 'Service3']
    obj._active_members = ['123456', '654321']
    obj._active_providers = ['123456789', '987654321']

    obj2 = DatabaseMgr.DatabaseMgr._copy_constructor(obj)
    
    assert obj2._service_dir == obj._service_dir
    assert obj2._active_members == obj._active_members
    assert obj2._active_providers == obj._active_providers
    
def test_init_raises_exceptions():
    with pytest.raises(ValueError) as e:
        obj = DatabaseMgr.DatabaseMgr("non-object")
    assert str(e.value) == "Other is not of type DatabaseMgr in copy constructor"

    with pytest.raises(ValueError)as e:
        obj = DatabaseMgr.DatabaseMgr("arg1", "arg2")
    assert str(e.value) == "Incorrect number of arguments when initializing DatabaseMgr"

def test_display_service():
    obj = DatabaseMgr()
    obj._service_dir = ['Service1', 'Service2', 'Service3']

    # Use patch to mock the standard output
    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        # Call the _display_service method
        obj._display_service()

        # Get the printed output
        printed_output = fake_stdout.getvalue().strip()

    # Assert that the printed output matches the expected output
    expected_output = '\n'.join(obj._service_dir)
    assert printed_output == expected_output