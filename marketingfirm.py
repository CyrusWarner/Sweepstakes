from sweepstakes import Sweepstakes
from user_interface import User_Interface

class MarketingFirm:
    def __init__(self):
        self.name = "Dynamic"
        self.sweepstakes_storage = ["Unity Scholarship", "Lottery", "Weekly Sweepstake", "Yearly sweepstake"]

    def create_sweepstakes(self):
        new_sweepstakes = User_Interface.get_user_input_string("\nPlease enter the name for the new sweepstakes.")
        self.sweepstakes_storage.append(new_sweepstakes)

    def change_marketing_firm_name(self):
        new_firm_name = User_Interface.get_user_input_string("\nPlease enter the name for the new marketing firm.")
        self.name = new_firm_name

    def select_sweepstakes(self):
        user_number = get_user_input_number("Please Choose a sweepstakes")
        index = 0
        for each in self.sweepstakes_storage:
            print(f"{index}\t{each}")
            index += 1
            if user_number == each:
                return each

    def menu(self):
        User_Interface.display_marketing_firm_menu_options(self.name)
        user_input = User_Interface.get_user_input_number("\nPlease Choose from the menu\n")
        if user_input == 0:
            User_Interface.display_sweepstakes(self.sweepstakes_storage)
            User_Interface.sweepstakes_selection_menu(self.sweepstakes_storage)
        if user_input == 1:
            self.create_sweepstakes()
        if user_input == 2:
            self.change_marketing_firm_name()
        if user_input == 3:
            User_Interface.exit_sweepstakes()

    def view_sweepstakes(self):
        User_Interface.display_sweepstakes(self.sweepstakes_storage)
