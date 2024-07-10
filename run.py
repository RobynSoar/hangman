"""
Hangman Game Script

This script allows users to play the classic Hangman game in the terminal.

Author: Robyn Soar
Date: July 2024
"""

import sys  # Imports the sys module to exit the system
# Imports the random module to allow function to return random words
import random
# Imports colorama to colour ASCII  art and reset colour
from colorama import Fore, init
import title  # Imports from title.py
from words import words  # Imports from words.py
from hangman import display_hangman  # Imports from hangman.py

# Initilizes colorama to reset colour changes
init(autoreset=True)


def print_welcome_message():
    """
    Print a welcome message to the user upon starting Hangman game terminal.
    Provides basic guideline and rules for user.
    """
    print(title.title)  # Import title from title.py with styling
    print("Welcome to Hangman!")
    print("Hangman is a game about guessing a random word one letter at a \
        time.\n")
    print("- The word is hidden at the beginning and correct guesses will \
        reveal it.")
    print("- You can guess individual letters or the whole word!")
    print("- You have 7 wrong guesses before it's Game Over.")
    print("- You can leave the game at any time by typing 'exit' into the \
        terminal at any time\n")


def play_question():
    """
    Validates if the user would like to proceed with game play.
    Checks if user input is valid.
    """
    while True:  # Loops till user agrees to play
        # .lower to allow Capitilised Y/N
        play = input("Would you like to play? (y/n):\n").lower()
        # User input validation
        if play != "y" and play != "n":
            print(Fore.RED + "Please enter either 'y' for Yes or 'n' for No")
        elif play == "n":
            print("Okay, let's play another time! Goodbye!")
            return False
        elif play == "y":
            return True


def get_player_name():
    """
    Asks the user for their name.
    Validates user's name to be more than 1 character and only alphabetical.
    """
    while True:
        username = input("Excellent! Please enter your name:\n")
        if len(username) <= 1:
            print(Fore.RED + "Please enter a name of at least two letters! \
                Try again.")
        elif not username.isalpha():
            print(Fore.RED + "Your name should contain only alphabetical \
                characters, try again.")
        else:
            print(Fore.CYAN + f"Hello, {username}! Nice to meet you, let's \
                play!\n")
            return username


def select_random_word():
    """
    Selects a word and it's corrponding hint from the words dictionary \
        within words.py.
    Returns words in uppercase and hints capitilized.
    """
    selected_word = random.choice(words)
    word = selected_word["word"]  # Chooses random word from words.py
    hint = selected_word["hint"]  # Gets the chosen word's hint from words.py
    # Returns words in uppercase and hints capitalised
    return word.upper(), hint.capitalize()


# Inspired code
def play_game(word, hint, username):
    """
    Main function to play game.
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7

    print(Fore.YELLOW + f"You've got 7 wrong guesses before the gallows are \
        full, {username}! You can do this!\n")
    print(display_hangman(tries))
    print(word_completion)
    print(f"Hint: {hint}\n")
    print(f"Guessed Letters: {guessed_letters}")
    print(f"Guessed Words: {guessed_words}\n")

    while not guessed and tries > 0:
        guess = input("Enter a letter or try for the whole word: \n")
        # If guess is a single alphabetic letter
        if len(guess) == 1 and guess.isalpha():
            print("You entered a letter")
        # If guess is the same length as chosen word and alphabetic
        elif len(guess) == len(word) and guess.isalpha():
            print("You entered a full word")
        # If input is alphabetic but more than a letter but not len of word
        elif (
            not (len(guess) == 1 or len(guess) == len(word))
            and guess.isalpha()
        ):
            print(Fore.RED + "Your guess needs to be either a single letter \
                or the same length as the whole word, please try again.")
        else:  # If input contains any numbers or special characters
            print(Fore.RED + "Please try again with no numbers or special \
                characters!")


def main():
    """
    Run all program functions
    """
    print_welcome_message()
    if play_question():
        username = get_player_name()
        word, hint = select_random_word()
        play_game(word, hint, username)


main()  # Runs main function for the game to play
