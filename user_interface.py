
class User_Interface:

    @staticmethod
    def main_menu():
        print(f"0) \t Would you like to see all sweepstakes.")
        print(f"1) \t Would you like to access marketing firm menu? Requires password.")
        print(f"2) \t Would you like to access the sweepstakes menu?")
        print(f"3) \t Would you like to exit the menu.")

        
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
        for key, value in contestant.items():
            print(key, value)

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
            
            
    @staticmethod       
    def display_sweepstakes_info(sweepstakes_name):
        if sweepstakes_name == "Unity Scholarship":
            print("College scholarship worth $10,000")
        if sweepstakes_name == "Lottery":
            print("Randomly drawn registration number if you win you win 500 million dollars!")
        if sweepstakes_name == "Weekly Sweepstake":
            print("Weekly sweepstake which randomly draws a registration number, winner wins 1000 dollars!")
        if sweepstakes_name == "Yearly Sweepstake":
            print("Yearly sweepstake which randomly draws a registration number, winner wins 100000 dollars!")

    @staticmethod #Come back to and make work with integers and not strings
    def sweepstakes_selection_menu(all_sweepstakes):
        user_choose_sweepstake = User_Interface.get_user_input_number("\nPlease Select a sweepstake.\n")
        index = -1
        for each in all_sweepstakes:
            index += 1
            if user_choose_sweepstake == index:
                return each


    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print("\nYou are now accessing the Marketing firm menu.\n")
        print(f"0) \t Would you like to access the sweepstake selection menu?")
        print(f"1) \t Would you like to create a new sweepstakes?")
        print(f"2) \t Would you like to change the marketing firm name from {marketing_firm_name}?")
        print(f"3) \t Would you like to exit the marketing firm menu?")

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        print(f"0) \t Would you like to view all contestants?")
        print(f"1) \t Would you like to register a new contestant?")
        print(f"2) \t Winner of {sweepstakes_name}!")
        print(f"3) \t Would you like to exit the sweepstakes menu?")
        
    @staticmethod
    def exit_menu():
        print("Exiting menu.")