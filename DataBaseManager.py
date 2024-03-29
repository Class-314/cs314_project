import sys
import os
import glob
import bisect
from Records import *
import random
import string
import datetime
import time

#test
#holds directory of serivices name/id/fee
class DatabaseManager:

    def __init__(self):
    

        # Files #
        self.directory_file = "services.txt" # name of file for service directory


        # Relative Paths spawning from inside programs directory#
        self.MemberRecords_relative_path = "Data/UserRecords/MemberRecords/"
        self.ProviderRecords_relative_path = "Data/UserRecords/ProviderRecords/"
        self.MemberReports_relative_path = "Data/Reports/MemberReports/"
        self.ProviderReports_relative_path = "Data/Reports/ProviderReports/"
        self.EFTDataReports_relative_path = "Data/Reports/EFTDataReports/"
        self.SummaryReports_relative_path = "Data/Reports/SummaryReports/"
        self.ServiceRecords_relative_path = "Data/ServiceRecords/"
        self.ServiceDirectory_relative_path = "Data/services.txt"
        self.Registerd_IDs_relative_path = "Data/Registerd_IDs.txt"
        self.SR_count_relative_path = "Data/SR_count.txt"

        # Data Members #
        self.directory= [] # list where each element holds { Name: [ ID, FEE] } a service- comprised it is the service directory
        self.IDs = {} #Dictionary of all ID's ever generated
        self.SR_count = 0


        #Essential Methods for program start #
        if not self.load_IDs():
            raise ValueError("Failed to load IDs during initialization")
        if not self.load_directory():
            raise ValueError("Failed to load directory during initialization")
        if not self.load_SR_count():
            raise ValueError("Failed to load SR count during initialization")

##################################################################################################
#################################### PYTEST Helper Methods ##########h##################################
##################################################################################################

    def Hpytest_remove_latest_entry(self):
        try:
            # Open the file in read mode to read its contents
            with open(self.Registerd_IDs_relative_path, 'r') as file:
                lines = file.readlines()

            # Remove the last entry from the list of lines
            if lines:
                lines.pop()

            # Open the file in write mode and write the updated list of lines back to the file
            with open(self.Registerd_IDs_relative_path, 'w') as file:
                file.writelines(lines)

            return True
        except FileNotFoundError:
            print("File not found:", self.Registerd_IDs_relative_path)
            return False
        except Exception as e:
            print("Error:", e)
            return False


    def Hpytest_deincrement_SR_file_count(self):
        try:
            self.SR_count -= 1  # Decrement SR_count by 1

            with open(self.SR_count_relative_path, 'w') as file:
                file.write(str(self.SR_count))

            return True
    
        except:
               print("File not found:", self.SR_count_relative_path)
               return False

    def Hpytest_remove_latest_SR_record(self, to_remove_record):
        # Convert the record to a dictionary
        data_dict = self.package_into_dict(to_remove_record)
       
        next_number = str(self.SR_count)

        now = data_dict["Date Provided"]
        formatted_date = now.replace('-','')

        # Construct the new filename with the incremented number
        new_filename_with_prefix = f"SR{next_number}_{formatted_date}.txt"

        relative_file_path = self.ServiceRecords_relative_path + new_filename_with_prefix

        # Check if the file exists
        if os.path.exists(relative_file_path):
            # Attempt to remove the file
            try:
                os.remove(relative_file_path)

                return self.Hpytest_deincrement_SR_file_count()

            except Exception as e:
                return False # Return False or an appropriate value to indicate an error occurred
        else:
            return False # Return False or an appropriate value to indicate the file does not exist
            

    

##################################################################################################
#################################### Utility Methods ##########h##################################
##################################################################################################

    #-------------Backend Work---------------#
        
    def debug_remove_latest_entry(self):
        try:
            # Open the file in read mode to read its contents
            with open(self.Registerd_IDs_relative_path, 'r') as file:
                lines = file.readlines()

            # Remove the last entry from the list of lines
            if lines:
                lines.pop()

            # Open the file in write mode and write the updated list of lines back to the file
            with open(self.Registerd_IDs_relative_path, 'w') as file:
                file.writelines(lines)

            return True
        except FileNotFoundError:
            print("File not found:", self.Registerd_IDs_relative_path)
            return False
        except Exception as e:
            print("Error:", e)
            return False


    def load_SR_count(self):
        try:
            with open(self.SR_count_relative_path, 'r') as file:
                count = file.readline()

            self.SR_count = int(count)
            return True

        except:
               print("File not found:", self.SR_count_relative_path)
               return False


    def update_SR_file_count(self):
        try:
            with open(self.SR_count_relative_path, 'w') as file:
                file.write(str(self.SR_count))

            return True
    
        except:
               print("File not found:", self.SR_count_relative_path)
               return False

    def load_IDs(self):  
        try:
            with open(self.Registerd_IDs_relative_path, 'r') as file:
                # Split the line into parts based on the first space
                for line in file:
                    parts = line.split(' ', 1)

                    # The first part is the key, and the rest of the line is the value
                    key = parts[0].strip()

                    # Add the key-value pair to the dictionary

                    self.IDs[key] = ""

            return True

        except:
               print("File not found:", self.Registerd_IDs_relative_path)
               return False


    def register_ID(self,ID):
        value = self.ID_exists(ID)
        if value ==True:
            print("The Member already exists on File. No new record will be created.")
            return False # Return False or an appropriate value to indicate the file already exists
        else:
            try:
                self.IDs[str(ID)] = ""
                with open(self.Registerd_IDs_relative_path, 'a') as file:
                    file.write(f"{ID}\n")
                return True
            except:
                print("File not found:", self.Registerd_IDs_relative_path)
                return False
            


    def get_members_dict(self,instance):
        members_dict = {}
        for name in dir(instance):
            if not name.startswith("__"): # Exclude special methods
                members_dict[name] = getattr(instance, name)
        return members_dict

    def print_members(self,instance):
        members_dict = self.get_members_dict(instance)
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
                "ID": to_add_record.ID
            }
            return data_dict
        elif isinstance(to_add_record, ServiceRecord):

            if (to_add_record.comments is None):
                to_add_record.comments = "None"
            

            data_dict = {
                "Name": to_add_record.name,
                "Fee": to_add_record.fee,
                "Service Code": to_add_record.service_code,
                "Provider ID": to_add_record.pID,
                "Member ID": to_add_record.mID,
                "Comments": to_add_record.comments,
                "Date Provided": to_add_record.date_provided,
                "Current DateTime": to_add_record.current_datetime
            }

            return data_dict

        return None

    def shuffle_digits(self, num):
            digits = [int(digit) for digit in str(num)]
            random.shuffle(digits)
            shuffled_num = int(''.join(map(str, digits)))
            return shuffled_num

    def generate_random_ID(self):
        timestamp = int(time.time())
        timestamp = self.shuffle_digits(timestamp)
        rand_num = random.randint(1,999999)
        timestamp = str(timestamp)
        uid = timestamp[:6] + str(rand_num)[:2]
        rand_fill = str(random.randint(1, 8))
        uid = uid[:9].ljust(9, rand_fill)

        while uid in self.IDs:
            timestamp = int(time.time())
            timestamp = self.shuffle_digits(timestamp)
            rand_num = random.randint(1,999999)
            timestamp = str(timestamp)
            uid = timestamp[:6] + str(rand_num)[:2]
            rand_fill = str(random.randint(1, 8))
            uid = uid[:9].ljust(9, rand_fill)
        
        if (uid[0] == 0):
            uid[0] = rand_fill+1

        return int(uid)
        # # Define the character set including digits and asterisks
        # char_set = string.digits 

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

        #PRE - REMOVE to_add_record.ID = self.generate_random_ID()

        data_dict["ID"] = to_add_record.ID
        file_name = to_add_record.ID
        
        
        file_name_with_prefix = "M" + str(file_name) + ".txt"
        relative_file_path = self.MemberRecords_relative_path + file_name_with_prefix

        # Check if the ID already exists
        value = self.ID_exists(file_name)
        if value ==True:

                    print("The Member already exists on File. No new record will be created.")
                    return False # Return False or an appropriate value to indicate the file already exists
        else:
            try:
                with open(relative_file_path, 'w') as file:

                    for key, value in data_dict.items():
                        file.write(f"{value}\n")

                    file.write("=\n")
        
                self.register_ID(file_name)
            
                print(f"Member Record successfully uploaded to the database")

                return True

            except:
                print("File not found:", relative_file_path)
                return False

    def add_provider_record(self, to_add_record):

        data_dict = self.package_into_dict(to_add_record)

        #POST

        data_dict["ID"] = to_add_record.ID
        file_name = to_add_record.ID

        file_name_with_prefix = "P" + str(file_name) + ".txt"
        relative_file_path = self.ProviderRecords_relative_path + file_name_with_prefix

        # Check if the ID already exists
        value = self.ID_exists(file_name)
        if value ==True:

                    print("The Provider already exists on File. No new record will be created.")
                    return False # Return False or an appropriate value to indicate the file already exists
        else:
            try:
                with open(relative_file_path, 'w') as file:

                    for key, value in data_dict.items():
                        file.write(f"{value}\n")

                    file.write("=\n")

                self.register_ID(file_name)
            
                print(f"Provider Record successfully uploaded to the database")
                print(to_add_record)

                return True
            except:
                print("File not found:", relative_file_path)
                return False
            

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
                        mr = MemberRecord(name, ID, an_address)
                        mr.is_suspended = is_suspended
                        return mr

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
                        # print("IN")
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
        # """
        # # List all existing files that match the pattern
        # existing_files = glob.glob(f"{self.ServiceRecords_relative_path}/SR*.txt")

        # # Extract the integer part from the filename, if possible
        # existing_numbers = []
        # for f in existing_files:
        #     match = re.search(r'SR(\d+)_', f)
        #     if match:
        #         existing_numbers.append(int(match.group(1)))


        # # Find the maximum number if any files exist, or start with 0 if the directory is empty
        # next_number = max(existing_numbers, default=0) + 1 if existing_numbers else 0
        # """

        self.SR_count += 1
        next_number = str(self.SR_count)
        self.update_SR_file_count()

        #Get the current date
        #now = datetime.datetime.now()
        # Format the date as MM-DD-YYYY without dashes
        #formatted_date = now.strftime("%m%d%Y")
        now = data_dict["Date Provided"]
        formatted_date = now.replace('-','')

        # Construct the new filename with the incremented number
        new_filename_with_prefix = f"SR{next_number}_{formatted_date}.txt"

        relative_file_path = self.ServiceRecords_relative_path + new_filename_with_prefix


        # Check if the ID already exists
        value = self.ID_exists(relative_file_path)
        if value ==True:

                    self.SR_count -= 1
                    self.update_SR_file_count()
                    print("The Service Record already exists on File. No new record will be created.")
                    return False # Return False or an appropriate value to indicate the file already exists
        else:
            try:
                with open(relative_file_path, 'w') as file:

                    for key, value in data_dict.items():
                        file.write(f"{value}\n")
            except:
                print("File not found:", relative_file_path)
                return False

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
        try:
            with open(self.ServiceDirectory_relative_path, 'w') as file:
                for service in self.directory:
                    file.write(f"{service[0]}:{service[1]}:{service[2]}\n")
            return True

        except:
            print("File not found:", self.ServiceDirectory_relative_path)
            return False

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
        sid_int = int(sid)
        # Assuming self.directory is the list of sublists you're traversing
        for service in self.directory:
            service_int = int(service[1])
            if service_int == sid_int and service[0]==name:
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


    
     
    def get_directory_service(self, sid):
        sid_int = int(sid)
        for service in self.directory:
            service_id_int = int(service[1])

            if service_id_int == sid_int:
                return service

        # Return None if no matching service is found
        return None

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
        



##################################################################################################
###################################### Reporter Methods ##########################################
##################################################################################################
    


    def write_weekly_member_report(self):
        sr_filepath = self.ServiceRecords_relative_path
        sr_files = os.listdir(sr_filepath)
        mID_list = []
        for file_name in sr_files:
            if os.path.isfile(os.path.join(sr_filepath, file_name)):
                if (file_name[0] == 'S'):
                    service_date = self.strip_service_date(file_name)
                    if (self.check_date(str(service_date))):
                        filepath = sr_filepath + file_name
                        curr_mID = self.get_mid(filepath)
                        # print(curr_mID)
                        if not (curr_mID in mID_list):
                            mID_list.append(curr_mID)
                        self.write_member_report(curr_mID)


    def get_mid(self, filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
            mID = lines[4]
        return int(mID)


    def write_weekly_provider_report(self):
        sr_filepath = self.ServiceRecords_relative_path
        sr_files = os.listdir(sr_filepath)
        pID_list = []
        for file_name in  sr_files:
            if os.path.isfile(os.path.join(sr_filepath, file_name)):
                if (file_name[0] == 'S'):
                    service_date = self.strip_service_date(file_name)
                    if (self.check_date(str(service_date))):
                        filepath = sr_filepath + file_name
                        curr_pID = self.get_pid(filepath)
                        # print(curr_mID)
                        if not (curr_pID in pID_list):
                            pID_list.append(curr_pID)
                        self.write_provider_report(curr_pID)
            else:
                raise ValueError("Filepath does not exist")


    def get_pid(self, filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
            pID = lines[3]
        return int(pID)

    def write_member_report(self, mID):
        if not self.ID_exists(mID):
            print("Member does not exist")
            return
        
        member = self.get_member(mID)
        record_path = str(self.MemberRecords_relative_path + 'M' + str(mID) + '.txt')
        service_file_list = self.get_service_list(record_path)

        if (len(service_file_list)) == 0:
            return
        
        current_date = datetime.datetime.now().replace(microsecond=0)
        current_date = current_date.strftime("%m-%d-%Y")
        member_report_file = str(self.MemberReports_relative_path + str(member.name) + "_" + str(current_date) + ".txt")

        with open(member_report_file, 'w') as file:
            lines = []
            lines.append("================ Member Report ============\n")
            lines.append(str(member.name + '\n'))
            lines.append(str(member.ID) + '\n')
            lines.append(str(member.street) + '\n')
            lines.append(str(member.city) + '\n')
            lines.append(str(member.state) + '\n')
            lines.append(str(member.zip) + "\n\n")
            
            lines.append("Services recieved this week: " + '\n\n')
            for service in service_file_list:
                date = self.get_service_date(service)
                hacky_list = self.get_service_info(service)
                prov_name = hacky_list["provider"].name
                service_desc = str(service[0])[:-4]
                lines.append("=====" + str(service_desc) + "=====\n")
                lines.append("Service Date: " + str(date) + '\n')
                lines.append("Provider: " + str(prov_name) + '\n')
                lines.append("Service: " + str(hacky_list["service_name"]) + '\n\n')

            file.writelines(lines)
        
    def write_provider_report(self, pID):
        if not self.ID_exists(pID):
            print("Provider does not exist")
            return
        
        provider = self.get_provider(pID)
        record_path = str(self.ProviderRecords_relative_path + 'P' + str(pID) + '.txt')
        service_file_list = self.get_service_list(record_path)

        if (len(service_file_list)) == 0:
            return
        
        current_date = datetime.datetime.now().replace(microsecond=0)
        current_date = current_date.strftime("%m-%d-%Y")
        provider_report_file = str(self.ProviderReports_relative_path + str(provider.name) + "_" + str(current_date) + ".txt")

        with open(provider_report_file, 'w') as file:
            lines = []
            num_consultations = 0
            total_fee = 0
            lines.append("================ Provider Report ============\n")
            lines.append(str(provider.name + '\n'))
            lines.append(str(provider.ID) + '\n')
            lines.append(str(provider.street) + '\n')
            lines.append(str(provider.city) + '\n')
            lines.append(str(provider.state) + '\n')
            lines.append(str(provider.zip) + "\n\n")
            
            lines.append("Services provided this week: " + '\n\n')
            for service in service_file_list:
                date = self.get_service_date(service)
                hacky_list = self.get_service_info(service)
                total_fee += float(hacky_list["fee"])
                num_consultations += 1
                service_desc = str(service[0])[:-4]
                lines.append("=====" + str(service_desc) + "=====\n")
                lines.append("Date Provided: " + str(date) + '\n')
                lines.append("Date Received: " + str(hacky_list["curr_datetime"]))
                lines.append("Member Name: " +  str(hacky_list["member"].name) + '\n')
                lines.append("Member ID: " + str(hacky_list["mID"]))
                lines.append("Service Code: " + str(hacky_list["sID"]))
                lines.append("Service Fee: " + str(hacky_list["fee"]) + '\n')


            lines.append("Total number of consultations: " + str(num_consultations) + '\n')
            lines.append("Total fee for the week: $" + str(total_fee))
            file.writelines(lines)

            self.write_eft_data(hacky_list["provider"], total_fee)


    def get_service_info(self, service):
        filepath = self.ServiceRecords_relative_path
        filepath += service[0]
        with open(filepath, 'r') as file:
            lines = file.readlines()
            service_name = lines[0]
            fee = lines[1]
            sID = lines[2]
            pID = lines[3]
            mID = lines[4]
            comments = lines[5]
            date_provided = lines[6]
            curr_datetime = lines[7]

        provider = self.get_provider(pID)
        member = self.get_member(mID)

        hacky_list = {
            "service_name" : service_name, 
            "fee" : fee, 
            "sID" : sID, 
            "pID" : pID, 
            "mID" : mID, 
            "comments" : comments, 
            "date_provided" : date_provided, 
            "curr_datetime" : curr_datetime, 
            "provider" : provider, 
            "member" : member}
        
        return hacky_list


    def get_service_date(self, service):
        date = datetime.datetime.strptime(service[1], "%Y-%m-%d")
        date = date.strftime("%m-%d-%Y")
        return date


    def get_service_list(self, record_path):
        service_file_list = {}
        # print(record_path)
        if os.path.exists(record_path):
            with open(record_path, 'r') as rec_file:
                lines = rec_file.readlines()[7:]
                for line in lines:
                    if line[0] == 'S':
                        line = line[:-1]
                        service_date = self.strip_service_date(line)
                        if self.check_date(service_date):
                            service = line
                            service_datetime = self.convert_service_date(service_date)
                            service_file_list[service] = str(service_datetime)
                
        else:
            raise ValueError("Record does not exist in database")
        

        service_file_list = sorted(service_file_list.items(), key=lambda x: datetime.datetime.strptime(x[1], "%Y-%m-%d"))
        # print(service_file_list)
        return service_file_list        
    
  
    def check_date(self, service_date_string):
        service_datetime = self.convert_service_date(service_date_string)
        current_date_time = datetime.datetime.now()
        week_start = current_date_time - datetime.timedelta(days=7)
        week_start = week_start.date()
        if service_datetime < week_start:
            return False
        else:

            return True


    def convert_service_date(self, service_date_string):
        year = int(service_date_string[-4:])
        month = int(service_date_string[0:2])
        day = int(service_date_string[2:4])
        service_datetime = datetime.date(year, month, day)
        return service_datetime

    def strip_service_date(self, line):
        service_date = line.split('_', 1)[-1]
        service_date = service_date[:-4]
        return service_date

    def get_member(self, mID):
        mID = int(mID)
        # Use placeholder values that pass the Address validation
        minimal_address = Address("NA", "NA", "NA", "97205")
        
        # Attempt to create a ProviderRecord with placeholder values
        # Important: Adjust this based on what ProviderRecord and Address validations allow
        temp_member = MemberRecord("NA", mID, minimal_address)
        
        # Fetch the provider record
        member_record = self.get_member_record(temp_member)
        return member_record

    def get_provider(self, provider_id):
        provider_id = int(provider_id)
        # Use placeholder values that pass the Address validation
        minimal_address = Address("NA", "NA", "NA", "97205")
        
        # Attempt to create a ProviderRecord with placeholder values
        # Important: Adjust this based on what ProviderRecord and Address validations allow
        temp_provider = ProviderRecord("NA", provider_id, minimal_address)
        
        # Fetch the provider record
        provider_record = self.get_provider_record(temp_provider)
        
        return provider_record


    def get_pid_list(self):
        sr_filepath = self.ServiceRecords_relative_path
        sr_files = os.listdir(sr_filepath)
        pID_list = []
        for file_name in  sr_files:
            if os.path.isfile(os.path.join(sr_filepath, file_name)):
                if (file_name[0] == 'S'):
                    service_date = self.strip_service_date(file_name)
                    if (self.check_date(str(service_date))):
                        filepath = sr_filepath + file_name
                        curr_pID = self.get_pid(filepath)
                        # print(curr_mID)
                        if not (curr_pID in pID_list):
                            pID_list.append(curr_pID)
                        
            else:
                raise ValueError("Filepath does not exist")
        return pID_list
            
    def write_summary_report(self):
        num_providers = 0
        num_consultations = 0
        overall_fee = 0.0
        pID_list = self.get_pid_list()
        curr_date = datetime.date.today()
        curr_date = curr_date.strftime("%m-%d-%Y")
        filepath = self.SummaryReports_relative_path + str(curr_date) + ".txt"
        with open(filepath, 'w') as file:
            lines = []
            for pID in pID_list:
                provider = self.get_provider(pID)
                record_path = str(self.ProviderRecords_relative_path + 'P' + str(pID) + '.txt')
                service_file_list = self.get_service_list(record_path)
                fee = self.get_total_fee(service_file_list)
                fee = "{:.2f}".format(fee)
                lines.append("Provider: " + str(provider.name) + '\n')
                lines.append("Number of Consultations: " + str(len(service_file_list)) + '\n')
                lines.append("Total fee: $" + str(fee) + '\n\n')
                num_providers += 1
                num_consultations += (len(service_file_list))
                overall_fee += float(fee)

            num_con_str = "Total number of Providers who provided services this week: " + str(num_providers) + '\n'
            num_prov_str = "Total number of consultations this week: " + str(num_consultations) + '\n'
            fee_str = "Overall fee total for this week: " + str(overall_fee) + '\n'
            lines.append(num_con_str)
            lines.append(num_prov_str)
            lines.append(fee_str)
            file.writelines(lines)

        print(num_con_str)
        print(num_prov_str)
        print(fee_str)


    def get_total_fee(self, service_file_list):
        total_fee = 0
        for service in service_file_list:
            hacky_list = self.get_service_info(service)
            total_fee += float(hacky_list["fee"])
        return total_fee
        

    def write_eft_data(self, provider, payment_owed):
        filepath = self.EFTDataReports_relative_path + str(provider.name) + "_" + "EFT.txt"
        with open(filepath, 'w') as file:
            lines = []
            lines.append(str(provider.name) + '\n')
            lines.append(str(provider.ID) + '\n')
            payment_owed = "{:.2f}".format(payment_owed)
            lines.append("$" + str(payment_owed))

            file.writelines(lines)
        

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

data = DatabaseManager()
serve= ServiceRecord("123456",101027954,100112136,"01-23-2024","destroyer of worlds", 123)
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






