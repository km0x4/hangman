import random

class Hangman:

    def __init__(self, word_list, num_lives=5):

        # Import the random module.
        import random

        # Set the number of lives.
        self.num_lives = num_lives

        # Get a random word from the list.
        self.word = random.choice(word_list)

        # Initialize the word_guessed list.
        self.word_guessed = ['' for _ in range(len(self.word))]

        # Initialize the num_letters variable.
        self.num_letters = len(self.word)

        # Initialize the list_of_guesses list.
        self.list_of_guesses = []

    def check_guess(self, guess):

        # Convert the guessed letter to lower case.
        guess = guess.lower()

        # Check if the guess is in the word.
        if guess in self.word:
            # The guess is in the word.
            print("Good guess! {} is in the word.".format(guess))

            # Update the word_guessed list to show that the letter has been guessed.
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess

        else:
            # The guess is not in the word.
            print("Sorry, {} is not in the word.".format(guess))

            # Decrement the number of lives.
            self.num_lives -= 1

    def ask_for_input(self):

        # Create a while loop and set the condition to True.
        while True:

            # Ask the user to guess a letter and assign this to a variable called guess.
            guess = input("Guess a letter: ")

            # Check that the guess is a single alphabetical character.
            if len(guess) == 1 and guess.isalpha():
                # The guess is valid.

                # Check if the guess is already in the list_of_guesses.
                if guess in self.list_of_guesses:
                    print("You already tried that letter!")
                    continue

                # Call the check_guess method.
                self.check_guess(guess)

                # Append the guess to the list_of_guesses.
                self.list_of_guesses.append(guess)

                # Break out of the loop.
                break

            else:
                # The guess is invalid.
                print("Invalid letter. Please, enter a single alphabetical character.")


