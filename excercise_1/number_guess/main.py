import random



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


if __name__ == '__main__':
    score = 100;

    # generate a random number
    target_number = random.randint(1, 100)

    guess = get_number()

    while not check_number(guess, target_number, score):
      score = score - 5
      print(f"your score is {score}")
      guess = get_number()
