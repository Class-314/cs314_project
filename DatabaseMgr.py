from Records import *

class DatabaseMgr:
    def __init__(self, *args) -> None:
        arg_len = len(args)
        if(arg_len > 1):
            raise ValueError("Incorrect number of arguments when initializing DatabaseMgr")
        elif(arg_len == 0):
            self._default_constructor()
        elif(arg_len == 1):
            self._copy_constructor(args[0])

    def _default_constructor(self):
        self._service_dir = []
        self._active_members = []
        self._active_providers = []

    def _copy_constructor(self, other: object) -> object:
        if not (isinstance(other, DatabaseMgr)):
            raise ValueError("Other is not of type DatabaseMgr in copy constructor")
        self._service_dir = other._service_dir
        self._active_members = other._active_members
        self._active_providers = other._active_providers

        return self
    
    def _display_service(self): #display services from service dictionary
        for service in self._service_dir:
            print(service)

    def _populate_dir(self, filename): #populate service_dir with services in file
        try:
            with open(filename, 'r') as file:
                for line in file: #update for a list, need file format
                    #key, value = line.strip().split(':') #
                    #dict_name[key.strip()] = value.strip()
                    break

        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Error reading from file.")

    def _load_member_record(self, mID): #load member's file by mID?
        return
    
    def _load_provider_record(self, pID): #load provider's file by pID?
        return

    def _get_member(self, mID) -> object:
        for member in self._active_members:
            if(member._ID == mID):
                return member

        print("Member with ID", mID, "not found.")
    
    def _add_member(self, new_member):
        self._active_members.append(new_member)
        return
    
    def _edit_member(self, mID):
        for member in self._active_members:
            if(member._ID == mID):
                #TODO edit info
                return

        print("Member with ID", mID, "not found.")
    
    def _remove_member(self, mID):
        for member in self._active_members:
            if(member._ID == mID):
                self._active_members.remove(member)
                break
        return
    
    def _find_member(self, mID) -> bool:
        for member in self._active_members:
            if(member._ID == mID):
                return True #mID found

        print("Member ID", mID, "not found.") 
        return False #mID does not exist

    def _get_provider(self, pID) -> object:
        for provider in self._active_provider:
            if(provider._ID == pID):
                return provider

        print("Provider with ID", pID, "not found.")
    
    def _add_provider(self, new_provider):
        self._active_providers.append(new_provider)
        return
    
    def _edit_provider(self, pID):
        for provider in self._active_provider:
            if(provider._ID == pID):
                #TODO edit info
                return

        print("Provider with ID", pID, "not found.")
    
    def _remove_provider(self, pID):
        for provider in self._active_providers:
            if(provider._ID == pID):
                self._active_members.remove(provider)
                return

        print("Provider with ID", pID, "not found.")
        return
    
    def _find_provider(self, pID) -> bool:
        for provider in self._active_providers:
            if(provider._ID == pID):
                return True #pID found

        print("Provider ID", pID, "not found.")
        return False #pID does not exist
   