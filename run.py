import random


def welcome_message():
    """Prints a welcome message to the user."""
    print("Welcome to the Bad-Hangman game !")
    print("It is a game i'm sure a lot of you know.")
    print("It was fun to play it in the past,")
    print("at least for those of you that are my age")
    print("and still remember it :)")
    print("HINT !")
    print("The words are characters from The Witcher Universe")
    print("Try to guess letter by letter")
    print("Have fun !!!")


def choose_word():
    """Choose a random word for the user to guess."""
    witcher_characters = ["geralt",
                          "yennefer", "triss", "cirilla",
                          "dandelion", "eredin", "vesemir",
                          "lambert", "karadin", "imlerith"]
    return random.choice(witcher_characters)


def display_word(word, guessed_letters):
    """
    Display the hidden word with underscores for unknown letters.

    Args:
    word (str): The word to display.
    guessed_letters (set): A set containing the letters guessed by the user.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(display)


def draw_hangman(incorrect_guesses):
    """Draws the hangman based on the number of incorrect guesses."""
    hangman = [
        """
        +---+
        |   |
        |   O 
        |  /|\ 
        |  / \ 
        |  ___
        |  |||
      =========
        """,    


# Code idea from "https://stackoverflow.com/"
def take_guess(guessed_letters):
    """
    Prompt the user to guess a letter.

    Args:
    guessed_letters (set): A set containing the letters guessed by the user.

    Returns:
    str: The letter guessed by the user.
    """
    guess = input("Guess a letter:\n").strip().lower()
    # Validate the guess
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        return take_guess(guessed_letters)
    elif guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        return take_guess(guessed_letters)
    return guess


def play_hangman():
    """Play the Bad-Hangman game."""
    welcome_message()
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    attempts_left = 15
    max_attempts = 15

    # While loop to call functions and add guessed letters to answer
    while True:
        print("\n")
        display_word(word, guessed_letters)
        draw_hangman(incorrect_guesses)
        guess = take_guess(guessed_letters)
        guessed_letters.add(guess)
        # Counter for mistakes
        if guess not in word:
            incorrect_guesses += 1
            attempts_left -= 1
            attempts_left_str = str(attempts_left)
            print("Incorrect guess!")
            print(f"Attempts left: {attempts_left_str}")
            # End game if counter reaches 15 and print the right answer
            if incorrect_guesses >= max_attempts:
                print("Sorry, you lost. The word was:", word)
                break
        # Win message
        if all(letter in guessed_letters for letter in word):
            print("Congratulations, you won!")
            break

    # Play again or quit input
    play_again = input("Do you want to play again? (Y/N):\n").upper()
    if play_again == "Y":
        play_hangman()
    else:
        print("Thanks for playing!")


# Play the game
play_hangman()
