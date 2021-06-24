
class Contestant:
    def __init__(self, first_name, last_name, email, contestant_dictionary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.won_sweepstake = False
        self.display_text_if_won_or_lost = ""
        self.registration_number = 1 + len(contestant_dictionary)
