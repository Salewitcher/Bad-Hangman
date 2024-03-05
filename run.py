import random


# A function that prints a welcome message to the user
def welcome_message():
    print("Welcome to the Bad-Hangman game !")
    print("It is a game i'm sure a lot of you know.")
    print("It was fun to play it in the past,")
    print("at least for those of you that are my age")
    print("and still remember it :)")
    print("HINT !")
    print("The words are characters from The Witcher Universe")
    print("Try to guess letter by letter")
    print("Have fun !!!")


# A function to choose a random word for the user to guess
def choose_word():
    # List of Witcher character names
    witcher_characters = ["geralt",
                          "yennefer", "triss", "cirilla",
                          "dandelion", "eredin", "vesemir",
                          "lambert", "karadin", "imlerith"]
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


# A function with an input for the user to guess a letter
def take_guess(guessed_letters):
    guess = input("Guess a letter:\n").lower()
    # Validate the guess
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        return take_guess(guessed_letters)
    elif guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        return take_guess(guessed_letters)
    return guess


# A function to play the game calling all other functions
def play_hangman():
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
        guess = take_guess(guessed_letters)
        guessed_letters.add(guess)
        # Counter for mistakes
        if guess not in word:
            incorrect_guesses += 1
            attempts_left -= 1
            attempts_left_str = str(attempts_left)
            print("Incorrect guess!")
            print(f"Attempts left: {attempts_left_str}")
            # End game if counter reaches 15 and print the right amswer
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
