import random

def generate_random_number():
    """
    Generates a random number between 1 and 100.
    """
    return random.randint(1, 100)

def get_user_guess():
    """
    Prompts the user to input their guess and converts it to an integer.
    """
    return int(input("Enter your guess: "))

def compare_numbers(random_number, user_guess):
    """
    Compares the random number and the user's guess, and provides feedback.
    """
    if user_guess > random_number:
        return "Too high!"
    elif user_guess < random_number:
        return "Too low!"
    else:
        return "Congratulations! You guessed the number."

def play_game():
    """
    Runs the game until the user correctly guesses the number.
    """
    random_number = generate_random_number()
    attempts = 0

    while True:
        attempts += 1
        user_guess = get_user_guess()
        result = compare_numbers(random_number, user_guess)

        if result == "Congratulations! You guessed the number.":
            print(result)
            print(f"It took you {attempts} attempts to win the game.")
            break
        else:
            print(result)

if __name__ == "__main__":
    play_game()1