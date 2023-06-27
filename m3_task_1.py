import random

# Create a list of fruits
fruits = ["apple", "banana", "orange", "grape", "strawberry"]

# Create a while loop and set the condition to True.
while True:

    # Ask the user to guess a letter and assign this to a variable called guess.
    guess = input("Guess a letter: ")

    # Check that the guess is a single alphabetical character.
    if len(guess) == 1 and guess.isalpha():
        # If the guess passes the checks, break out of the loop.
        break

    # If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."
    print("Invalid letter. Please, enter a single alphabetical character.")

# Get the random word from the list of fruits
word = random.choice(fruits)

# Check if the user's guess is in the word
if guess in word:
    print("Correct! The letter {} is in the word.".format(guess))
else:
    print("Incorrect! The letter {} is not in the word.".format(guess))
