import random

class RockPaperScissors:

    def __init__(self, user_choice):
        self.choice = random.choice(["rock", "paper", "scissor"])
        self.user_choice = user_choice.lower()
        self.winner = ""


    def play(self):
        if self.user_choice.lower() == self.choice:
            print(f"You both had {self.choice}, no winner or loser")
            self.winner = "not decided"
            return 0

        case_1 = ["rock", "paper"]
        case_2 = ["paper", "scissor"]
        case_3 = ["scissor", "rock"]

        case_1.sort()
        case_2.sort()
        case_3.sort()

        self.input = {self.choice: "Computer", self.user_choice:"User"}

        self.input_check = [i.lower() for i in list((self.input.keys()))]
        self.input_check.sort()
        
        print(self.input_check)

        if self.input_check == case_1:
            self.winner = self.input["paper"]
        elif self.input_check == case_2:
            self.winner = self.input["scissor"]
        elif self.input_check == case_3:
            self.winner = self.input["rock"]
        else: 
            print("Wrong")


        return self.winner
