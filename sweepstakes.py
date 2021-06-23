from contestant import Contestant
from user_interface import User_Interface
from marketingfirm import MarketingFirm

class Sweepstakes:
    def __init__(self):
        self.name = ""
        self.contestants = {
        }

    def register_contestant(self, contestant):
        self.contestants[contestant.registration_number] = contestant

    def menu(self):
        marketing_firm = MarketingFirm()
        User_Interface.display_sweepstakes(marketing_firm.sweepstakes_storage)
        sweepstake_name = User_Interface.sweepstakes_selection_menu(marketing_firm.sweepstakes_storage)
        User_Interface.display_sweepstakes_menu_options(sweepstake_name)
        choose_option_sweepstake = User_Interface.get_user_input_number("Please seleect an option from the menu")
        if choose_option_sweepstake == 0:
            User_Interface.display_contestants(self.contestants)
        if choose_option_sweepstake == 1:
            contestant = Contestant.user()
            self.register_contestant(contestant)
            return new_contestant
        if choose_option_sweepstake == 2:
            pass
        if choose_option_sweepstake == 3:
            User_Interface.exit_menu()


    def view_contestants(self):
        User_Interface.display_contestants(self.contestants)

    def pick_winner(self):
        pass

