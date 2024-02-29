import random

# A function that prints a welcome message to the user
def welcome_message():
    print("Welcome to the Bad-Hangman game !")
    print("It is a game i'm sure a lot of you know.")
    print("It was fun to play it in the past")
    print("at least for those of you that are my age")
    print("and still remember it :)")
    print("HINT !")
    print("The words are characters from The Witcher Universe")
    print("Try to quess letter by letter")
    print("Have fun !!!")


# Function to play the game calling all other functions
def play_hangman():
    welcome_message()


# Play the game
play_hangman()   