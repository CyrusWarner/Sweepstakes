import random

class Sweepstakes:
    def __init__(self):
        self.name = ""
        self.contestants = {
        }

    def register_contestant(self, contestant):
        contestant.registration_number = random.randint(1, 10)

    def menu(self):
        pass

    def view_contestants(self):
        pass

    def pick_winner(self):
        pass
