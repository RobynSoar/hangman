def print_welcome_message():
    """
    Print a welcome message to the user upon starting Hangman game terminal.
    Provides basic guideline and rules for user.
    """

    print("Welcome to Hangman!")
    print("Hangman is a game about guessing a random word one letter at a time.")
    print("The word is hidden at the beginning and correct guesses will reveal")
    print(" the word. You can guess individual letters or the whole word!")
    print("You have 7 wrong guesses before it's Game Over.")
    print("You can leave the game at any time by typing 'exit' into the terminal at any time\n")


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
        else play == "y":
            get_player_name()

        