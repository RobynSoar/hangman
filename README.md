# Hangman
(by Robyn Soar)

Hangman is a word game and runs in the Code Institute mock terminal on Heroku.
It's a well-known childhood word game in which traditionally is played with two or more players, with one person choosing a word and setting up the game, and the other being the one to guess the letters one by one or the whole word at a time. 

This Hangman game has been made so the user can play against a computer who decides on a random word, keeps tally of used letters and guesses left available, as well as gives hints to the user of the hidden word. 

As this terminal-based Python project is design specifically for laptop / desktop screens, it will not display correctly on a mobile.

View the live site [here](https://robyn-hangman-b1356368c517.herokuapp.com/)

## Key Project Goals

- To give a fun game experience to the user that they can keep coming back to.
- To allow users to play as a singlular person instead of needed another to set up the game.

## Target Audience

- The primary target audience for Hangman is 5+, whether as a learning platform to help the younger audience learn how to spell or to soliditfy learning, but also for all reading ages to be able to have fun with a game.

## Table of Contents

- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
- [Design](#design)
    - [Flowchart](#flowchart)
    - [Imported Libraries](#imported-libraries)
    - [Technologies Used](#technologoies-used)
- [Testing](#testing)
    - [Functional Testing](#functional-testing)
    - [Validator Testing](#validator-testing)
    - [Fixed Bugs](#fixed-bugs)
- [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Deployment to Heroku](#deployment-to-heroku)
    - [Clone the Repository Code Locally](#clone-the-repository-code-locally)
- [Credits](#credits)
    - [Inspired Code](#inspired-code)
    - [Walkthrough Code](#walkthrough-code)
    - [Acknowledgements](#acknowledgements)
- [Author](#author)

## Features

### Existing Features

### Features Left to Implement

[Return to Table of Contents](#table-of-contents)

## Design

### Flowchart

[Lucidchart](https://www.lucidchart.com/pages/) was used to create a flowchart to map out the Hangman game.

This aids the creation of the game by showing validators for user input, where functions are needed as well as game end points.

![Hangman flowchart using Lucidchart](documentation/flowchart/hangman-flowchart.png)

### Imported Libraries

__pyfiglet (PyPi)__ - Used to generate ASCII art text for the title

__colorama__ - Used to colour ASCII art and text feedback to the user

__sys__ - Used to enable the user to be able to exit the program at any time

__random__ - Used to allow the program to randomly choose a word from a dictionary within the words.py file

### Technologies Used

- GitHub
    - Source code is hosted on GitHub.

- Git
    - Used for development of the game as well as commit and pushing code throughout.

- [pyfiglet (PyPi)](https://pypi.org/project/pyfiglet/)
    - Used to generate the ASCII art for the game title.

- [colorama](https://pypi.org/project/colorama/)
    - Used to colour ASCII art and text within the game.

- [Lucidchart](https://www.lucidchart.com/pages/)
    - Used to create a flowchart to map out the functions, validators and user input within the game.

[Return to Table of Contents](#table-of-contents)

## Testing

### Functional Testing

### Validator Testing

### Fixed Bugs

__Random Module Bug__

*Bug*

Terminal posed the below message to notify of an issue.

![Random Module - Bug](documentation/testing/random-module-bug.png)

*Fix*

I noticed that the import wasn't being seen, and I needed to tweak it for the random module to see the necessary information.

![Random Module - Fix](documentation/testing/random-module-fix.png)

__Boolean Game Stop Bug__

*Bug*

Main function would still execute after the User declined ('n') to play again.

![Boolean Game Stop Bug](documentation/testing/if-no-game-stop-bug.png)

*Fix*

Added an ```if``` statement to the main function to only excute if ```play_question() = True```

__Extra Space Bug__

*Bug*

Within the code ```word_completion = "_" * len(word)```, the "_" had been changed to have a space ("_ ") with the intention to give better readability to the user when the word was hidden.

In the terminal this showed as intended, however, the hidden word took on the spaces as a hidden letter, and showed ```_ _ _ ``` instead of ```______``` for a 6 letter word.

The program was also ending after 4-5 correct guesses, even with enough 'tries' left.

*Fix*

Simply reseting "_ " back to "_" fixed the part of the bug that limited the amount of tries given with correct guesses.

Inside the words.py file dictionary, the amount of letters was also put into the hint given for each word, which accounts for the lack of visible spaces between hidden letters.

[Return to Table of Contents](#table-of-contents)

## Deployment

### Version Control

The site was created using the Git editor and pushed to GitHUb to the remote repository 'hangman'

The following git commands were used throughout development to push code to the remote repository:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are commited.

```git commit -m "commit message"``` - This command was used to commit changes to the local repository queue ready to be pushed.

```git push``` - This command was used to push all committed code to the remote repository 'woohoo-salon' on GitHub.

### Deployment to Heroku

1. Make sure that Heroku will install dependencies used by opening the "requirements.txt" file and typing "pip3 freeze > requirements.txt" and hit the "Enter" key.
2. Commit and push the changes to GitHub.
3. Go to Heroku.com and sign up for an account.
4. Click "Create new app".
5. Give the app a unique name, select region and "Create app".
6. Go to "Settings" and then to "Config Vars".
7. Create a Config Var called PORT (Key) and set it to 8000 (Value).
8. Scroll down, click "Add buildpack" and add two buildpacks within the "Settings" tab, and add them in the following order.
    * heroku/python
    * heroku/nodejs
9. Click "Deploy" in the navbar at the top of the page.
10. Select "GitHub" within the section called "Deployment method".
11. Click "Connect to GitHub".
12. Under "Connect to GitHub, search for your repository name and click "Connect".
13. Scroll down the page to Automatic deploys and click "Enable Automatic Deploys" to enable Heroku to rebuild the app when a new change is pushed to GitHub.
14. When deployment is completed and you're notified that the deployment was successful, click "View" to go to the mock terminal.

### Clone the Repository Code Locally

Navigate to the GitHub Repository you want to clone to use locally:
1. Click on the code drop down button
2. Click on HTTPS
3. Copy the repository link to the clipboard
4. Open your IDE of choice (Git must be installed for the next steps)
5. Type git close copied-git-url into the IDE terminal

The project will now of been cloned on your local machine for use.

[Return to Table of Contents](#table-of-contents)

## Credits

### Inspired Code

- [Love Sandwiches - Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/58d3e90f9a2043908c62f31e51c15deb/)
    - Used for sections of basic code.

- [How to Build HANGMAN with Python in 10 MINUTES - Kite](https://www.youtube.com/watch?v=m4nEnsavl6w)
    - Used as guidance on how to excute certain parts of code.

- [Write a long string on multiple line in Python - note.nkmk.me](https://note.nkmk.me/en/python-long-string/)
    - Used to format code to fit within 80 characters on a single line by using newline characters and parenthesis.

### Walkthrough Code

- [Coding Professor - How to create ASCII art text in Python](https://www.youtube.com/watch?v=Y0QiBbI3MWs)
    - YouTube video helped me understand how to import and style ASCII art fonts for the Hangman title.

### Acknowledgements

[Return to Table of Contents](#table-of-contents)

## Author

Robyn Soar
robyn999@hotmail.co.uk