# Imports
# Import ProviderRecord
# Import MemberRecord
# Import DatabaseMgr
from Records import *

class ClientInterface:
    # Initialize the ClientInterface with optional member and provider IDs
    def __init__(self, member_ids=None, provider_ids=None):
        self.current_provider = None  # Instance of ProviderRecord for the current provider
        self.current_member = None  # Instance of MemberRecord for the current member
        # self.DB_mgr = DatabaseMgr()  # Instance of Database Manager for DB operations


    # display the menu choices
    def display_menu(self, menu_type):
        menu_functions = {
            "provider": self.provider_menu,
            "manager": self.manager_menu,
        }
        menu_function = menu_functions.get(menu_type, lambda: print("Invalid menu type"))
        menu_function()
    
    def display_provider_menu(self):
        # Enter and verify provider ID 
        if not self.verify_provider_input():
            print("Exiting to main menu.")
            return
        
        # Enter and verify member ID
        if not self.verify_member_input():
            print("Exising to main menu.")
            return

        # If provider and member ID are provided, show menu. 
        while True:
            # print menu
            print("\nProvider Menu")
            
            # print current provder

            # print current member

            # print provider menu
            print("0. Return to Main Menu")
            print("1. Display Provider Information")
            print("2. Display Member Information")
            print("3. Display Service Record Directory")
            print("4. Enter Service Record")
            print("5. Change Current Member ID")
            print("6. Change Current Provider ID")
            choice = input("\nChoose an option: ")

            if choice == '1':
                print("\nDisplay Provider Information")
            elif choice == '2':
                print("\nDisplay Member Information")
            elif choice == '3':
                print("\nDisplay Member Information")
            elif choice == '4':
                print("\nDisplay Service Record Directory")                
            elif choice == '0':
                break
            else:
                print("\nInvalid option. Please try again.")

    def manager_menu(self):
            while True:
                print("\nManager Menu")
                print("1. Manage Reports")
                print("2. Manage Users")
                print("9. Return to Main Menu")
                choice = input("Choose an option: ")

                if choice == '1':
                    # Implement view reports functionality
                    print("\nViewing Reports")
                elif choice == '2':
                    # Implement manage users functionality
                    print("\nManaging Users")
                elif choice == '9':
                    break  # Exit loop to return to the main menu
                else:
                    print("\nInvalid option. Please try again.")
    
    # Verify user input for provider id
    def verify_provider_input(self):
        while True:
            user_input = input("\nEnter Provider ID: ")
            if user_input.isdigit() and len(user_input) == 9:
                temp_provider = self.verify_provider(user_input)
                if temp_provider:
                    self.update_current_provider(temp_provider)
                    return True
                else:
                    print("Provider ID not found.")
            else:
                print("Error: Provider ID must be an integer and 9 digits long.")

            try_again = input("Do you want to try again? (y/n): ").lower()
            if try_again != 'y':
                return False
    
    # Verify provider's ID against the database
    def verify_provider(self, pID):
        return self.DB_mgr._get_provider(pID)
    
    # Update the current provider based on the given provider ID
    def update_current_provider(self, temp_provider):
        # Update current provider logic here
         self.current_provider = ProviderRecord.copy_constructor(temp_provider)
    
    # Verify user input for member id
    def verify_member_input(self):
        while True:
            user_input = input("\nEnter Member ID: ")
            if user_input.isdigit() and len(user_input) == 9:
                temp_member = self.verify_member(user_input)
                if temp_member:
                    self.update_current_member(temp_member)
                    return True
                else:
                    print("Member ID not found.")
            else:
                print("Error: Member ID must be an integer and 9 digit long.")

            try_again = input("Do you want to try again? (y/n): ").lower()
            if try_again != 'y':
                return False
    
    # Verify member's ID against the database
    def verify_member(self, mID):
        return self.DB_mgr.verify_member(mID)
    
    # Set the current member based on the given member ID
    def update_current_member(self, temp_member):
        self.current_member = MemberRecord.copy_constructor(temp_member)
    '''
    
    # Confirm if a service code exists in the system
    def verify_service(self, service_code):
        # Implement service verification logic here
        return self.DB_mgr.verify_service(service_code)

    # Return the record of the currently selected member
    def get_current_member(self):
        return self.current_member

    # Retrieve the currently active provider's record
    def get_current_provider(self):
        return self.current_provider

    # Log a service provided by the current provider to the current member
    def write_service(self, to_write):
        # Implement service logging here
        pass

    # Refresh the member directory, possibly re-fetching from the database
    def update_member_directory(self):
        # Implement member directory update logic here
        pass

    # Updates the provider directory with the latest data
    def update_provider_directory(self):
        # Implement provider directory update logic here
        pass

    # Refresh the service directory, ensuring it has the current offerings
    def update_service_directory(self):
        # Implement service directory update logic here
        pass
    '''
# Note: This code assumes the existence of a DatabaseMgr class with methods like
# verify_provider, verify_member, verify_service, get_member_record, get_provider_record.

