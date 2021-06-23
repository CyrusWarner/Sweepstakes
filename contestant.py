from user_interface import User_Interface
import random

class Contestant:
    def __init__(self, first_name, last_name, email, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration_number = registration_number
        
    def notify(self, winner):
        pass
  
"""
    def new_user(self):
        self.first_name = get_user_input_string("Please enter your first name.")
        self.last_name = get_user_input_string("Please enter your last name.")
        self.email = get_user_input_string("Please enter your email.")
        self.registration_number = 7 #Try to find a way to add one to end of dictionary rgistration number

"""