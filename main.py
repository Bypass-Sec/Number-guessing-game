import random

def welcome_message():
    print("Welcome to the Ultimate Number Guessing Game!")
    print("Get ready to guess the magic number...")

def game_intro():
    print("\nYou can choose between the following modes:")
    print("1) Classic Mode (Guess the number)")
    print("2) Lucky Mode (Get hints to guide your guesses)")
    print("3) Mystery Mode (With a secret twist!)")
    choice = input("Pick your mode (1/2/3): ")
    return choice

def classic_mode(top_of_range):
    print("\nClassic Mode: Guess the number!")
    magic_number = random.randint(1, top_of_range)
    attempts = 0
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {top_of_range}: "))
            attempts += 1
            if guess < magic_number:
                print("Too low! Try again stupid ah.")
            elif guess > magic_number:
                print("Too high! Try again stupid ah.")
            else:
                print(f"Congrats! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

def lucky_mode(top_of_range):
    print("\nLucky Mode: Get hints to guide your guesses!")
    magic_number = random.randint(1, top_of_range)
    attempts = 0
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {top_of_range}: "))
            attempts += 1
            if guess < magic_number:
                print("Too low! But worry, youre far off!")
            elif guess > magic_number:
                print("Too high! Almost there you b - word!")
            else:
                print(f"Awesome! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

def mystery_mode(top_of_range):
    print("\nMystery Mode: Guess the number, but with a surprise twist!")
    magic_number = random.randint(1, top_of_range)
    special_number = random.randint(1, top_of_range)
    attempts = 0
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {top_of_range}: "))
            attempts += 1
            if guess < magic_number:
                print("Too low!")
            elif guess > magic_number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the magic number in {attempts} attempts!")
                if attempts == special_number:
                    print("BONUS: You guessed it on the special lucky attempt!")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    welcome_message()
    
    top_of_range = input("Type the highest number you want to guess up to: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Please type a number larger than 0 next time.")
            quit()
    else:
        print("That's not a valid number!")
        quit()
    
    mode = game_intro()
    
    if mode == "1":
        classic_mode(top_of_range)
    elif mode == "2":
        lucky_mode(top_of_range)
    elif mode == "3":
        mystery_mode(top_of_range)
    else:
        print("Invalid choice, quitting the game.")
        quit()

if __name__ == "__main__":
    main()
