from Records import *

class DatabaseMgr:
    def __init__(self, *args) -> None:
        arg_len = len(args)
        if(arg_len > 2):
            raise ValueError("Incorrect number of arguments when initializing DatabaseMgr")
        elif(arg_len == 0):
            self._default_constructor()
        elif(arg_len == 1):
            self._copy_constructor(args[0])
        elif(arg_len == 2):
            self._param_constructor(args[0], args[1])

    def _default_constructor(self):
        self._member_dict = {}
        self._provider_dict = {}
        self._service_dict = {}
        self._active_members = []
        self._active_providers = []

    def _copy_constructor(self, other: object) -> object:
        self._member_dict = other._member_dict
        self._provider_dict = other._provider_dict
        self._service_dict = other._service_dict
        self._active_members = other._active_members
        self._active_providers = other._active_providers

        return other
    
    def _param_constructor(self, member_ids, provider_ids):
        self._member_dict = member_ids
        self._provider_dict = provider_ids
        self._service_dict = {}
        self._active_members = []
        self._active_providers = []
        
    def _display_service(self): #display services from service dictionary
        for key, value in self._service_dict.items():
            print(key, ":", value)

    def _populate_dict(self, filename, dict_name): #populate dict_name with information in file
        try:
            with open(filename, 'r') as file:
                for line in file:
                    key, value = line.strip().split(':') #
                    dict_name[key.strip()] = value.strip()

        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Error reading from file.")

    def _load_member_record(self, mID):
        return
    
    def _load_provider_record(self, pID):
        return

    def _get_member(self, mID):
        for member in self._active_members:
            if(member._ID == mID):
                return member

        print("Member with ID", mID, "not found.")
        return
    
    def _add_member(self, new_member):
        self._active_members.append(new_member)
        return
    
    def _edit_member(self, mID):
        return
    
    def _remove_member(self, mID):
        for member in self._active_members:
            if(member._ID == mID):
                self._active_members.remove(member)
                break
        return
    
    def _find_member(self, mID) -> object: #difference between get_member() and find_member()?
        return #found member

    def _get_provider(self, pID):
        for provider in self._active_provider:
            if(provider._ID == pID):
                return provider

        print("Provider with ID", pID, "not found.")
        return
    
    def _add_provider(self, new_provider):
        self._active_providers.append(new_provider)
        return
    
    def _edit_provider(self, pID):
        return
    
    def _remove_provider(self, pID):
        for provider in self._active_providers:
            if(provider._ID == pID):
                self._active_members.remove(provider)
                break
        return
    
    def _find_provider(self, pID) -> object:
        return #found provider
   