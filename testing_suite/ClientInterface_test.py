import pytest
import sys
sys.path.append("..")
from ClientInterface import *
from Records import *
from unittest.mock import patch

@pytest.fixture
def ci():
    ci = ClientInterface()
    return ci

@pytest.fixture
def member():
    m_a = Address("Test Street", "Test City", "OR", 99999)
    m = MemberRecord("Test Nmae", 100112136, m_a)
    return m

@pytest.fixture
def provider():
    m_p = Address("9587 Lopez Parks Suite 985", "Thomasland", "WV", 48610)
    p = ProviderRecord("Abigail Aguirre", 101027954, m_p)
    return p

# Unit Test 1 - Verify valid member ID is recognized.
def test_verify_member_exists(ci):
    assert ci.verify_member_exists(100112136) == True
    assert ci.verify_member_exists(111111111) == False

# Unit Test 2 - Ensure valid provider ID is acknowledged.
def test_verify_provider_exists(ci):
    assert ci.verify_provider_exists(101027954) == True
    assert ci.verify_provider_exists(111111111) == False

# Unit Test 3 - Check correct member details are fetched by ID.
def test_get_member(ci, member):
    m = ci.get_member(100112136)
    assert m.name == member.name
    assert m.ID == member.ID
    assert m.street == member.street
    assert m.city == member.city
    assert m.state == member.state
    assert m.zip == member.zip
    assert m.is_suspended == member.is_suspended

# Unit Test 4 - Validate fetching provider by ID returns accurate details.
def test_get_provider(ci, provider):
    p = ci.get_provider(101027954)
    assert p.name == provider.name
    assert p.ID == provider.ID
    assert p.street == provider.street
    assert p.city == provider.city
    assert p.state == provider.state
    assert p.zip == provider.zip
    assert p.num_consultations == provider.num_consultations
    assert p.total_payment == provider.total_payment

# Unit Test 5 - Test valid provider ID input for verification process.
def test_verify_provider_input_valid(ci):
    with patch('builtins.input', side_effect=['101027954']) as mock_input:
        result = ci.verify_provider_input()
        assert result == True
        mock_input.assert_called_once_with("\nEnter Provider ID: ")

# Unit Test 6 - Assess valid member ID input during verification.
def test_verify_provider_input_invalid_then_valid(ci):
    with patch('builtins.input', side_effect=['12345678', 'y', '101027954']) as mock_input:
        result = ci.verify_provider_input()
        assert result == True
        assert mock_input.call_count == 3

# Unit Test 7 - Evaluate provider input handling for invalid format, then valid input.
def test_verify_provider_input_invalid_then_exit(ci):
    with patch('builtins.input', side_effect=['123', 'n']) as mock_input:
        result = ci.verify_provider_input()
        assert result == False
        assert mock_input.call_count == 2

# Unit Test 8 - Verify provider input handling for invalid format, then choose to exit.
def test_verify_provider_input_non_digit_then_exit(ci):
    with patch('builtins.input', side_effect=['abcdefghi', 'n']) as mock_input:
        result = ci.verify_provider_input()
        assert result == False
        assert mock_input.call_count == 2

# Unit Test 9 - Test provider input handling for completely invalid input and exit choice.
def test_verify_member_input_valid(ci):
    with patch('builtins.input', side_effect=['100112136']) as mock_input:
        result = ci.verify_member_input()
        assert result == True
        mock_input.assert_called_once_with("\nEnter Member ID: ")

# Unit Test 10 - Assess member input verification with valid input after invalid attempts.
def test_verify_member_input_invalid_then_valid(ci):
    with patch('builtins.input', side_effect=['12345678', 'y', '100112136']) as mock_input:
        result = ci.verify_member_input()
        assert result == True
        assert mock_input.call_count == 3

# Unit Test 11 - Verify member input handling for invalid format, then exit decision.
def test_verify_member_input_invalid_then_exit(ci):
    with patch('builtins.input', side_effect=['123', 'n']) as mock_input:
        result = ci.verify_member_input()
        assert result == False
        assert mock_input.call_count == 2

# Unit Test 12 - Test non-existent member ID handling and subsequent exit.
def test_verify_member_input_non_existent_then_exit(ci):
    with patch('builtins.input', side_effect=['123456789', 'n']), patch.object(ci, 'verify_member_exists', return_value=False):
        result = ci.verify_member_input()
        assert result == False

# Unit Test 13 - Verify updating current provider updates internal state.
def test_update_current_provider(ci, provider):
    ci.update_current_provider(provider)
    assert ci.current_provider == provider, "Current provider should be updated to the new provider."

# Unit Test 14 - Verify updating current member updates internal state.
def test_update_current_member(ci, member):
    ci.update_current_member(member)
    assert ci.current_member == member, "Current member should be a MemberRecord instance."

# Unit Test 15 - Verify retrieval of the current provider's record.
def test_get_current_provider(ci, provider):
    ci.current_provider = provider
    retrieved_provider = ci.get_current_provider()
    assert retrieved_provider == provider, "Should return the current provider record."

# Unit Test 16 - Verify retrieval of the current member's record.
def test_get_current_member(ci, member):
    ci.current_member = member
    retrieved_member = ci.get_current_member()
    assert retrieved_member == member, "Should return the current member record."

# unit test 17 - Confirms Provider Report generation for a valid Provider
def test_generate_provider_report_confirmed(ci, provider):
    with patch('builtins.input', side_effect=[str(provider.ID), 'y']), \
         patch.object(ci, 'verify_provider_exists', return_value=True), \
         patch.object(ci, 'get_provider', return_value=provider), \
         patch.object(ci.DB_mgr, 'write_provider_report') as mock_write_report:
        result = ci.generate_provider_report()
        assert result == True
        mock_write_report.assert_called_once_with(str(provider.ID))

# unit test 18 - Test declines Report generation after entering a valid provider ID
def test_generate_provider_report_declined(ci, provider):
    with patch('builtins.input', side_effect=[str(provider.ID), 'n']):  # 'n' to decline
        result = ci.generate_provider_report()
        assert result == False

# unit test 19 - Confirms report generation for a valid member
def test_generate_member_report_confirmed(ci, member):
    with patch('builtins.input', side_effect=[str(member.ID), 'y']), \
         patch.object(ci, 'verify_member_exists', return_value=True), \
         patch.object(ci, 'get_member', return_value=member), \
         patch.object(ci.DB_mgr, 'write_member_report') as mock_write_report:
        result = ci.generate_member_report()
        assert result == True
        mock_write_report.assert_called_once_with(str(member.ID))

# unit test 20 - declines report generation after entering a valid member ID
def test_generate_member_report_declined(ci, member):
    with patch('builtins.input', side_effect=[str(member.ID), 'n']):  # 'n' to decline
        result = ci.generate_member_report()
        assert result == False