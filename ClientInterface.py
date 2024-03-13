# Imports

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
            print("Exiting to main menu.")
            return
        
        # print current provider
        if self.current_provider is not None:
            print(f"\nCurrent Provider: \n{self.current_provider}\n")
        else:
            print("\nCurrent Provider: Not available")

        # print current member
        if self.current_member is not None:
            print(f"\nCurrent Member: \n{self.current_member}\n")
        else:
            print("\nCurrent Member: Not available")

        # If provider and member ID are provided, show menu. 
        while True:
            # print menu
            print("\nProvider Menu\n")

            # print provider menu
            print("0. Return to Main Menu")
            print("1. Display Current Provider Information")
            print("2. Display Current Member Information")
            print("3. Display Service Record Directory")
            print("4. Enter Service Record")
            print("5. Change Current Member ID")
            print("6. Change Current Provider ID")
            choice = input("\nChoose an option: ")
            # choice 1
            if choice == '1':
                print("\nDisplaying Provider Information")
                if self.current_provider is not None:
                    print(f"\nCurrent Provider: \n{self.current_provider}\n")
                else:
                    print("\nCurrent Provider: Not available")
            # choice 2
            elif choice == '2':
                print("\nDisplaying Member Information")
                if self.current_member is not None:
                    print(f"\nCurrent Member: \n{self.current_member}\n")
                else:
                    print("\nCurrent Member: Not available")
            # choice 3
            elif choice == '3':
                print("\nDisplay Service Record Directory")
                self.display_service_record()
            # choice 4
            elif choice == '4':
                print("\nEnter Service Record")
                self.write_service()
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
                print("\nManager Menu")
                print("1. Manage Members and Providers")
                print("2. Manage Services")
                print("3. Reports")
                print("0. Return to Main Menu")
                choice = input("Choose an option: ")

                if choice == '1':
                    self.manage_users_menu()
                elif choice == '2':
                    self.manage_services_menu()
                elif choice == '3':
                    self.manage_reports_menu()
                elif choice == '0':
                    break  # Exit loop to return to the main menu
                else:
                    print("\nInvalid option. Please try again.")


##################################################################
#                       User Management                          #
##################################################################

    def manage_users_menu(self):
        while True:
            print("\nUser Management")
            print("1. Add Provider")
            print("2. Modify Provider")
            print("3. Remove Provider")
            print("4. Add Member")
            print("5. Modify Member")
            print("6. Remove Member")
            print("0. Return to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_provider()
            elif choice == '2':
                self.modify_provider()
            elif choice == '3':
                self.remove_provider()
            elif choice == '4':
                self.add_member()
            elif choice == '5':
                    self.modify_member()
            elif choice == '6':
                    self.remove_member()
            elif choice == '0':
                break  # Exit loop to return to the main menu
            else:
                print("\nInvalid option. Please try again.")



    def add_provider(self):
        to_add = ProviderRecord()
        user_input = 'n'
        while user_input != 'y':
            self.input_user(to_add)
            to_add.ID = 111111111
            print(to_add)
            user_input = input("Does this information look correct? y/n: ")
            user_input = user_input.lower()
        self.DB_mgr.add_provider_record(to_add)
                
    def modify_provider(self):
        user_input = 'n'
        to_edit = None
        while user_input != 'y':
            if (self.verify_provider_input()):
                to_edit = self.current_provider
                self.current_provider = None
                if not (to_edit is None):
                    print(to_edit)
                    user_input = input("Is this the Provider you wish to edit? (y/n): ")
                    user_input = user_input.lower()
            else:
                user_input = 'y'
        
        if not (to_edit is None):
            self.input_user(to_edit)
            self.DB_mgr.edit_provider_record(to_edit)
        
        

    def remove_provider(self):
        user_input = 'n'
        to_remove = None
        while user_input != 'y':
            self.verify_provider_input()
            to_remove = self.current_provider
            self.current_provider = None
            print(to_remove)
            user_input = input("Is this the Provider you wish to remove? (y/n): ")
            user_input = user_input.lower()
        self.DB_mgr.remove_provider_record(to_remove)

    def add_member(self):
        to_add = MemberRecord()
        user_input = 'n'
        while user_input != 'y':
            self.input_user(to_add)
            to_add.ID = 111111111
            print(to_add)
            user_input = input("Does this information look correct? y/n: ")
            user_input = user_input.lower()
            print(user_input)
        
        self.DB_mgr.add_member_record(to_add)  

    def modify_member(self):
        user_input = 'n'
        to_edit = None
        while user_input != 'y':
            self.verify_member_input()
            to_edit = self.current_member
            self.current_member = None
            print(to_edit)
            user_input = input("Is this the Member you wish to edit? (y/n): ")
            user_input = user_input.lower()
        self.input_user(to_edit)
        user_input = ''
        user_input = input("Update membership suspension status? (y/n): ")
        while (user_input != 'y' and user_input != 'n'):
            print("Invalid entry, please enter y or n")
            user_input = input("Change membership suspension status?")
        if (user_input == 'y'):
            to_edit.is_suspended = not to_edit.is_suspended
            status = to_edit.convert_status()
            print("Membership status has been updated to " + str(status))
        self.DB_mgr.edit_member_record(to_edit)

    def remove_member(self):
        user_input = 'n'
        to_remove = None
        while user_input != 'y':
            self.verify_member_input()
            to_remove = self.current_member
            self.current_member = None
            print(to_remove)
            user_input = input("Is this the Member you wish to remove? (y/n): ")
            user_input = user_input.lower()
        self.DB_mgr.remove_member_record(to_remove)  


    def input_user(self, to_add):
        while True:
            try:
                name_input = input("Enter User's Name: ")
                to_add.name = name_input
                break
            except Exception as e:
                print(e)

        while True:
            try:
                street_input = input("Enter the User's Street: ")
                to_add.street = street_input
                break
            except Exception as e:
                print(e)

        while True:
            try:
                city_input = input("Enter the User's city: ")
                to_add.city = city_input
                break
            except Exception as e:
                print(e)
        while True:
            try:
                state_input = input("Enter the User's State Abbreviation: ")
                to_add.state = state_input
                break
            except Exception as e:
                print(e)
        while True:
            try:
                zip_input = input("Enter the User's Zip Code: ")
                to_add.zip = zip_input
                break
            except Exception as e:
                print(e)
        



##################################################################
#                       Service Management                       #
##################################################################

    def manage_services_menu(self):
        while True:
            print("\nService Management")
            print("1. Add Service")
            print("2. Modify Service")
            print("3. Remove Service")
            print("0. Return to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_service()
            elif choice == '2':
                    self.modify_service()
            elif choice == '3':
                    self.remove_service()
            elif choice == '0':
                break  # Exit loop to return to the main menu
            else:
                print("\nInvalid option. Please try again.")

    def add_service(self):
        
        user_input = 'n'
        while user_input != 'y':
            name, code, fee = self.input_service()
            
            print(name + ' ' + code + ' ' + fee)
            user_input = input("Does this information look correct? y/n: ")
            user_input = user_input.lower()
        
        self.DB_mgr.insert_directory_service(name, code, fee)

    def modify_service(self):
        user_input = 'y'
        while user_input != 'n':
            to_edit = input("Please enter the service code of the service to edit: ")
            try:
                service = self.DB_mgr.get_directory_service(to_edit)
                if (service is None):
                    print("Service does not exist")
                    user_input = input("Try again? (y/n): ")
                else:
                    print(service)
                    service[0], service[1], service[2] = self.input_service()
                    self.DB_mgr.update_directory_service(service[0], service[1], service[2])
                    break
            except:
                print("Invalid entry, please enter a 6 digit service code: ")

                
            

    def remove_service(self):
        user_input = 'n'
        while user_input != 'y':
            to_remove_code = input("Please enter ther service code of the service to remove: ")
            try:
                to_remove = self.DB_mgr.get_directory_service(to_remove_code)
                print(to_remove)
                user_input = input("Is this the service you'd like to remove? (y/n): ")
            except:
                print("Invalid entry, please enter a 6-digit service code")

        self.DB_mgr.remove_directory_service(to_remove_code)
                

    def input_service(self):
        service_name = input("Please enter the name of the service: ")
        service_name = str(service_name)
        while (len(service_name) > 20):
            print("Invalid entry, please enter a name with 20 or less characters")
            service_name = input("Please enter the name of the service: ")
        service_code = input("Please enter the service code")
        service_code = str(service_code)
        while (len(service_code) != 6):
            print("Invalid entry, please enter a 6 digit number")
            service_code = input("Please enter the service code: ")
        service_fee = input("Please enter the fee associated with the service: ")
        while(float(service_fee) > 999.99):
            print("Invalid Entry, fee must be less than $999.99")
            service_fee = input("Please enter the fee associated with the service: ")
        service_fee = str(service_fee)
        return service_name, service_code, service_fee

##################################################################
#                       Report Management                        #
##################################################################   

    def manage_reports_menu(self):
        while True:
            print("\nReport Management")
            print("1. Generate Member Reports")
            print("2. Generate Individual Member Report")
            print("3. Generate Provider Reports")
            print("4. Generate Individual Provider Report")
            print("5. Generate Summary Report")
            print("6. Generate Weekly Report")
            print("0. Return to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                self.generate_member_reports()
            elif choice == '2':
                self.generate_member_report()
            elif choice == '3':
                self.generate_provider_reports()
            elif choice == '4':
                self.generate_provider_report()
            elif choice == '5':
                self.generate_summary_report()
            elif choice == '6':
                self.generate_member_reports()
                self.generate_provider_reports()
                self.generate_summary_report()
            elif choice == '0':
                break  # Exit loop to return to the main menu
            else:
                print("\nInvalid option. Please try again.")


    def generate_member_reports(self):
        pass

    def generate_member_report(self):
        pass

    def generate_provider_reports(self):
        pass

    def generate_provider_report(self):
        pass

    def generate_summary_report(self):
        pass


    # Check if the provider ID exists 
    def verify_provider_exists(self, provider_id):
        if self.DB_mgr.ID_exists(provider_id):
            return True
        else:
            return False
    
    # Fetch the provider record
    def get_provider(self, provider_id):
        # Use placeholder values that pass the Address validation
        minimal_address = Address("NA", "NA", "NA", "97205")
        
        # Attempt to create a ProviderRecord with placeholder values
        # Important: Adjust this based on what ProviderRecord and Address validations allow
        temp_provider = ProviderRecord("NA", provider_id, minimal_address)
        
        # Fetch the provider record
        provider_record = self.DB_mgr.get_provider_record(temp_provider)
        
        return provider_record
    
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
        self.current_provider = ProviderRecord(temp_provider)

    # Check if the member ID exists 
    def verify_member_exists(self, member_id):
        if self.DB_mgr.ID_exists(member_id):
            return True
        else:
            return False
    
    # Fetch the provider record
    def get_member(self, member_id):
        # Use placeholder values that pass the Address validation
        minimal_address = Address("NA", "NA", "NA", "97205")
        
        # Attempt to create a ProviderRecord with placeholder values
        # Important: Adjust this based on what ProviderRecord and Address validations allow
        temp_member = MemberRecord("NA", member_id, minimal_address)
        
        # Fetch the provider record
        member_record = self.DB_mgr.get_member_record(temp_member)
        
        return member_record
    
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
        self.current_member = MemberRecord(temp_member)

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
                if len(service_name) > 23:
                    print("Error: The service name must be less than 23 characters.")
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
                print("Error: The service code does not exist in the database. Please enter a new service name and service code.")
                
            else:
                # Service code already exists in the database, move on to create Service Record object
                break  

        # Assuming current_member and current_provider are already set
        service_member = self.current_member
        service_provider = self.current_provider

        # Initialize service_comment as None or an empty string if no comment is provided
        service_comment = None

        # Ask the user if they want to add a comment
        add_comment = input("Would you like to add a comment to the service record? (yes/no): ").strip().lower()

        if add_comment == "yes":
            while True:
                service_comment = input("\nEnter the Service Comment (100 characters max): ")
                
                # Validate the length of the comment
                if len(service_comment) <= 100:
                    break  # Exit the loop if the comment is valid
                else:
                    print("Error: The service comment must be 100 characters or less.")
        elif add_comment == "no":
            # If the user chooses not to add a comment, you can leave service_comment as None or ""
            print("Proceeding without adding a comment.")
        else:
            print("Invalid response. Proceeding without adding a comment.")


        # Get user input for service date in format (MM-DD-YYYY)
        while True:
            from datetime import datetime
            service_date_str = input("\nEnter the Service Date (MM-DD-YYYY): ")
            try:
                # Now this will work as expected
                datetime.strptime(service_date_str, "%m-%d-%Y")
                break  # If conversion succeeds, exit the loop
            except ValueError:
                print("The date entered is invalid or does not match the format MM-DD-YYYY. Please try again.")
        
        update_success = False  # Initialize update_success to False
        try:
            # Fetch service details using the service_code
            service_details = self.DB_mgr.get_directory_service(service_code)
            
            if service_details:
                # Unpack the fetched details
                fetched_name, fetched_sid, fetched_fee = service_details 
                
                # Assuming placeholders for missing data
                #service_code =  int(fetched_sid)
                #service_name = fetched_name
                #service_fee = float(fetched_fee)
                service_code =  fetched_sid
                service_name = fetched_name
                service_fee = fetched_fee
                
                # Check if a comment was provided by the user
                if service_comment:  
                    # Create the ServiceRecord object with the comment
                    service_record = ServiceRecord(service_code, service_provider.ID, service_member.ID, service_date_str, service_name, service_fee, service_comment)
                else:
                    # Create the ServiceRecord object without the comment
                    service_record = ServiceRecord(service_code, service_provider.ID, service_member.ID, service_date_str, service_name, service_fee)
                
                # Attempt to add the service record via the Database Manager
                update_success = self.DB_mgr.add_service_record(service_record)
            
            # Initialize update_success to False at the beginning of the try block to ensure it's defined
            else:
                update_success = False
                print("Failed to fetch service details.")
            
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
    '''     
        while True:
            try:
                service_fee_input = input("\nEnter the Service Fee: ")
                service_fee = float(service_fee_input)
                if service_fee < 0 or service_fee >= 1000000:
                    raise ValueError("Service fee must be between $0.00 and $999,999.99.")
                break
            except ValueError as e:
                print(f"Invalid input for service fee: {e}. Please try again.")
        '''  