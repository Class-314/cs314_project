
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
        return str(self._street)
    
    # Setter decorator works the same. Now when someone using this class types a1.street = 1234, this will automatically cast it to a string
    # title() capitalizes each word in the string
    # each setter handles converting to the right type, changing formatting as needed and error checking
    @street.setter
    def street(self, new_street):
        self._street = str(new_street).title() 

    @property
    def city(self):
        return str(self._city)
    
    @city.setter
    def city(self, new_city):
        self._city = str(new_city).title()


    @property
    def state(self):
        return str(self._state)

    @state.setter
    def state(self, new_state):
        if (len(new_state) != 2):
            raise ValueError("Invalid input when setting state")
        self._state = str(new_state).upper() #protection in case someone does something like a1.state = "or"


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
        self._services = []

    # Copy Constructor
    def _copy_constructor(self, other):
        if not (isinstance(other, UserRecord)):
            raise ValueError("Other is not of type Address in copy constructor")
        super()._copy_constructor(other)
        self.name = other.name
        self.ID = other.ID
        #TODO: setup service insert when ServiceRecords have been made
        self._services = []
    

    # Paramaterized Constructor
    def _param_constructor(self, a_name, a_ID, a_address):
            super()._copy_constructor(a_address)
            self.name = a_name
            self.ID = a_ID

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
        return str(self._name).title()
    
    @name.setter
    def name(self, new_name):
        if not (isinstance(new_name, str)):
            raise ValueError("Invalid type when setting name")
        self._name = str(new_name).title()

    @property
    def ID(self):
        return int(self._ID)
    
    @ID.setter
    def ID(self, new_id):
        if (len(str(new_id)) != 6):
            raise ValueError("Invalid number of digits in set ID")
        self._ID = int(new_id)

    #TODO: Add service list functionality
        
##################################
#
# MemberRecord : UserRecord
#
##################################
        
class MemberRecord(UserRecord):
    def __init__(self, *args):
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
        string += ("Consultations: " + str(self.num_constultations))
        string += ("Total Payment Due: " + str(self.total_payment))


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