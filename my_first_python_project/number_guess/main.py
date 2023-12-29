import random

# generate a random number
number_range = range(0, 101)
target_number = random.randint(1, 100)
score = 20;

def get_number():
    # Getting the number
    guess = int(input("Please guess a number between 1 and 100\n"))
    # validating the number
    while guess not in number_range:
        guess = int(input("Try again, Please guess a number between 1 and 100 , if you want to quit press 0 \n"))
    return(guess)


# Checking the number
def check_number(guessed_number, target_number, score):
    if guessed_number == target_number:
        print(f"Great! You found it! your score is {score}")
        return 1
    elif guessed_number == 0:
        print(f"The random number was {target_number}. We stop the game, Bye!")
        return 1
    elif guessed_number < target_number and guessed_number > 0 :
        print("give it another try, Guess a bigger number")
        return 0
    elif guessed_number > target_number and guessed_number > 0:
        print("give it another try, Guess a smaller number")
        return 0


if name == main:
    guess = get_number()

while not check_number(guess, target, score):
   score = score - 1
   print(f"your score is {score}")
   guess = get_number()
