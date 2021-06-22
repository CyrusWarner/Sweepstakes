from sweepstakes import Sweepstakes


class MarketingFirm:
    def __init__(self):
        self.name = "Dynamic"
        self.sweepstakes_storage = ("Scholarship", "Lottery", "Weekly Sweepstake", "Yearly sweepstake")

    def create_sweepstakes(self):
        pass

    def change_marketing_firm_name(self):
        pass

    def select_sweepstakes(self):
        pass
    def menu(self):
        index = 0
        for each in self.sweepstakes_storage:
            print(f"{index}\t{each}")
            index += 1