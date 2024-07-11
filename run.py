"""
Hangman Game Script

This script allows users to play the classic Hangman game in the terminal.

Author: Robyn Soar
Date: July 2024
"""

import sys  # Imports the sys module to exit the system
# Imports the random module to allow function to return random words
import random
# Imports colorama to colour ASCII art and reset colour
from colorama import Fore, init
import title  # Imports from title.py
from words import words  # Imports from words.py
from hangman import display_hangman  # Imports from hangman.py

# Initializes colorama to reset colour changes
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
terminal\n")


def play_question():
    """
    Validates if the user would like to proceed with game play.
    Checks if user input is valid.
    """
    while True:  # Loops till user agrees to play
        # .lower to allow capitalised Y/N
        play = input("Would you like to play? (y/n):\n").lower()
        # User input validation
        if play != "y" and play != "n":
            print(Fore.RED + "Please enter either 'y' for Yes or 'n' for No")
        elif play == "n":
            print("Okay, let's play another time! Goodbye!")
            return False  # Exits game play
        elif play == "y":
            return True  # Continues game play


def get_player_name():
    """
    Asks the user for their name.
    Validates user's name to be more than 1 character and only alphabetical.
    """
    while True:
        username = input("Excellent! Please enter your name:\n").capitalize()
        if len(username) <= 1:  # If input is less than 1 character
            print(Fore.RED + "Please enter a name of at least two letters! \
Try again.")
        elif not username.isalpha():  # If input is not alphabetic
            print(Fore.RED + "Your name should contain only alphabetical \
characters, try again.")
        else:  # Greets user with the username entered
            print(Fore.CYAN + f"Hello, {username}! Nice to meet you, let's \
play!\n")
            return username


def select_random_word():
    """
    Selects a word and its corresponding hint from the words dictionary \
within words.py.
    Returns words in uppercase and hints capitalised.
    """
    selected_word = random.choice(words)
    word = selected_word["word"]  # Chooses random word from words.py
    hint = selected_word["hint"]  # Gets the chosen word's hint from words.py
    # Returns words in uppercase and hints capitalized
    return word.upper(), hint.capitalize()


# Inspired code
def play_game(word, hint, username):
    """
    Main function to play game.
    """
    word_completion = "_" * len(word)  # Displays "_" as chosen word length
    guessed = False  # Displays the word as "_" until guessed
    guessed_letters = []  # Empty list for guessed letters
    guessed_words = []  # Empty list for guessed words
    tries = 7  # How many tries till game end for user

    print(Fore.YELLOW + f"You've got 7 wrong guesses before the gallows are \
full, {username}! You can do this!\n")
    print(display_hangman(tries))
    print(word_completion)  # Displays word to user
    print(f"Hint: {hint}\n")  # Displays hint associated with word to user
    print(f"Guessed Letters: {guessed_letters}")  # Letters user has guessed
    print(f"Guessed Words: {guessed_words}")  # Words user has guessed
    # Written number of tries left to be clearer to the user
    print(f"Incorrect guesses left: {tries}\n")

    while not guessed and tries > 0:
        guess = input("Enter a letter or try for the whole word: \n").upper()
        if guess.lower() == "exit":  # If input is 'exit', confirm game exit
            exit_confirmed = confirm_exit()
            if exit_confirmed:
                sys.exit()  # Exit the game if user confirms
            else:
                continue  # Continue the game if user decides not to exit
        # If guess is a single alphabetic letter
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(Fore.RED + "You already guessed that letter")
            elif guess not in word:
                print(Fore.RED + f"The letter {guess} isn't in the word")
                tries -= 1  # Lessens the wrong guessed available to user
                guessed_letters.append(guess)  # Appends guessed_letters list
            else:
                print(Fore.GREEN + f"Yes! {guess} is in the word")
                guessed_letters.append(guess)  # Appends guessed_letters list
                # Iterates through as tuples and converts back into string
                word_completion = "".join(
                    [guess if letter == guess else wc_letter
                     for letter, wc_letter in zip(word, word_completion)]
                )
                if "_" not in word_completion:
                    guessed = True
        # If guess is the same length as chosen word and alphabetic
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(Fore.RED + f"You already guessed that word, it's not \
{guess}.")  # If user has guessed that word before
            elif guess != word:
                # If user guess is not the hidden word
                print(Fore.RED + f"{guess} is not the word.")
                tries -= 1  # Removes 1 try for the user to guess incorrectly
                guessed_words.append(guess)  # Adds guessed word to list
            else:
                print(Fore.GREEN + f"YOU GOT IT! The word was {guess}!")
                guessed = True  # If above passes, guess = hidden word
                word_completion = word  # Hidden word is revealed
        # If input is alphabetic but more than a letter but not len of word
        elif (
            not (len(guess) == 1 or len(guess) == len(word))
            and guess.isalpha()
        ):
            print(Fore.RED + "Your guess has to be either a single letter \
or the same length as the whole word")
        else:  # If input contains any numbers or special characters
            print(Fore.RED + "Please try again with no numbers or special \
characters!")

        print(display_hangman(tries))
        print(word_completion)
        print(f"Hint: {hint}\n")
        # Letters user has guessed
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        # Words user has guessed
        print(f"Guessed Words: {', '.join(guessed_words)}")
        # Written number of tries left to be clearer to the user
        print(f"Incorrect guesses left: {tries}\n")

        #
    if guessed:
        print(Fore.GREEN + f"Congraulations {username}! You got it, the \
word was {word}!\n")
    else:
        print(Fore.RED + f"Sorry {username}, you've run out of guesses \
and it's Game Over!")
        print(Fore.YELLOW + f"The word was {word}")
            

def confirm_exit():
    """
    Prompts the user to confirm if they would like to exit the game with \
"y" or "n"
    Returns True if the user confirms ("y"), False if the user denies ("n")
    """
    while True:
        # Input validation for user upon 'exit' input
        play = input(
            Fore.YELLOW + "Are you sure you'd like to exit the game?\n"
        ).lower()
        if play == "n":
            print(Fore.GREEN + "That's the spirit, you've got this!")
            return False  # Returns to game play
        elif play == "y":
            print(Fore.BLUE + "Exiting the game. Goodbye till next time!")
            return True  # Exits the game via sys.exit() in play_game
        else:
            print(Fore.RED + "Please enter either 'y' for Yes or 'n' for No")


def main():
    """
    Run all program functions
    """
    print_welcome_message()
    while True:
        if play_question():
            username = get_player_name()
            word, hint = select_random_word()
            play_game(word, hint, username)
        else:
            break

        print(Fore.GREEN + F"Thanks for playing Hangman {username}, another \
game maybe?\n")


main()  # Runs main function for the game to play
