from contestant import Contestant
from sweepstakes import Sweepstakes



# Contestants participating in sweepstakes


contestant_one = Contestant("David", "Science", "DavidScience2002@yahoo.com", 1)
contestant_two = Contestant("Mike", "Car", "MikeCar2090@gmail.com", 2)
contestant_three = Contestant("Tyrone", "Shook", "TyroneShool2100@gmail.com", 3)
contestant_four = Contestant("Bill", "Nye", "BillNye1579@yahoo.com", 4)
contestant_five = Contestant("Riana", "Bratton", "RianaBratton2001@gmail.com", 5)
contestant_six = Contestant("Illia", "Carter", "IlliaCarter1101@yahoo.com", 6)

# Contestants receiving a registration number

sweepstakes = Sweepstakes()


sweepstakes.register_contestant(contestant_one)
sweepstakes.register_contestant(contestant_two)
sweepstakes.register_contestant(contestant_three)
sweepstakes.register_contestant(contestant_four)
sweepstakes.register_contestant(contestant_five)
sweepstakes.register_contestant(contestant_six)








