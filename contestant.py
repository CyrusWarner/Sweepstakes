from user_interface import User_Interface

class Contestant:
    def __init__(self, first_name, last_name, email, contestant_dictionary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration_number = 1 + len(contestant_dictionary)
        
    def notify(self, winner):
        pass
    
