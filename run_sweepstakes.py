from user_interface import User_Interface
from sweepstakes import Sweepstakes
from contestant import Contestant
from marketingfirm import MarketingFirm

class run_Sweepstakes:
    def __init__(self):
        pass
    
    
    def run_simulation(self):
        User_Interface.main_menu()
        user_number_input = User_Interface.get_user_input_number("Please choose from the menu")
        if user_number_input == 0:
            new = Contestant.user()
        if user_number_input == 1:
            marketing_firm = MarketingFirm()
            marketing_firm.view_sweepstakes()
            self.run_simulation()
        if user_number_input == 2:
            marketing_firm = MarketingFirm()
            marketing_firm.menu()
        if user_number_input == 3:
            sweepstakes = Sweepstakes()
            sweepstakes.menu()
        if user_number_input == 4:
            sweepstakes = Sweepstakes()
            sweepstakes.view_contestants()
        if user_number_input == 5:
            User_Interface.display_exit()

