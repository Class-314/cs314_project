import datetime

##################################
#
# ServiceRecord (Base Class)
#
##################################

class ServiceRecord:
    def __init__(self, *args):
        self._comments = None
        arg_len = len(args)
        if (arg_len != 0 and arg_len != 1 and arg_len != 6 and arg_len !=7): # Check to make sure valid number of arguments
            raise ValueError("Incorrect number of arguments when initializing ServiceRecord")
        if (arg_len == 1): # 1 argument: args[0] should be another ServiceRecord object, error checking in _copy_constructor
            self._copy_constructor(args[0])
        elif (arg_len == 6): 
            self._param_constructor(args[0], args[1], args[2], args[3], args[4], args[5])
        elif (arg_len == 7):
            self._comments = str(args[4])
            strip_table = str.maketrans("", "", "\t\n\v")
            self._comments = self._comments.translate(strip_table)
            self._param_constructor(args[0], args[1], args[2], args[3], args[5], args[6])
        else: # No arguments, default constructor, should generally not be used unless you're planning on filling up the members with setters immediately after
            self._default_constructor()

    # Default Constructor
    def _default_constructor(self):
        self._name = None
        self._fee = None
        self._service_code = None
        self._mID = None
        self._pID = None
        self._comments = None 
        self._date_provided = None
        self._current_datetime = datetime.datetime.now().replace(microsecond=0)
        self._current_datetime = self._current_datetime.strftime("%m-%d-%Y %H:%M:%S")

    # Copy Constructor
    def _copy_constructor(self, other):
        if not (isinstance(other, ServiceRecord)):
            raise ValueError("Other is not of type ServiceRecord in copy constructor")
        self.name = other._name
        self._fee = other._fee
        self._service_code = other._service_code
        self._mID = other._mID
        self._pID = other._pID
        self._comments = other._comments
        self._date_provided = other._date_provided
        self._current_datetime = other._current_datetime

    # Paramaterized Constructor
    def _param_constructor(self, a_service_code, a_pID, a_mID, a_date, a_name, a_fee):
            self.name = a_name
            self._fee = a_fee
            self.service_code = a_service_code
            self.mID = a_mID
            self.pID = a_pID
            self.date_provided = self.convert_date(a_date)
            self._current_datetime = datetime.datetime.now().replace(microsecond=0)
            self._current_datetime = self._current_datetime.strftime("%m-%d-%Y %H:%M:%S")



    def convert_date(self, input_string):
        input_string = str(input_string)
        month, day, year = map(int, input_string.split('-'))
        converted = datetime.date(year, month, day)
        converted = converted.strftime("%m-%d-%Y")
        return converted

    # Getters/Setters using decorators for extra protection
            
    @property
    def service_code(self):
        return int(self._service_code)
    
    @property
    def fee(self):
        return int(self._fee)
    
    @property
    def comments(self):
        return str(self._comments)
    

    

    @service_code.setter
    def service_code(self, new_sc):
        if (len(str(new_sc)) != 6): # cast to str to check length to guarantee 5 digits, there's probably a cleaner way to do this
            raise ValueError("Invalid input when setting service code")
        new_sc = int(new_sc)
        self._service_code = new_sc


    @property
    def name(self):
        strip_table = str.maketrans("", "", "\t\n\v")
        self._name = self._name.translate(strip_table)
        return str(self._name)
    
    @name.setter
    def name(self, new_name):
        strip_table = str.maketrans("", "", "\t\n\v")
        self._name = new_name.translate(strip_table)


    @property
    def mID(self):
        return int(self._mID)
    

    @mID.setter
    def mID(self, new_id):
        if (len(str(new_id)) != 9): # cast to str to check length to guarantee 5 digits, there's probably a cleaner way to do this
            raise ValueError("Invalid input when setting service code")
        new_id = int(new_id)
        self._mID = new_id
    
    @property
    def pID(self):
        return int(self._pID)

    @pID.setter
    def pID(self, new_id):
        if (len(str(new_id)) != 9):
            raise ValueError("Invalid input when setting service code")
        new_id = int(new_id)
        self._pID = new_id

    @property
    def date_provided(self):
        return str(self._date_provided)
    
    @date_provided.setter
    def date_provided(self, new_date):
        #TODO Date error checking
        if (len(str(new_date)) != 10):
            raise ValueError("Invalid input when setting date provided")
        self._date_provided = new_date

    @property
    def current_datetime(self):
        return str(self._current_datetime)
    
    @current_datetime.setter
    def current_datetime(self, new_datetime):
        self._current_datetime = new_datetime



    # str overload, similar to << overload in C++
    # lets us specify exactly what comes out when someone calls print(object)
    def __str__(self):
        string = str(str(self.name) + '\n' + str(self._fee) + '\n' + str(self._service_code) + "\nProvider ID: " + str(self._pID) + "\nMember ID: " + str(self._mID))
        string += str("\nDate Provided: " + str(self._date_provided) + "\nDate Submitted: " + str(self._current_datetime))
        if not (self._comments is None):
            string += str('\n' + str(self._comments))
        return string
    
    def __eq__(self, other):
        if not (isinstance(other, ServiceRecord)):
            raise ValueError("Trying to compare object not of type ServiceRecord")
        return (self._service_code == other._service_code and self._pID == other._pID and self._mID == other._mID and self._comments == other._comments and self._date_provided == other._date_provided and self._current_datetime == other._current_datetime)
    
    def __ne__(self, other):
        if not (isinstance(other, ServiceRecord)):
            raise ValueError("Trying to compare object not of type ServiceRecord")
        return (not (self == other))


##################################
#
# Address (Base Class)
#
##################################

class Address:
    # Python default constructor
    # Added some additional checks so the objects can function a little more like C++ on instantiation
    def __init__(self, *args):
        arg_len = len(args)
        if (arg_len != 0 and arg_len != 1 and arg_len != 4): # Check to make sure valid number of arguments
            raise ValueError("Incorrect number of arguments when initializing Address")
        if (arg_len == 1): # 1 argument: args[0] should be another Address object, error checking in _copy_constructor
            self._copy_constructor(args[0])
        elif (arg_len == 4): # 4 arguments: args[0:4] should be street, city, state, zip in that order
            self._param_constructor(args[0], args[1], args[2], args[3])
        else: # No arguments, default constructor, should generally not be used unless you're planning on filling up the members with setters immediately after
            self._default_constructor()

    # Default Constructor
    def _default_constructor(self):
        self._street = None
        self._city = None
        self._state = None
        self._zip = None

    # Copy Constructor
    def _copy_constructor(self, other):
        if not (isinstance(other, Address)):
            raise ValueError("Other is not of type Address in copy constructor")
        self.street = other.street
        self.city = other.city
        self.state = other.state
        self.zip = other.zip

    # Paramaterized Constructor
    # All error checking is in the setters, implicitly called when not using the underscore. So self.street = a_street actually calls the street setter
    def _param_constructor(self, a_street, a_city, a_state, a_zip):
            self.street = a_street
            self.city = a_city
            self.state = a_state 
            self.zip = a_zip 

    # Getters/Setters using decorators for extra protection
    # This allows anyone using this class to access the data members directly without the protected ._value
    # The benefit is this allows us to add extra protections when they do, like making sure the values are cast to their expected type
    @property
    def street(self):
        strip_table = str.maketrans("", "", "\t\n\v")
        self._street = self._street.translate(strip_table)
        return str(self._street)
    
    # Setter decorator works the same. Now when someone using this class types a1.street = 1234, this will automatically cast it to a string
    # title() capitalizes each word in the string
    # each setter handles converting to the right type, changing formatting as needed and error checking
    @street.setter
    def street(self, new_street):
        strip_table = str.maketrans("", "", "\t\n\v")
        self._street = new_street.translate(strip_table)
        self._street = str(self._street).title() 

    @property
    def city(self):
        strip_table = str.maketrans("", "", "\t\n\v")
        self._city = self._city.translate(strip_table)
        return str(self._city)
    
    @city.setter
    def city(self, new_city):
        strip_table = str.maketrans("", "", "\t\n\v")
        self._city = new_city.translate(strip_table)
        self._city = str(self._city.title())


    @property
    def state(self):
        strip_table = str.maketrans("", "", "\t\n\v")
        self._state = self._state.translate(strip_table)
        return str(self._state)

    @state.setter
    def state(self, new_state):
        if (len(new_state) != 2):
            raise ValueError("Invalid input when setting state")
        strip_table = str.maketrans("", "", "\t\n\v")
        self._state = new_state.translate(strip_table)
        self._state = str(self._state).upper() #protection in case someone does something like a1.state = "or"


    @property
    def zip(self):
        return int(self._zip)
    

    @zip.setter
    def zip(self, new_zip):
        if (len(str(new_zip)) != 5): # cast to str to check length to guarantee 5 digits, there's probably a cleaner way to do this
            raise ValueError("Invalid input when setting zip")
        new_zip = int(new_zip)
        self._zip = new_zip


    # str overload, similar to << overload in C++
    # lets us specify exactly what comes out when someone calls print(object)
    def __str__(self):
        if (self._street == None or self._city == None or self._zip == None or self._state == None):
            raise ValueError("One or more values is None in __str__")
        string = str(self._street + '\n' + self._city + '\n' + str(self._zip) + '\n' + self._state )
        return string
    
    def __eq__(self, other):
        if not (isinstance(other, Address)):
            raise ValueError("Trying to compare object not of type Address")
        return (self._street == other._street and self._city == other._city and self._state == other._state and self._zip == other._zip)
    
    def __ne__(self, other):
        if not (isinstance(other, Address)):
            raise ValueError("Trying to compare object not of type Address")
        return (self._street != other._street or self._city != other._city or self._state != other._state or self._zip == other._zip)

##################################
#
# UserRecord : Address
#
##################################

class UserRecord(Address):
    def __init__(self, *args):
        super(UserRecord, self).__init__()
        arg_len = len(args)
        if (arg_len != 0 and arg_len != 1 and arg_len != 3 and arg_len != 6): # Check to make sure valid number of arguments
            raise ValueError("Incorrect number of arguments when initializing UserRecord")
        
        if (arg_len == 1): # 1 argument: args[0] should be another Address object, error checking in _copy_constructor
            self._copy_constructor(args[0])

        elif (arg_len == 3): # 3 arguments: args[0:3] should be name, ID, address in that order
            self._param_constructor(args[0], args[1], args[2])

        elif (arg_len == 6):
            address = Address(args[2], args[3], args[4], args[5])
            self._param_constructor(args[0], args[1], address)

        else: # No arguments, default constructor, should generally not be used unless you're planning on filling up the members with setters immediately after
            self._default_constructor()

    # Default Constructor
    def _default_constructor(self):
        super()._default_constructor()
        self._name = None
        self._ID = None
        self.services = []

    # Copy Constructor
    def _copy_constructor(self, other):
        if not (isinstance(other, UserRecord)):
            raise ValueError("Other is not of type UserRecord in copy constructor")
        super()._copy_constructor(other)
        self.name = other.name
        self.ID = other.ID
        self.services = []
    

    # Paramaterized Constructor
    def _param_constructor(self, a_name, a_ID, a_address):
            super()._copy_constructor(a_address)
            self.name = a_name
            self.ID = a_ID


    def add_service(self, new_service):
        if not (isinstance(new_service, ServiceRecord)):
            raise TypeError("Trying to insert non-ServiceRecord object")
        self.services.append(new_service)

    def display_services(self):
        for service in self.services:
            print(service)
            print("====")

    def __str__(self):
        string = str(self._name + ": " + str(self._ID) + '\n')
        string += super().__str__()
        return string
    
    def __eq__(self, other):
        if not (isinstance(other, UserRecord)):
            raise ValueError("Trying to compare object not of type UserRecord")
        return ((self._name == other._name and self._ID == other._ID) and super().__eq__(other))
    
    def __ne__(self, other):
        if not (isinstance(other, UserRecord)):
            raise ValueError("Trying to compare object not of type UserRecord")
        return ((self._name != other._name or self._ID != other._ID) or super().__ne__(other))
    
    @property
    def name(self):
        strip_table = str.maketrans("", "", "\t\n\v")
        self._name = self._name.translate(strip_table)
        return str(self._name).title()
    
    @name.setter
    def name(self, new_name):
        if not (isinstance(new_name, str)):
            raise ValueError("Invalid type when setting name")
        strip_table = str.maketrans("", "", "\t\n\v")
        self._name = new_name.translate(strip_table)
        self._name = str(self._name).title()

    @property
    def ID(self):
        return int(self._ID)
    
    @ID.setter
    def ID(self, new_id):
        if (len(str(new_id)) != 9):
            raise ValueError("Invalid number of digits in set ID")
        self._ID = int(new_id)


        
##################################
#
# MemberRecord : UserRecord
#
##################################
        
class MemberRecord(UserRecord):
    def __init__(self, *args):
        super(MemberRecord, self).__init__()
        arg_len = len(args)
        if (arg_len != 0 and arg_len != 1 and arg_len != 3 and arg_len != 6): # Check to make sure valid number of arguments
            raise ValueError("Incorrect number of arguments when initializing UserRecord")
        
        if (arg_len == 1): # 1 argument: args[0] should be another Address object, error checking in _copy_constructor
            self._copy_constructor(args[0])

        elif (arg_len == 3): # 3 arguments: args[0:3] should be name, ID, address in that order
            self._param_constructor(args[0], args[1], args[2])

        elif (arg_len == 6):
            address = Address(args[2], args[3], args[4], args[5])
            self._param_constructor(args[0], args[1], address)

        else: # No arguments, default constructor, should generally not be used unless you're planning on filling up the members with setters immediately after
            self._default_constructor()

    # Default Constructor
    def _default_constructor(self):
        super()._default_constructor()
        self._is_suspended = False 

    # Copy Constructor
    def _copy_constructor(self, other):
        if not (isinstance(other, MemberRecord)):
            raise ValueError("Other is not of type MemberRecord in copy constructor")
        super()._copy_constructor(other)
        self._is_suspended = other._is_suspended
    

    # Paramaterized Constructor
    def _param_constructor(self, a_name, a_ID, a_address):
            super()._param_constructor(a_name, a_ID, a_address)
            self._is_suspended = False

    def suspend_membership(self):
        self.is_suspended = True

    def activate_membership(self):
        self.is_suspended = False

    def convert_status(self):
        if (self._is_suspended == True):
            return "Suspended"
        else:
            return "Active"

    @property
    def is_suspended(self):
        return bool(self._is_suspended)
    
    @is_suspended.setter
    def is_suspended(self, new_status):
        if not (isinstance(new_status, bool)):
            raise ValueError("Invalid type when setting suspension status")
        self._is_suspended = new_status

    def __str__(self):
        string = super().__str__()
        string += "\nMembership Status: " + str(self.convert_status())
        return string
    
    def __eq__(self, other):
        if not (isinstance(other, MemberRecord)):
            raise ValueError("Trying to compare object not of type MemberRecord")
        return super().__eq__(other)
    
    def __ne__(self, other):
        if not (isinstance(other, MemberRecord)):
            raise ValueError("Trying to compare object not of type MemberRecord")
        return super().__ne__(other)
    


    #TODO: Add service list functionality


##################################
#
# ProviderRecord : UserRecord
#
##################################
    
class ProviderRecord(UserRecord):

    def __init__(self, *args):
        super(ProviderRecord, self).__init__()
        arg_len = len(args)
        if (arg_len != 0 and arg_len != 1 and arg_len != 3 and arg_len != 6): # Check to make sure valid number of arguments
            raise ValueError("Incorrect number of arguments when initializing UserRecord")
        
        if (arg_len == 1): # 1 argument: args[0] should be another Address object, error checking in _copy_constructor
            self._copy_constructor(args[0])

        elif (arg_len == 3): # 3 arguments: args[0:3] should be name, ID, address in that order
            self._param_constructor(args[0], args[1], args[2])

        elif (arg_len == 6):
            address = Address(args[2], args[3], args[4], args[5])
            self._param_constructor(args[0], args[1], address)

        else: # No arguments, default constructor, should generally not be used unless you're planning on filling up the members with setters immediately after
            self._default_constructor()

    # Default Constructor
    def _default_constructor(self):
        super()._default_constructor()
        self._num_consultations = 0
        self._total_payment = 0.00

    # Copy Constructor
    def _copy_constructor(self, other):
        if not (isinstance(other, ProviderRecord)):
            raise ValueError("Other is not of type ProviderRecord in copy constructor")
        super()._copy_constructor(other)
        self._num_consultations = other.num_consultations
        self._total_payment = other.total_payment
    

    # Paramaterized Constructor
    def _param_constructor(self, a_name, a_ID, a_address):
            super()._param_constructor(a_name, a_ID, a_address)
            self._num_consultations = 0
            self._total_payment = 0.00
    


    def add_payment(self, new_payment):
        new_payment = float(new_payment) # Will force a TypeError if its the wrong type, but will convert ints to floats
        self.total_payment += new_payment
    
    def add_consultation(self):
        self.num_consultations += 1

    def __str__(self):
        string = super().__str__()
        # string += ("Consultations: " + str(self.num_consultations))
        # string += ("\nTotal Payment Due: " + str(self.total_payment))
        return string

    def __eq__(self, other):
        if not (isinstance(other, ProviderRecord)):
            raise ValueError("Trying to compare object not of type ProviderRecord")
        return super().__eq__(other)
    
    def __ne__(self, other):
        if not (isinstance(other, ProviderRecord)):
            raise ValueError("Trying to compare object not of type ProviderRecord")
        return super().__ne__(other)

    @property
    def num_consultations(self):
        return int(self._num_consultations)
    
    @num_consultations.setter
    def num_consultations(self, new_num):
        if not (isinstance(new_num, int)):
            raise ValueError("Invalid type when setting num consultations")
        self._num_consultations = new_num

    @property
    def total_payment(self):
        return float(self._total_payment)
    
    @total_payment.setter
    def total_payment(self, new_amount):
        print(new_amount)
        if not (isinstance(new_amount, float)):
            raise ValueError("Invalid type when setting total payment")
        self._total_payment = new_amount