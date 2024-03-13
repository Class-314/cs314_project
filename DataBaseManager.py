import sys
import os
import glob
import bisect
from pprint import pprint
from Records import *
import random
import string
import datetime
import re

#test
#holds directory of serivices name/id/fee
class DatabaseManager:

    def __init__(self):
    

        # Files #
        self.directory_file = "services.txt" # name of file for service directory


        # Relative Paths spawning from inside programs directory#
        self.MemberRecords_relative_path = "Data/UserRecords/MemberRecords/"
        self.ProviderRecords_relative_path = "Data/UserRecords/ProviderRecords/"
        self.ServiceRecords_relative_path = "Data/ServiceRecords/"
        self.ServiceDirectory_relative_path = "Data/services.txt"
        self.Registerd_IDs_relative_path = "Data/Registerd_IDs.txt"

        # Data Members #
        self.directory= [] # list where each element holds { Name: [ ID, FEE] } a service- comprised it is the service directory
        self.IDs = {} #Dictionary of all ID's ever generated


        #Essential Methods for program start #
        self.load_IDs()
        self.load_directory()



##################################################################################################
#################################### Utility Methods ##########h##################################
##################################################################################################

    #-------------Backend Work---------------#

    def load_IDs(self):

        with open(self.Registerd_IDs_relative_path, 'r') as file:
            # Split the line into parts based on the first space
            for line in file:
                parts = line.split(' ', 1)

                # The first part is the key, and the rest of the line is the value
                key = parts[0].strip()

                # Add the key-value pair to the dictionary

                self.IDs[key] = ""

            
            return True

    def register_ID(self,ID):
        value = self.ID_exists(ID)
        if value ==True:
            print("The Member already exists on File. No new record will be created.")
            return False # Return False or an appropriate value to indicate the file already exists
        else:
            with open(self.Registerd_IDs_relative_path, 'a') as file:
                file.write(f"{ID}\n")
            
        return True


    def get_members_dict(self,instance):
        members_dict = {}
        for name in dir(instance):
            if not name.startswith("__"): # Exclude special methods
                members_dict[name] = getattr(instance, name)
        return members_dict

    def print_members(self,instance):
        members_dict = get_members_dict(instance)
        for name, value in members_dict.items():
            print(f"{name}: {value}")


    #-------------Client---------------#
    # Package the attributes of Provider/Member object into a dictionary
    def package_into_dict(self, to_add_record):

        if isinstance(to_add_record, MemberRecord):
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
        elif isinstance(to_add_record, ProviderRecord):
            data_dict = {
                "Street": to_add_record.street,
                "City": to_add_record.city,
                "State": to_add_record.state,
                "Zip": to_add_record.zip,
                "Name": to_add_record.name,
                "ID": to_add_record.ID,
#                "Number Consultations": to_add_record.num_consultations,
                #"Total Payment": to_add_record.total_payment
            }
            return data_dict
        elif isinstance(to_add_record, ServiceRecord):
            data_dict = {
                #"Fee": to_add_record._fee,
                "Service Code": to_add_record.service_code,
                "Provider ID": to_add_record.pID,
                "Member ID": to_add_record.mID,
                #"Comments": to_add_record.comments,
                "Date Provided": to_add_record.date_provided,
                "Current DateTime": to_add_record.current_datetime
            }
            return data_dict

        return None


    def generate_random_ID(self):
        # Define the character set including digits and asterisks
        char_set = string.digits 

        # Generate a random ID of length 9
        new_ID = ''.join(random.choice(char_set) for _ in range(9))

        # Check if the ID already exists
        while new_ID in self.IDs:
            new_ID = ''.join(random.choice(char_set) for _ in range(9))

        return new_ID

    

    # Check if the ID exists in the dictionary
    def ID_exists(self,ID):
        return str(ID) in self.IDs

##################################################################################################
################################ Member, Provider, ADMIN records Methods #######################################
##################################################################################################
    
    #-------------Backend Work---------------#

    def add_member_record(self, to_add_record):

        data_dict = self.package_into_dict(to_add_record)
#       file_name = data_dict["ID"]
        file_name = self.generate_random_ID()
        
        
        file_name_with_prefix = "M" + str(file_name) + ".txt"
        relative_file_path = self.MemberRecords_relative_path + file_name_with_prefix

        # Check if the ID already exists
        value = self.ID_exists(file_name)
        if value ==True:

                    print("The Member already exists on File. No new record will be created.")
                    return False # Return False or an appropriate value to indicate the file already exists
        else:
            with open(relative_file_path, 'w') as file:

                for key, value in data_dict.items():
                    file.write(f"{value}\n")

                file.write("=\n")
    
            self.register_ID(file_name)
        
            print(f"Member Record successfully uploaded to the database")

        return True

    def add_provider_record(self, to_add_record):

        data_dict = self.package_into_dict(to_add_record)
        #file_name = data_dict["ID"]
        file_name = self.generate_random_ID()
        file_name_with_prefix = "P" + str(file_name) + ".txt"
        relative_file_path = self.ProviderRecords_relative_path + file_name_with_prefix

        # Check if the ID already exists
        value = self.ID_exists(file_name)
        if value ==True:

                    print("The Provider already exists on File. No new record will be created.")
                    return False # Return False or an appropriate value to indicate the file already exists
        else:
            with open(relative_file_path, 'w') as file:

                for key, value in data_dict.items():
                    file.write(f"{value}\n")

                file.write("=\n")

            self.register_ID(file_name)
        
            print(f"Provider Record successfully uploaded to the database")

        return True

    def remove_member_record(self, to_remove_record):
        # Convert the record to a dictionary
        data_dict = self.package_into_dict(to_remove_record)
        file_name = data_dict["ID"]
        file_name_with_prefix = "M" + str(file_name) + ".txt"
        relative_file_path = self.MemberRecords_relative_path + file_name_with_prefix

        # Check if the file exists
        if os.path.exists(relative_file_path):
            # Attempt to remove the file
            try:
                os.remove(relative_file_path)
                print(f"Member Record with ID {file_name} successfully removed from the database.")
                return True
            except Exception as e:
                print(f"An error occurred while removing the Member Record with ID {file_name}: {e}")
                return False # Return False or an appropriate value to indicate an error occurred
        else:
            print(f"Member Record with ID {file_name} does not exist in the database. No record was removed.")
            return False # Return False or an appropriate value to indicate the file does not exist


    def remove_provider_record(self, to_remove_record):
        # Convert the record to a dictionary
        data_dict = self.package_into_dict(to_remove_record)
        file_name = data_dict["ID"]
        file_name_with_prefix = "P" + str(file_name) + ".txt"
        relative_file_path = self.ProviderRecords_relative_path + file_name_with_prefix

        # Check if the file exists
        if os.path.exists(relative_file_path):
            # Attempt to remove the file
            try:
                os.remove(relative_file_path)
                print(f"Provider Record with ID {file_name} successfully removed from the database.")
                return True
            except Exception as e:
                print(f"An error occurred while removing the Provider Record with ID {file_name}: {e}")
                return False # Return False or an appropriate value to indicate an error occurred
        else:
            print(f"Provider Record with ID {file_name} does not exist in the database. No record was removed.")
            return False # Return False or an appropriate value to indicate the file does not exist
    
    

    def get_member_record(self, to_add_record):

        data_dict = self.package_into_dict(to_add_record)
        file_name = data_dict["ID"]
        file_name_with_prefix = "M" + str(file_name) + ".txt"
        relative_file_path = self.MemberRecords_relative_path + file_name_with_prefix

        # Check if the file exists
        if os.path.exists(relative_file_path):
            # Attempt to remove the file
            try:
                if os.path.exists(relative_file_path):
                    with open(relative_file_path, 'r') as file:
                        data = file.read()
                        lines = data.split('\n')
                        # Assuming the file structure is consistent and each line corresponds to a different attribute
                        street = lines[0].strip()
                        city = lines[1].strip()
                        state = lines[2].strip()
                        zip_code = lines[3].strip()
                        name = lines[4].strip()
                        ID = lines[5].strip()
                        is_suspended = lines[6].strip() == 'True' # Convert string to boolean

                        # Create a MemberRecord object with the data and return
                        an_address = Address(street,city,state,zip_code )
                        return MemberRecord(name,ID,an_address) 

            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"Member Record with ID {file_name} does not exist in the database. No record was removed.")
            return None # Return False or an appropriate value to indicate the file does not exist

    def get_provider_record(self, to_add_record):

        data_dict = self.package_into_dict(to_add_record)
        file_name = data_dict["ID"]
        file_name_with_prefix = "P" + str(file_name) + ".txt"
        relative_file_path = self.ProviderRecords_relative_path + file_name_with_prefix

        # Check if the file exists
        if os.path.exists(relative_file_path):
            # Attempt to remove the file
            try:
                if os.path.exists(relative_file_path):
                    with open(relative_file_path, 'r') as file:
                        data = file.read()
                        lines = data.split('\n')
                        # Assuming the file structure is consistent and each line corresponds to a different attribute
                        street = lines[0].strip()
                        city = lines[1].strip()
                        state = lines[2].strip()
                        zip_code = lines[3].strip()
                        name = lines[4].strip()
                        ID = lines[5].strip()
                        #consultations=int(lines[6].strip())
                        #t_payment=float(lines[7].strip())
                        # Create a MemberRecord object with the data and return
                        an_address = Address(street,city,state,zip_code )
                        Provrecord = ProviderRecord(name,ID,an_address) 
                        #Provrecord.num_consultations = consultations
                        #Provrecord.total_payment= t_payment
                        print("IN")
                        return Provrecord
                        

            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"Provider Record with ID {file_name} does not exist in the database. No record was removed.")
            return None # Return False or an appropriate value to indicate the file does not exist

    def edit_member_record(self, to_update_record):
        try:
            data_dict = self.package_into_dict(to_update_record)
            file_name = data_dict["ID"]
            file_name_with_prefix = "M" + str(file_name) + ".txt"
            relative_file_path = self.MemberRecords_relative_path + file_name_with_prefix

            # Check if the file exists
            if os.path.exists(relative_file_path):
                # Read the file and update the lines
                with open(relative_file_path, 'r') as file:
                    data = file.read()
                    lines = data.split('\n')

                # Assuming the file structure is consistent and each line corresponds to a different attribute
                lines[0] = f"{data_dict['Street']}\n"
                lines[1] = f"{data_dict['City']}\n"
                lines[2] = f"{data_dict['State']}\n"
                lines[3] = f"{data_dict['Zip']}\n"
                lines[4] = f"{data_dict['Name']}\n"
                lines[5] = f"{data_dict['ID']}\n"
                lines[6] = f"{data_dict['Is Suspended']}\n"


                # Write the updated lines back to the file
                with open(relative_file_path, 'w') as file:
                    file.writelines(lines)

                print(f"Member Record with ID {file_name} successfully updated in the database.")
                return True
            else:
                print(f"Member Record with ID {file_name} does not exist in the database. No record was updated.")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def edit_provider_record(self, to_update_record):
        try:
            data_dict = self.package_into_dict(to_update_record)
            file_name = data_dict["ID"]
            file_name_with_prefix = "P" + str(file_name) + ".txt"
            relative_file_path = self.ProviderRecords_relative_path + file_name_with_prefix

            # Check if the file exists
            if os.path.exists(relative_file_path):
                # Read the file and update the lines
                with open(relative_file_path, 'r') as file:
                    data = file.read()
                    lines = data.split('\n')

                # Assuming the file structure is consistent and each line corresponds to a different attribute
                lines[0] = f"{data_dict['Street']}\n"
                lines[1] = f"{data_dict['City']}\n"
                lines[2] = f"{data_dict['State']}\n"
                lines[3] = f"{data_dict['Zip']}\n"
                lines[4] = f"{data_dict['Name']}\n"
                lines[5] = f"{data_dict['ID']}\n"
                #lines[7] = f"{data_dict['Number Consultations']}\n"
                #lines[8] = f"{data_dict['Total Payment']}\n"

                # Write the updated lines back to the file
                with open(relative_file_path, 'w') as file:
                    file.writelines(lines)

                print(f"Provider Record with ID {file_name} successfully updated in the database.")
                return True
            else:
                print(f"Provider Record with ID {file_name} does not exist in the database. No record was updated.")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False




    #-------------Client---------------#
    def add_user_record(self,to_add_record):

        if isinstance(to_add_record, ProviderRecord):
            return self.add_provider_record(to_add_record)
        elif isinstance(to_add_record, MemberRecord):
            return self.add_member_record(to_add_record)
        else:
            print("Item is neither a ProviderRecord nor a MemberRecord.")
            return False


    def remove_user_record(self,to_remove_record):

        if isinstance(to_remove_record, ProviderRecord):
            return self.remove_provider_record(to_remove_record)
        elif isinstance(to_remove_record, MemberRecord):
            return self.remove_member_record(to_remove_record)
        else:
            print("Item is neither a ProviderRecord nor a MemberRecord.")
            return False
    
    
    def get_user_record(self, to_get_record):
        if isinstance(to_get_record, ProviderRecord):
            return self.get_provider_record(to_get_record)
        elif isinstance(to_get_record, MemberRecord):
            return self.get_member_record(to_get_record)
        else:
            print("Item is neither a ProviderRecord nor a MemberRecord.")
            return False


    def edit_user_record(self, to_edit_record):
        if isinstance(to_edit_record, ProviderRecord):
            return self.edit_provider_record(to_edit_record)
        elif isinstance(to_edit_record, MemberRecord):
            return self.edit_member_record(to_edit_record)
        else:
            print("Item is neither a ProviderRecord nor a MemberRecord.")
            return False



################################################################################################
#####################################Service Records #############################################
##################################################################################################



#-------------Backend Work---------------#

                

    def update_member_with_service_record_fname(self,ID,fname):

        file_name_with_prefix = "M" + str(ID) + ".txt"
        relative_file_path = self.MemberRecords_relative_path + file_name_with_prefix


        if(os.path.exists(relative_file_path) ==False):
                sys.stderr.write("\nMemeber Record not found. Unable to link Service Record to Member\n")
                return False

        with open(relative_file_path, 'a') as file:
            file.write(f"{fname}\n")

        return True

    def update_provider_with_service_record_fname(self,ID,fname):

        file_name_with_prefix = "P" + str(ID) + ".txt"
        relative_file_path = self.ProviderRecords_relative_path + file_name_with_prefix


        if(os.path.exists(relative_file_path) ==False):
                sys.stderr.write("\nProvider Record not found. Unable to link Service Record to Provider\n")
                return False
        
        with open(relative_file_path, 'a') as file:
            file.write(f"{fname}\n")

        return True



#-------------Client---------------#

    def add_service_record(self,to_add_record):

        if isinstance(to_add_record, ServiceRecord) == False:
            print("Item is not a ServiceRecord.")
            return False

        data_dict = self.package_into_dict(to_add_record)

        # List all existing files that match the pattern
        existing_files = glob.glob(f"{self.ServiceRecords_relative_path}/SR*.txt")

        # Extract the integer part from the filename, if possible
        existing_numbers = []
        for f in existing_files:
            match = re.search(r'SR(\d+)_', f)
            if match:
                existing_numbers.append(int(match.group(1)))


        # Find the maximum number if any files exist, or start with 0 if the directory is empty
        next_number = max(existing_numbers, default=0) + 1 if existing_numbers else 0


        #Get the current date
        now = datetime.datetime.now()

        # Format the date as MM-DD-YYYY without dashes
        formatted_date = now.strftime("%m%d%Y")

        # Construct the new filename with the incremented number
        new_filename_with_prefix = f"SR{next_number}_{formatted_date}.txt"

        relative_file_path = self.ServiceRecords_relative_path + new_filename_with_prefix


        # Check if the ID already exists
        value = self.ID_exists(relative_file_path)
        if value ==True:

                    print("The Service Record already exists on File. No new record will be created.")
                    return False # Return False or an appropriate value to indicate the file already exists
        else:
            with open(relative_file_path, 'w') as file:

                for key, value in data_dict.items():
                    file.write(f"{value}\n")

        print(f"Serivce Record successfully uploaded to the database")

        m_update= self.update_member_with_service_record_fname(to_add_record.mID,new_filename_with_prefix) 
        p_update =self.update_provider_with_service_record_fname(to_add_record.pID,new_filename_with_prefix)
    
        if m_update== False or p_update == False:
            return False
        else:
            return True


##################################################################################################
################################ Service Directory Methods #######################################
##################################################################################################

#-------------Backend Work---------------#

#Loads the service entrys(one line each) from the file into the service directory list
#directory list will contain one sublist for each service, where each sublist is structured as [Name, ID, FEE].
#list is alphabetucally organized A-Z based off of each sublists[0] element, the name of service
    def load_directory(self):
            try:
                with open(self.ServiceDirectory_relative_path, 'r') as file:
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
        with open(self.ServiceDirectory_relative_path, 'w') as file:
            for service in self.directory:
                file.write(f"{service[0]}:{service[1]}:{service[2]}\n")
        return True

    #-------------Client---------------#
            
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

        # Find the insertion point for the new element
        bisect.insort(self.directory , element , key=lambda x: x[0])

        print(f"The Service '{name}:{sid}:{fee}' has been added into the Service Directory")

        self.update_file()

        return True


    def is_service(self,name,sid):
        # Assuming self.directory is the list of sublists you're traversing
        for service in self.directory:
            if service[1] == sid and service[0]==name:
                return True 
        return False # Return None if no matching service is found



    def remove_directory_service(self,sid):

        for index, element in enumerate(self.directory):
            if element[1] == sid:
                print(f"Service '{element[0]}:{element[1]}' has been removed from the Service Directory")
                del self.directory[index]
                self.update_file()
                return True # Indicate that the service was successfully removed
        print(f"Service ID '{sid}' is not associated with a Serivce in the Service Directory")
        return False # Indicate that no service with the given SID was found


    
     
    def get_directory_service(self,sid):
        # Assuming self.directory is the list of sublists you're traversing
        for service in self.directory:
            if service[1] == sid:
                return service
        return None # Return None if no matching service is found
    


    def update_directory_service(self,name,sid,fee):

        flag= False
        for index, element in enumerate(self.directory):
            if element[1] == sid:
                flag = True
                del self.directory[index]
        
        if flag==True:
            element = [name,sid,fee]

            # Find the insertion point for the new element
            bisect.insort(self.directory , element , key=lambda x: x[0])

            self.update_file()
            print(f"The Service '{name}:{sid}:{fee}' has been edited in the Service Directory")

            return True

        else:
            print(f"Service ID '{sid}' is not associated with a Serivce in the Service Directory")
            return False 
        

#tests
#data = DatabaseManager()
""""
#test
        
#seed
ad = Address("Sw carrot RD", "Clackamas","OR","97015")
m = MemberRecord("Jeb Bush", 100000000 ,ad)
p = ProviderRecord("George Bush", 200000000, ad)
serve= ServiceRecord("123456",200000000,100000000,"01-23-2024","destroyer of worlds", 123)


#add
data.add_user_record(m)
data.add_user_record(p)

#new update

data.add_service_record(serve)

"""

#Service Directory Tests
"""
Data.insert_directory_service("two_time","2","444")
Data.insert_directory_service("three_time","3","444")
Data.display_service_directory()
element=Data.get_directory_service("1")
elementa=Data.get_directory_service("45")
Data.update_directory_service("CARRRRRR","1","444")
Data.update_directory_service("TESTA","1442","444")
Data.display_service_directory()
"""






