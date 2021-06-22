from sweepstakes import Sweepstakes
import user_interface

class MarketingFirm:
    def __init__(self):
        self.name = "Dynamic"
        self.sweepstakes_storage = ("Scholarship", "Lottery", "Weekly Sweepstake", "Yearly sweepstake")

    def create_sweepstakes(self):
        new_sweepstakes = get_user_input_string("Please enter the name for the new sweepstakes.")
        self.sweepstakes_storage.append(new_sweepstakes)

    def change_marketing_firm_name(self):
        new_firm_name = get_user_input_string("Please enter the name for the new marketing firm.")
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
        pass
