from modules import atm

def describe_atm():
    def should_validate_true():
       """Expect validate to be true"""
       assert atm.validate() == True