# Imports
from datetime import datetime
from Records import *
from DataBaseManager import * 

class ClientInterface:
    # Initialize the ClientInterface with optional member and provider IDs
    def __init__(self, member_ids=None, provider_ids=None):
        self.current_provider = None  # Instance of ProviderRecord for the current provider
        self.current_member = None  # Instance of MemberRecord for the current member
        # Instance of Database Manager for DB operations
        self.DB_mgr = DatabaseManager() 

    # display the menu choices
    def display_menu(self, menu_type):
        menu_functions = {
            "provider": self.provider_menu,
            "manager": self.manager_menu,
        }
        menu_function = menu_functions.get(menu_type, lambda: print("Invalid menu type"))
        menu_function()
    
    def provider_menu(self):
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
                # Call the verify_member_input method and check if the result is True
                if self.verify_member_input():
                    print("Successfully changed Member ID.")
                else:
                    # If verify_member_input returns False, indicate failure and exit to the main menu
                    print("Failed to change Member ID. Exiting to Main Menu.")
                    break
            # choice 6
            elif choice == '6':
                print("\nChange Current Provider ID")
                # Call the verify_provider_input method and check if the result is True
                if self.verify_provider_input():
                    print("Successfully changed Provider ID.")
                else:
                    # If verify_provider_input returns False, indicate failure and exit to the main menu
                    print("Failed to change Provider ID. Exiting to Main Menu.")
                    break
            # choice 0
            elif choice == '0':
                # Exit the loop/menu
                break
            else:
                print("\nInvalid option. Please try again.")

    def manager_menu(self):
            while True:
                print("0. Return to Main Menu")
                print("\nManager Menu")
                print("1. Manage Reports")
                print("2. Manage Operations")
                choice = input("Choose an option: ")

                if choice == '1':
                    # Implement view reports functionality
                    # Add sub-menu to choose what type of report
                    while True:
                        print("0. Return to Manager Menu")
                        print("\nViewing Reports")
                        print("1. Manage Provider Reports")
                        print("2. Manage Member Reports")
                        choice = input("Choose an option: ")
                        
                        if choice == '0':
                            # Break out and go back to last menu
                            break
                        elif choice == '1':
                            # do stuff here not ready
                            print("\nManage Provider Reports")
                        elif choice == '2':
                            # do stuff here not ready
                            print("\nManage Member Reports")
                        else:
                            print("\nInvalid option. Please try again.")
                elif choice == '2':
                    # Implement manage users functionality
                    while True:
                        print("0. Return to Manager Menu")
                        print("\nManaging Operations")
                        print("1. Manage Providers")
                        print("2. Manage Services")
                        print("3. Manage Members")
                        choice = input("Choose an option: ")
                        
                        if choice == '0':
                            # Break out and go back to last menu
                            break
                        elif choice == '1':

                            while True:
                                # Another sub menu for Remove/Add/Modify
                                print("0. Return to Operations Menu")
                                print("\nManaging Providers")
                                print("1. Remove Provider")
                                print("2. Add Provider")
                                print("3. Modify Provider")
                                choice = input("Choose an option: ")

                                if choice == '0':
                                    # Break out and go back to last menu
                                    break
                                elif choice == '1':
                                    # Remove 
                                    print("\nRemove Provider")
                                    id = input("Enter Provider ID: ")

                                    # Check if they even exist to remove                    
                                    if self.verify_provider_exists(id):
                                        try_again = ("\nProvider does not exist. Try again? (y/n): ")
                                        if try_again == 'y':
                                            continue
                                        else:
                                            break
                
                                    # then idk here remove it ill do it later
                                elif choice == '2':
                                    # Add a provider
                                    print("\nAdd Provider")

                                    # btw this is rough draft if its bad its ok to scrap

                                    # Collect the info for the Provider here

                                    input("Enter Provider everything: ")
                                    
                                elif choice == '3':
                                    # Modify 
                                    print("\Modify Provider")
                                    id = input("Enter Provider ID: ")
                                    # then update it

                        elif choice == '2':
                            
                            while True:
                                # Another sub menu for Remove/Add/Modify
                                print("0. Return to Operations Menu")
                                print("\nManaging Services")
                                print("1. Remove Service")
                                print("2. Add Service")
                                print("3. Modify Service")
                                choice = input("Choose an option: ")

                                if choice == '0':
                                    # Break out and go back to last menu
                                    break
                                elif choice == '1':
                                    # Remove 
                                    print("\nRemove Service")
                                    id = input("Enter Service ID: ")

                                    # Check if they even exist to remove                    
                                    if self.verify_service(id):
                                        try_again = ("\nService does not exist. Try again? (y/n): ")
                                        if try_again == 'y':
                                            continue
                                        else:
                                            break
                
                                    # then idk here remove it ill do it later
                                elif choice == '2':
                                    # Add a service
                                    print("\nAdd Service")
                                    # Collect the info for the Service here
                                    
                                    input("Enter Service everything: ")
                                    
                                elif choice == '3':
                                    # Modify
                                    print("\Modify Service")
                                    id = input("Enter Service ID: ")
                                    # then update it

                        elif choice == '3':

                            while True:
                                # Another sub menu for Remove/Add/Modify
                                print("0. Return to Operations Menu")
                                print("\nManaging Members")
                                print("1. Remove Member")
                                print("2. Add Member")
                                print("3. Modify Member")
                                choice = input("Choose an option: ")

                                if choice == '0':
                                    # Break out and go back to last menu
                                    break
                                elif choice == '1':
                                    # Remove 
                                    print("\nRemove Member")
                                    id = input("Enter Member ID: ")

                                    # Check if they even exist to remove                    
                                    if self.verify_member_exists(id):
                                        try_again = ("\nMember does not exist. Try again? (y/n): ")
                                        if try_again == 'y':
                                            continue
                                        else:
                                            break
                
                                    # then idk here remove it ill do it later
                                elif choice == '2':
                                    # Add a member
                                    print("\nAdd Member")

                                    # btw this is rough draft if its bad its ok to scrap

                                    # Collect the info for the member here

                                    input("Enter Member everything: ")
                                    
                                elif choice == '3':
                                    # Modify 
                                    print("\Modify Member")
                                    id = input("Enter Member ID: ")
                                    # then update it

                        else:
                            print("\nInvalid option. Please try again.")

                elif choice == '0':
                    break  # Exit loop to return to the main menu
                else:
                    print("\nInvalid option. Please try again.")
    
    # Check if the provider ID exists 
    def verify_provider_exists(self, provider_id):
        if self.DB_mgr.ID_exists(provider_id):
            return True
        else:
            return False
    
    # Fetch the provider record
    def get_provider(self, provider_id):   
        return self.DB_mgr.get_provider_record(provider_id)
    
    # Validate user input, verify the provider ID exists, fetch provider record
    def verify_provider_input(self):
        while True:
            user_input = input("\nEnter Provider ID: ")
            if user_input.isdigit() and len(user_input) == 9:
                # Verify if the provider ID exists
                if self.verify_provider_exists(user_input):
                    # Fetch the provider object since ID exists
                    temp_provider = self.get_provider(user_input)
                    if temp_provider:
                        self.update_current_provider(temp_provider)
                        return True
                    else:
                        print("Unexpected error retrieving provider details.")
                else:
                    print("Provider ID not found.")
            else:
                print("Error: Provider ID must be an integer and 9 digits long.")

            try_again = input("Do you want to try again? (y/n): ").lower()
            if try_again != 'y':
                return False
    
    # Update current provider
    def update_current_provider(self, temp_provider):   
        self.current_provider = None
        self.current_provider = ProviderRecord.copy_constructor(temp_provider)

    # Check if the member ID exists 
    def verify_member_exists(self, member_id):
        if self.DB_mgr.ID_exists(member_id):
            return True
        else:
            return False
    
    # Fetch the member record 
    def get_member(self, member_id):
        return self.DB_mgr.get_member_record(member_id)
    
    # Validate user input, verify the member ID exists, fetch member record
    def verify_member_input(self):
        while True:
            user_input = input("\nEnter Member ID: ")
            if user_input.isdigit() and len(user_input) == 9:
                if self.verify_member_exists(user_input):
                    temp_member = self.get_member(user_input)
                    if temp_member:
                        self.update_current_member(temp_member)
                        return True
                    else:
                        print("Unexpected error retrieving member details.")
                else:
                    print("Member ID not found.")
            else:
                print("Error: Member ID must be an integer and 9 digits long.")

            try_again = input("Do you want to try again? (y/n): ").lower()
            if try_again != 'y':
                return False
    
    # update current member 
    def update_current_member(self, temp_member):
        self.current_member = temp_member
        self.current_member = MemberRecord.copy_constructor(temp_member)

    # Retrieve the current provider's record
    def get_current_provider(self):
        return self.current_provider

    # Retrieve the current member's record
    def get_current_member(self):
        return self.current_member
    
    # Display the service record directory
    def display_service_record(self):
        return self.DB_mgr.display_service_directory()
    
    # Confirm if a service code exists in the system
    def verify_service(self, name, sid):
        return self.DB_mgr.is_service(name, sid)
    
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
            if not self.DB_mgr.is_service(service_name, service_code):
                # Service code does not already exist, it's valid for new entry
                break  # Break out of the loop, ready for new entry
            else:
                # Service code already exists in the database, ask for a new one
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
                # Create ServiceRecord object. 
                temp_service = ServiceRecord(
                    service_code,
                    service_provider, 
                    service_member, 
                    service_date_str,
                    service_comment,
                    service_name,
                    service_fee,                   
                )

                # Attempt to add the service record via the Database Manager
                update_success = self.DB_mgr.add_service_record(temp_service)
                
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