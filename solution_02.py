from enum import Enum

from utils import read_file


class Throw(Enum):
    A = 1  # Rock
    B = 2  # Paper
    C = 3  # Scissors
    
    X = 1  # Rock
    Y = 2  # Paper
    Z = 3  # Scissors


class Outcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    # Constants for outcome -> throw conversion
    X = 2  # Loss
    Y = 0  # Draw
    Z = 1  # Win


# Honestly not even sure if this solution is better than the one with 9 branches
# for each round possibility. This code is maybe more modular, but it's definitely
# more complicated. The other one is very readable, although duplicated as well.
class Round():
    def __init__(self, opp_throw, my_throw=None, outcome=None):
        self.opp_throw = opp_throw
        self.my_throw = my_throw
        self.outcome = outcome

    def get_outcome(self):
        diff = (Throw[self.my_throw].value - Throw[self.opp_throw].value) % 3
        if diff == 0:
            return Outcome.DRAW.name
        if diff == 1:
            return Outcome.WIN.name
        return Outcome.LOSS.name

    def set_outcome(self, outcome):
        self.outcome = outcome

    def get_my_throw(self):
        my_throw_value = (Throw[self.opp_throw].value + Outcome[self.outcome].value) % 3
        if my_throw_value == 0:
            my_throw_value = 3
        return Throw(my_throw_value).name

    def set_my_throw(self, my_throw):
        self.my_throw = my_throw

    def get_score(self):
        outcome_as_score = self.outcome
        outcome_mapping = {
            "X": Outcome.LOSS.name,
            "Y": Outcome.DRAW.name,
            "Z": Outcome.WIN.name,
        }
        if outcome_as_score in outcome_mapping:
            outcome_as_score = outcome_mapping[self.outcome]
            
        return Throw[self.my_throw].value + Outcome[outcome_as_score].value


def get_round_score(opp_throw, my_throw):
    round = Round(opp_throw, my_throw=my_throw)
    round.set_outcome(round.get_outcome())
    return round.get_score()

    # Original solution
    # score = Throw[my_throw].value
    
    # if opp_throw == "A":
    #     if my_throw == "X":
    #         return score + Outcome.DRAW.value
    #     if my_throw == "Y":
    #         return score + Outcome.WIN.value
    #     if my_throw == "Z":
    #         return score + Outcome.LOSS.value
            
    # if opp_throw == "B":
    #     if my_throw == "X":
    #         return score + Outcome.LOSS.value
    #     if my_throw == "Y":
    #         return score + Outcome.DRAW.value
    #     if my_throw == "Z":
    #         return score + Outcome.WIN.value

    # if opp_throw == "C":
    #     if my_throw == "X":
    #         return score + Outcome.WIN.value
    #     if my_throw == "Y":
    #         return score + Outcome.LOSS.value
    #     if my_throw == "Z":
    #         return score + Outcome.DRAW.value


def get_round_score_reversed(opp_throw, outcome):
    round = Round(opp_throw, outcome=outcome)
    round.set_my_throw(round.get_my_throw())
    return round.get_score()
    
    # Original solution
    # if opp_throw == "A":
    #     if outcome == "X":
    #         return Throw["Z"].value + Outcome["X"].value
    #     if outcome == "Y":
    #         return Throw["X"].value + Outcome["Y"].value
    #     if outcome == "Z":
    #         return Throw["Y"].value + Outcome["Z"].value

    # if opp_throw == "B":
    #     if outcome == "X":
    #         return Throw["X"].value + Outcome["X"].value
    #     if outcome == "Y":
    #         return Throw["Y"].value + Outcome["Y"].value
    #     if outcome == "Z":
    #         return Throw["Z"].value + Outcome["Z"].value

    # if opp_throw == "C":
    #     if outcome == "X":
    #         return Throw["Y"].value + Outcome["X"].value
    #     if outcome == "Y":
    #         return Throw["Z"].value + Outcome["Y"].value
    #     if outcome == "Z":
    #         return Throw["X"].value + Outcome["Z"].value

    
def problem_02_1():
    return sum(
        get_round_score(*round.split())
        for round in read_file("inputs/02_1.txt")
    )


def problem_02_2():
    return sum(
        get_round_score_reversed(*round.split())
        for round in read_file("inputs/02_1.txt")
    )


print(f"Problem 02 - 1: {problem_02_1()}")
print(f"Problem 02 - 2: {problem_02_2()}")