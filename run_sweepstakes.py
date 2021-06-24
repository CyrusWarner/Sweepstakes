from user_interface import User_Interface
from sweepstakes import Sweepstakes
from contestant import Contestant
from marketingfirm import MarketingFirm

class run_Sweepstakes:
    def __init__(self):
        pass
    
    
    def run_simulation(self):
        User_Interface.main_menu()
        marketing_firm = MarketingFirm()
        sweepstakes = Sweepstakes()
        user_number_input = User_Interface.get_user_input_number("\t Please choose from the menu")
        if user_number_input == 1:
            marketing_firm.view_sweepstakes()
            self.run_simulation()
        if user_number_input == 2:
            marketing_firm.menu()
        if user_number_input == 3:
            if marketing_firm.sweepstakes_storage:
                sweepstakes.menu(marketing_firm.sweepstakes_storage)
            else:
                User_Interface.display_sweepstakes(marketing_firm.sweepstakes_storage)
                self.run_simulation()
        if user_number_input == 4:
            User_Interface.exit_menu()

