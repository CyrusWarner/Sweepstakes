from user_interface import User_Interface
from sweepstakes import Sweepstakes
from contestant import Contestant
from marketingfirm import MarketingFirm

class run_Sweepstakes:
    def __init__(self):
        pass
    
    
    def run_simulation(self):
        marketing_firm = MarketingFirm()
        sweepstakes = Sweepstakes()
        user_number_input = User_Interface.main_menu()
        running = True
        while running:
            if user_number_input == 1:
                marketing_firm.view_sweepstakes()
                self.run_simulation()
            elif user_number_input == 2:
                marketing_firm.menu()
            elif user_number_input == 3:
                sweepstakes.menu(marketing_firm.sweepstakes_storage)
            else:
                running = False

