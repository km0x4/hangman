import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # defining the method 
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

        # Randomly choose a word from the word_list
        self.word = random.choice(word_list)
        
        # Create a list of the letters of the word, with each letter not yet guessed
        self.word_guessed = [''] * len(self.word)
        
        # Determine the number of unique letters in the word that have not been guessed yet
        self.num_letters = len(set(self.word))
