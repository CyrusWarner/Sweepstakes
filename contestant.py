import user_interface


class Contestant:
    def __init__(self):
        self.first_name = user_interface.get_user_input_string("What is your first name?")
        self.last_name = user_interface.get_user_input_string("What is your last name?")
        self.email = user_interface.get_user_input_string("Please enter your email")
        self.registration_number = user_interface.get_user_input_number

    def notify(self, winner):
        pass