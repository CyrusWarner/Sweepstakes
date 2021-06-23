import random
import contestant
from user_interface import User_Interface
class Sweepstakes:
    def __init__(self):
        self.name = ""
        self.contestants = {
        }

    def register_contestant(self, contestant):
        self.contestants[contestant.registration_number] = contestant

    def menu(self):
        pass

    def view_contestants(self):
        user_interface.display_contestants(self.contestants)

    def pick_winner(self):
        pass

