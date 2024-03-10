# Imports
from datetime import datetime
from Records import *
#from DataBaseManager import * 

class ClientInterface:
    # Initialize the ClientInterface with optional member and provider IDs
    def __init__(self, member_ids=None, provider_ids=None):
        self.current_provider = None  # Instance of ProviderRecord for the current provider
        self.current_member = None  # Instance of MemberRecord for the current member
        # self.DataBaseManager = DatabaseMgr()  # Instance of Database Manager for DB operations

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
            
            # print current provider
            if self.current_provider is not None:
                print(f"\nCurrent Provider: {self.current_provider}")
            else:
                print("\nCurrent Provider: Not available")

            # print current member
            if self.current_member is not None:
                print(f"\nCurrent Member: {self.current_member}")
            else:
                print("\nCurrent Member: Not available")

            # print provider menu
            print("0. Return to Main Menu")
            print("1. Display Provider Information")
            print("2. Display Member Information")
            print("3. Display Service Record Directory")
            print("4. Enter Service Record")
            print("5. Change Current Member ID")
            print("6. Change Current Provider ID")
            choice = input("\nChoose an option: ")
            # choice 1
            if choice == '1':
                print("\nDisplay Provider Information")
                if self.current_provider is not None:
                    print(f"\nCurrent Provider: {self.current_provider}")
                else:
                    print("\nCurrent Provider: Not available")
            # choice 2
            elif choice == '2':
                print("\nDisplay Member Information")
                if self.current_member is not None:
                    print(f"\nCurrent Member: {self.current_member}")
                else:
                    print("\nCurrent Member: Not available")
            # choice 3
            elif choice == '3':
                print("\nDisplay Service Record Directory")
                self.display_service_record()
            # choice 4
            elif choice == '4':
                print("\nEnter Service Record")
                # self.write_service()
            #choice 5
            elif choice == '5':
                print("\nChange Current Member ID")
                # make sure the member id is valid

                # make sure the current member id is changed

                # else exit to main menu
            #choice 6
            elif choice == '6':
                print("\nChange Current Provider ID")
                # make sure the provider id is valid

                # make sure the current provider id is changed

                # else exit to main menu
            # choice 0 
            elif choice == '0':
                break
            else:
                print("\nInvalid option. Please try again.")

    def manager_menu(self):
            while True:
                print("0. Return to Main Menu")
                print("\nManager Menu")
                print("1. Manage Reports")
                print("2. Manage Users")
                choice = input("Choose an option: ")

                if choice == '1':
                    # Implement view reports functionality
                    print("\nViewing Reports")
                elif choice == '2':
                    # Implement manage users functionality
                    print("\nManaging Users")
                elif choice == '0':
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
    
    # Verify provider's ID against the database and get provider object
    def verify_provider(self, pID):
        return self.DataBaseManager.get_provider_record(pID)
    
    # Update the current provider based on the given provider ID
    def update_current_provider(self, temp_provider):
        # Update current provider logic here
         self.current_provider = ProviderRecord.copy_constructor(temp_provider)
    
    # Retrieve the current provider's record
    def get_current_provider(self):
        return self.current_provider
    
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
    
    # Verify member's ID against the database and get member object
    def verify_member(self, mID):
        return self.DataBaseManager.get_member_record(mID)
    
    # Set the current member based on the given member ID
    def update_current_member(self, temp_member):
        self.current_member = MemberRecord.copy_constructor(temp_member)

    # Return the record of the current member
    def get_current_member(self):
        return self.current_member
    
    # Display the service record directory
    def display_service_record(self):
        return self.DataBaseManager.display_service_directory()
    
    # Confirm if a service code exists in the system
    # def verify_service(self):
    
    # Log a service provided by the current provider to the current member
    def write_service(self):
        # Get Service Details 
        while True:
            # Reinitialize variables at the start of the loop for retry logic
            service_name = None
            service_code = None

            while True:
                service_name = input("\nEnter the Service Name: ")
                if len(service_name) != 23:
                    print("Error: The service name must be exactly 23 characters.")
                else:
                    break  # Exit loop if service name meets the criteria

                if input("Do you want to try again? (y/n): ").lower() != 'y':
                    print("Exiting service name entry.")
                    return  # Exit the method if the user does not want to try again

            while True:
                service_code_input = input("\nEnter the Service Code: ")
                if service_code_input.isdigit() and len(service_code_input) == 6:
                    service_code = int(service_code_input)  # Convert to int if validation passes
                    break  # Exit loop if service code meets the criteria
                else:
                    print("Error: The service code must be a 6 digit integer.")

                if input("Do you want to try again? (y/n): ").lower() != 'y':
                    print("Exiting service code entry.")
                    return  # Exit the method if the user does not want to try again

            # Check with the database manager if the service code already exists
            if self.DataBaseManager.is_service(service_name, service_code):
                break  # Service code is valid and does not already exist, break out of the main loop
            else:
                print("Error: The service code already exists in the database. Please enter a new service name and service code.")

        while True:
            try:
                service_fee_input = input("\nEnter the Service Fee: ")
                service_fee = float(service_fee_input)
                if service_fee < 0 or service_fee >= 1000000:
                    raise ValueError("Service fee must be between $0.00 and $999,999.99.")
                break
            except ValueError as e:
                print(f"Invalid input for service fee: {e}. Please try again.")

        # Assuming current_member and current_provider are already set
        service_member = self.current_member
        service_provider = self.current_provider

        # Get user input for service comment and make sure it's under 100 characters
        while True:
            service_comment = input("\nEnter the Service Comment: ")
            if len(service_comment) <= 100:
                break
            else:
                print("Error: The service comment must be 100 characters or less.")

        # Get current time and date in format (MM-DD-YYYY HH:MM:SS)
        service_date_current = datetime.now().strftime("%m-%d-%Y %H:%M:%S")

        # Get user input for service date in format (MM-DD-YYYY)
        while True:
            service_date_str = input("\nEnter the Service Date (MM-DD-YYYY): ")
            try:
                # Attempt to convert the input string to a datetime object
                datetime.strptime(service_date_str, "%m-%d-%Y")
                break  # Break the loop if conversion succeeds
            except ValueError:
                print("The date entered is invalid or does not match the format MM-DD-YYYY. Please try again.")
        try:
                # Create ServiceRecord object. Adjust according to your ServiceRecord class constructor or factory method
                temp_service = ServiceRecord(
                    service_name,
                    service_code,
                    service_fee,
                    service_member,  
                    service_provider,  
                    service_comment,
                    service_date_current,
                    service_date_str
                )

                # Attempt to update the service directory via the Database Manager
                update_success = self.DataBaseManager.update_service_directory(temp_service)
                
                if update_success:
                    print("Service successfully updated in the directory.")
                    return True
                else:
                    print("Failed to update service in the directory.")
                    return False
        except Exception as e:
                print(f"An error occurred while writing service: {e}")
                return False
    '''
    # Refresh the member directory
    def update_member_directory(self):
        # Implement member directory update logic here -> sending to database manager
        pass

    # Updates the provider directory with the latest data 
    def update_provider_directory(self):
        # Implement provider directory update logic here -> sending to database manager
        pass

    # Refresh the service directory, ensuring it has the current offerings
    def update_service_directory(self):
        # Implement service directory update logic here -> sending to database manager
        pass

    '''