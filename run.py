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
    print("Try to guess letter by letter")
    print("Have fun !!!")


# A function to choose a random word for the user to guess
def choose_word():
    # List of Witcher character names
    witcher_characters = ["geralt", "yennefer", "triss", "cirilla", "dandelion", "eredin", "vesemir", "lambert", "karadin", "imlerith"]
    # Choose a random word from the list
    return random.choice(witcher_characters)


# A function to display the hidden word with underscores for unknown letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(display)


# A function to play the game calling all other functions
def play_hangman():
    welcome_message()
    word = choose_word()
    guessed_letters = set()


# Play the game
play_hangman()   