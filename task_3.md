import random

# Create a list of fruits
fruits = ["apple", "banana", "orange", "grape", "strawberry"]

# Define a function called check_guess.
def check_guess(guess):

    # Convert the guess into lower case.
    guess = guess.lower()

    # Check if the guess is in the word.
    if guess in word:
        # The guess is in the word.
        return True
    else:
        # The guess is not in the word.
        return False

# Define a function called ask_for_input.
def ask_for_input():

    # Ask the user to guess a letter and assign this to a variable called guess.
    guess = input("Guess a letter: ")

    # Check that the guess is a single alphabetical character.
    if len(guess) == 1 and guess.isalpha():
        # The guess is valid.

        # Check if the guess is in the word using the check_guess function.
        if check_guess(guess):
            print("Good guess! {} is in the word.".format(guess))
        else:
            print("Sorry, {} is not in the word. Try again.".format(guess))
    else:
        # The guess is invalid.
        print("Invalid letter. Please, enter a single alphabetical character.")

# Get the random word from the list of fruits
word = random.choice(fruits)

# Continuously ask the user for a letter until they guess the word correctly.
while not check_guess(guess):
    ask_for_input()

# When the user guesses the word correctly, print the message "Congratulations! You guessed the word correctly."
print("Congratulations! You guessed the word correctly.")