class User_Interface:


    @staticmethod
    def display_welcome():
        print("Welcome to sweepstakes!")
        
    @staticmethod
    def main_menu():
        print(f"0) Would you like to register to enter all sweepstakes?")
        print(f"1) Would you like to see all sweepstakes.")
        print(f"2) Would you like to access marketing firm menu? Requires password.")
        print(f"3) Would you like to see all contestants participating in sweepstakes.")
        print(f"4) Would you like to exit the menu.")

        
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
        for each in sweepstakes:
            print(each)

    @staticmethod
    def sweepstakes_selection_menu(all_sweepstakes):
        user_choose_sweepstake = get_user_input_number("Please Select a sweepstake.")
        index = 0
        for each in all_sweepstakes:
            print(f"{index} {each}")
            if user_choose_sweepstake == index:
                display_sweepstakes_menu_options(each)
        index += 1

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print(f"0) \t Would you like to access the sweepstake selection menu?")
        print(f"1) \t Would you like to create a new sweepstakes?")
        print(f"2) \t Would you like to change the marketing firm name from {marketing_firm_name}?")
        print(f"3) \t Would you like to exit the marketing firm menu?")

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        pass
    @staticmethod
    def exit_sweepstakes():
        print("Exiting menu.")