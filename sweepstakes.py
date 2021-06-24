from contestant import Contestant
from user_interface import User_Interface

class Sweepstakes:
    def __init__(self):
        self.name = ""
        self.contestants = {
        }

    def register_contestant(self, contestant):
        self.contestants[contestant.registration_number] = contestant


    def menu(self, sweepstakes):
        User_Interface.display_sweepstakes(sweepstakes)
        sweepstake_object = User_Interface.sweepstakes_selection_menu(sweepstakes)
        User_Interface.display_sweepstakes_menu_options(sweepstake_object)
        choose_option_sweepstake = User_Interface.get_user_input_number("Please select an option from the menu")
        if choose_option_sweepstake == 1:
            User_Interface.display_contestants(self.contestants)
        if choose_option_sweepstake == 2:
            get_user_first_name = User_Interface.get_user_input_string("enter your first name")
            get_user_last_name = User_Interface.get_user_input_string("enter your last name")
            get_user_email = User_Interface.get_user_input_string("enter your email")
            new_contestant = Contestant(get_user_first_name, get_user_last_name, get_user_email, 1)
            self.register_contestant(new_contestant)
        if choose_option_sweepstake == 3:
            pass
        if choose_option_sweepstake == 4:
            User_Interface.exit_menu()


    def view_contestants(self):
        User_Interface.display_contestants(self.contestants)

    def pick_winner(self):
        pass

