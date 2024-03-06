import sys
import os
import bisect
from pprint import pprint
from Records import *

#holds directory of serivices name/id/fee
class DatabaseManager:

    def __init__(self):
    

        # Files #
        self.directory_file = "services.txt" # name of file for service directory


        # Relative Paths #
        self.MemberRecords_relative_path = "Data/UserRecords/MemberRecords"
        self.ProviderRecords_relative_path = "Data/UserRecords/ProviderRecords"
        self.ServiceRecords_relative_path = "Data/ServiceRecords"
        self.ServiceDirectory_relative_path = "Data/services.txt"

        # Data Members #
        self.directory= [] # list where each element holds { Name: [ ID, FEE] } a service- comprised it is the service directory



    

    def package_into_dict(self, to_add_record):
        # Package the attributes into a dictionary
        data_dict = {
            "Street": to_add_record.street,
            "City": to_add_record.city,
            "State": to_add_record.state,
            "Zip": to_add_record.zip,
            "Name": to_add_record.name,
            "ID": to_add_record.ID,
            "Is Suspended": to_add_record.is_suspended
        }
        return data_dict


    def find_file(self,directory, target_file_name):
        # List all files and directories in the specified directory
        all_files_and_dirs = os.listdir(directory)

        # Check each item in the list
        for item in all_files_and_dirs:
            # Construct the full path to the item
            full_path = os.path.join(directory, item)

            # Check if the item is a file and if its name matches the target file name
            if os.path.isfile(full_path) and item == target_file_name:
                return full_path

        # If the file is not found, return None
        return None



    def get_full_path(self, relative_path, file_name=None):
        # Get the current working directory
        current_directory = os.getcwd()
        
        # Construct the full path to the directory
        full_path = os.path.join(current_directory, relative_path)
        
        # If a file name is provided, append it to the directory path
        if file_name:
            full_path = os.path.join(full_path, file_name)
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        
        return full_path



##################################################################################################
################################ Member, Provider, ADMIN records Methods #######################################
##################################################################################################

    def add_user_record(self,to_add_record):

        if isinstance(to_add_record, ProviderRecord):
            return self.add_provider_record(to_add_record)
        elif isinstance(to_add_record, MemberRecord):
            return self.add_member_record(to_add_record)
        else:
            print("Item is neither a ProviderRecord nor a MemberRecord.")
            return False

    def add_member_record(self, to_add_record):

        data_dict = self.package_into_dict(to_add_record)
        id_value = data_dict["ID"]
        id_value_with_prefix = "U" + str(id_value) + ".txt"

        # Assuming self.MemberRecords_relative_path is correctly defined
        full_path = self.get_full_path(self.MemberRecords_relative_path, id_value_with_prefix)

        print(f"Full path: {full_path}")

        # Check if the file already exists
        if os.path.isfile(full_path):
            print("The Member already exists on File. No new record will be created.")
            return False # Return False or an appropriate value to indicate the file already exists

        with open(full_path, 'w') as file:
            for key, value in data_dict.items():
                file.write(f"{value}\n")
            file.write("=\n")
    
        print("MemberRecord successfully uploaded to the database")
        return True

    

    def add_provider_record(self,to_add_record):
        pass


    def remove_user_record(self, UID):
        pass









##################################################################################################
################################ Service Directory Methods #######################################
##################################################################################################


#Loads the service entrys(one line each) from the file into the service directory list
#directory list will contain one sublist for each service, where each sublist is structured as [Name, ID, FEE].
#list is alphabetucally organized A-Z based off of each sublists[0] element, the name of service
    def load_directory(self):
            try:
                with open(self.directory_file, 'r') as file:
                    for line in file:
                        try:
                            parts = line.strip().split(':')
                            self.directory.append(parts)
                        except ValueError:
                            sys.stderr.write(f"Error: Invalid line format in '{self.directory_file}': {line}\n")
                            return False

            except TypeError:
                sys.stderr.write(f"Error: Invalid file path '{self.directory_file}'\n")
                return False

            except FileNotFoundError:
                sys.stderr.write(f"Error: File '{self.directory_file}' not found\n")
                return False

            #catch all o
            except Exception as e:
                sys.stderr.write(f"Error: {e}\n")
                return False

            return True

         
    def update_file(self):
        with open(self.directory_file, 'w') as file:
            for service in self.directory:
                file.write(f"{service[0]}:{service[1]}:{service[2]}\n")
            
    def display_service_directory(self):

        if not self.directory:
            print("The service directory is currently empty. No services are available.\nIf you believe this is an error, please contact an administrator.")
            return False

        print("---------------------------Service Directory-------------------------\n")
        print("Service Name                   Service ID                     Fee\n")
        for service in self.directory:
            name, sid, fee = service
            #print(f"{name:<30} {sid:<20} {fee:<10}")
            print(f"{name:<30} {sid:<30} {fee:<30}")

            
        return True


    def insert_directory_service(self,name,sid,fee):

        for element in self.directory:
            if element[0] == name:
                print(f"The name '{name}' already associated with Serivce '{element[0]}:{element[1]}' in the Service Directory")
                return False

            if element[1] == sid:
                print(f"The Service ID '{sid}' already associated with Serivce '{element[0]}:{element[1]}' in the Service Directory")
                return False

        element = [name,sid,fee]


        bisect.insort(self.directory , element , key=lambda x: x[0])
        print(f"The Service '{name}:{sid}:{fee}' has been added into the Service Directory")

        self.update_file()

        return True




    def remove_directory_service(self,sid):

        for index, element in enumerate(self.directory):
            if element[1] == sid:
                print(f"Service '{element[0]}:{element[1]}' has been removed from the Service Directory")
                del self.directory[index]
                return True # Indicate that the service was successfully removed
                self.update_file()


        print(f"Service ID '{element[1]}' is not associated with a Serivce in the Service Directory")
        return False # Indicate that no service with the given SID was found




Adress = Address("123 Main St", "Anytown", "CA", "12345")
mem = MemberRecord("Jim Bow","223456789",Adress);

base =DatabaseManager()
test= base.package_into_dict(mem)

base.add_user_record(mem)

base.get_record_member(UID)
->memberobject

cleint then eddits the record
base.edit_record(edited_record_object)



