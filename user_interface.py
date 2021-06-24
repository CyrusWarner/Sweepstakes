
class User_Interface:

    @staticmethod
    def main_menu():
        validate_user_selection = (False, None)
        while validate_user_selection[0] is False:
            print(f"1) \t Would you like to see all sweepstakes.")
            print(f"2) \t Would you like to access marketing firm menu?")
            print(f"3) \t Would you like to access the sweepstakes menu?")
            print(f"4) \t Would you like to exit the menu.")
            user_input = User_Interface.get_user_input_number("\nPlease choose from the menu")
            validate_user_selection = User_Interface.validate_main_menu(user_input)
        return validate_user_selection[1]

    @staticmethod
    def validate_main_menu(user_input):
        switcher = {
            1: (True, 1),
            2: (True, 2),
            3: (True, 3),
            4: (True, 4),
        }
        return switcher.get(user_input, (False, None))
        
    @staticmethod
    def get_user_input_string(prompt):
        user_input = input(prompt)
        return user_input

    @staticmethod
    def get_user_input_number(prompt):
        user_input_number = int(input(prompt))
        return user_input_number

    @staticmethod
    def display_contestants(contestant):
        if contestant:
            for key, value in contestant.items():
                print(f"\t {value.first_name} {value.last_name}")
        else:
            print("No Contestants.")

    @staticmethod
    def display_contestant_info(contestant):
        print(f"{contestant.first_name} {contestant.last_name}\n")

    @staticmethod
    def display_sweepstakes(sweepstakes):
        if sweepstakes:
            print("Displaying all sweepstakes.\n")
            index = 1
            for each in sweepstakes:
                print(f"{index}) {each.name}")
                index += 1
        else:
            print("\n\tNo sweepstakes currently\n")

    @staticmethod
    def sweepstakes_selection_menu(all_sweepstakes):
        if all_sweepstakes:
            user_choose_sweepstake = User_Interface.get_user_input_number("\nPlease Select a sweepstake.\n")
            index = -1
            for each in all_sweepstakes:
                index += 1
                if user_choose_sweepstake == index:
                    return each


    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print("\nYou are now accessing the Marketing firm menu.\n")
        print(f"1) \t Would you like to access the sweepstake selection menu?")
        print(f"2) \t Would you like to create a new sweepstakes?")
        print(f"3) \t Would you like to change the marketing firm name from {marketing_firm_name}?")
        print(f"4) \t Would you like to exit the marketing firm menu?")

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        print(f"1) \t Would you like to view all contestants?")
        print(f"2) \t Would you like to register a new contestant?")
        print(f"3) \t Determine winner of {sweepstakes_name}!")
        print(f"4) \t Would you like to exit the sweepstakes menu?")

    @staticmethod
    def display_winner(contestant):
        print(f"\t {contestant.first_name} {contestant.last_name} has won the sweepstake!")
        contestant.sweepstake_info = "You have won the sweepstakes"
    @staticmethod
    def display_loser(contestants):
        for key, value in contestants.items():
            if value.won_sweepstakes is False:
                value.display_text_if_won_or_lost = "You have lost the sweepstake."
        
    @staticmethod
    def exit_menu():
        print("exiting menu")