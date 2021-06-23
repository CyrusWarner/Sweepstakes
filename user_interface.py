
class User_Interface:

    @staticmethod
    def main_menu():
        print(f"\n\n0) Would you like to register to enter all sweepstakes?")
        print(f"1) Would you like to see all sweepstakes.")
        print(f"2) Would you like to access marketing firm menu? Requires password.")
        print(f"3) Would you like to access the sweepstakes menu?")
        print(f"4) Would you like to see all contestants participating in sweepstakes.")
        print(f"5) Would you like to exit the menu.")

        
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
        pass

    @staticmethod
    def display_contestant_info(contestant):
        print(contestant)

    @staticmethod
    def display_sweepstakes(sweepstakes):
        print("Displaying all sweepstakes.\n")
        index = 0
        for each in sweepstakes:
            print(f"{index}) {each}")
            index += 1

    @staticmethod #Come back to and make work with integers and not strings
    def sweepstakes_selection_menu(all_sweepstakes):
        user_choose_sweepstake = User_Interface.get_user_input_string("\nPlease Select a sweepstake.")
        index = 0
        for each in all_sweepstakes:
            if user_choose_sweepstake == index:
                print(each)
        index += 1

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print("\nYou are now accessing the Marketing firm menu.\n")
        print(f"0) \t Would you like to access the sweepstake selection menu?")
        print(f"1) \t Would you like to create a new sweepstakes?")
        print(f"2) \t Would you like to change the marketing firm name from {marketing_firm_name}?")
        print(f"3) \t Would you like to exit the marketing firm menu?")

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        print("\nWould you like to view all contestants?\n")
        print(f"0) \t Would you like to register a new contestant?")
        print(f"1) \t Winner of {sweepstakes_name}!")
        print(f"2) \t Would you like to exit the sweepstakes menu?")
        
    @staticmethod
    def exit_sweepstakes():
        print("Exiting menu.")