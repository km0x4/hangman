import random
fruits = ["apple", "banana", "orange", "grape", "strawberry"]
word_list = fruits
word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")

# Ask the user to enter a single letter.
guess = input("Enter a single letter: ")

# Check if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    # Print a message that says "Good guess!".
    print("Good guess!")
else:
    # Print a message that says "Oops! That is not a valid input.".
    print("Oops! That is not a valid input.")
