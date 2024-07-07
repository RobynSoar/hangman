# Imports
from pyfiglet import figlet_format # Imports pyfiglet to create ASCII art
from colorama import Fore, Style, init # Imports colorama to colour ASCII  art and reset colour
import sys # Imports the sys module to exit the system
import random # Imports the random module to allow function to return random words
import title # Imports from title.py
from words import words # Imports from words.py
from hangman import display_hangman # Imports from hangman.py

# Initilizes colorama to reset colour changes
init(autoreset=True)

def print_welcome_message():
    """
    Print a welcome message to the user upon starting Hangman game terminal.
    Provides basic guideline and rules for user.
    """
    print(title.title) # Import title from title.py with styling
    print("Welcome to Hangman!")
    print("Hangman is a game about guessing a random word one letter at a time.\n")
    print("- The word is hidden at the beginning and correct guesses will reveal it.")
    print("- You can guess individual letters or the whole word!")
    print("- You have 7 wrong guesses before it's Game Over.")
    print("- You can leave the game at any time by typing 'exit' into the terminal at any time\n")


def play_question():
    """
    Validates if the user would like to proceed with game play.
    Checks if user input is valid.
    """
    while True: # Loops till user agrees to play
        play = input("Would you like to play? (y/n):\n").lower() # .lower to allow Capitilised Y/N
        # User input validation
        if play != "y" and play != "n":
            print("Please enter either 'y' for Yes or 'n' for No")
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
            print("Please enter a name of at least two letters! Try again.")
        elif not username.isalpha():
            print("Your name should contain only alphabetical characters, try again.")
        else:
            print(f"Hello, {username}! Nice to meet you, let's play!")
            return username


def select_random_word():
    """
    Selects a word and it's corrponding hint from the words dictionary within words.py.
    Returns words in uppercase and hints capitilized.
    """
    selected_word = random.choice(words)
    word = selected_word["word"] # Chooses random word from words.py
    hint = selected_word["hint"] # Gets the chosen word's hint from words.py
    return word.upper(), hint.capitalize() # Returns words in uppercase and hints capitalised


def play_game(word, hint, username):
    """
    Main function to play game.
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7

    print(f"You've got 7 wrong guesses before the gallows are full, {username}! Let's play!")
    print(display_hangman(tries))
    print(word_completion)
    print(f"Hint: {hint}")


def main():
    """
    Run all program functions
    """
    print_welcome_message()
    play_question()
    username = get_player_name()
    word, hint = select_random_word()
    select_random_word()
    play_game(word, hint, username)

main() # Runs main function for the game to play