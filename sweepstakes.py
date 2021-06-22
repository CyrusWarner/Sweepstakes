import random
import contestant
import user_interface

class Sweepstakes:
    def __init__(self):
        self.name = ""
        self.contestants = {
        }

    def register_contestant(self, contestant):
        self.contestants[contestant.registration_number] = contestant
        # Change registration number to be based on individual index
    def menu(self):
        pass

    def view_contestants(self):
        for each in self.contestants:
            display_contestants(each)

    def pick_winner(self):
        pass
