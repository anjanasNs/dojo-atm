from modules import atm

def describe_atm():
    def should_return_invalid_on_input_0():
       """Expect input 0 to be False"""
       assert atm.validate_input(0) == False
    
    def should_return_valid_on_input_type_integer():
       """Expect input integer to be True"""
       assert atm.validate_input(2) == True

    def should_return_invalid_on_input_type_string():
       """Expect input string to be False"""
       assert atm.validate_input('test') == False

    def should_return_invalid_on_input_type_boolean():
       """Expect input boolean to be False"""
       assert atm.validate_input(False) == False

    def should_return_invalid_on_input_type_float():
       """Expect input float to be False"""
       assert atm.validate_input(1.543) == False

   