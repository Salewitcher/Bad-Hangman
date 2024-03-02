# Bad-Hangman Game

Welcome to the Bad-Hangman game! This is a simple Python implementation of the classic Hangman game with a Witcher Universe twist. In this game, players must guess the hidden word character by character before running out of attempts. Let's dive into the details:

## How to Play

1. **Setup**: Ensure you have Python installed on your system.
2. **Run the Game**: Execute the provided Python script `hangman.py` by running `python hangman.py` in your terminal.
3. **Game Instructions**: Follow the on-screen instructions to play the game. You'll be prompted to guess a letter at a time.
4. **Guessing Rules**: Enter a single letter as your guess. You have a limited number of attempts to guess the word correctly.
5. **Win or Lose**: If you successfully guess the word within the allowed attempts, you win! Otherwise, you lose the game.

## Game Features

- **Random Word Selection**: A random word from the Witcher Universe is chosen for each game session.
- **Interactive Interface**: The game provides interactive prompts and messages to guide the user through the gameplay.
- **Hints**: Players are given hints that the words are characters from The Witcher Universe.
- **Play Again**: After each game session, players have the option to play again.

## Testing

1. **Setup**: Python was installed on the testing system as a prerequisite.
2. **Clone the Repository**: The repository was cloned to the local machine using Git.
3. **Navigate to the Directory**: A terminal was opened, and navigation was performed to the directory where the repository was cloned.
4. **Run the Game**: The `hangman.py` script was executed by running `python hangman.py` in the terminal.
5. **Game Instructions**: The on-screen instructions were followed to play the game. Letters were guessed one at a time.
6. **Guessing Rules**: Single letters were entered as guesses, ensuring adherence to the guessing rules. Attempts were made to guess the word correctly within the limited number of attempts.
7. **Win or Lose**: The game was tested to ensure correct outcomes when winning or losing. Winning occurred when the word was guessed within the allowed attempts, while losing occurred when the attempts were exhausted.
8. **Play Again**: After each game session, the option to play again was selected to verify that the game restarted correctly.
9. **PEP8**: Passed the code through a PEP8 linter and confirmed there are no problems.

## Bugs

- Backwards counter did not print
- - Solution: Converted "attempts_left"  num-variable into a string (attempts_left_str = str(attempts_left)).

## Remainig Bugs

- No bugs remaining.

## Dependencies

This game requires Python to be installed on the system. No external libraries or dependencies are needed.

## How to Contribute

Contributions to improve this game are welcome! Here are a few ways you can contribute:

- Add additional features or enhancements to the gameplay.
- Improve the code structure or efficiency.
- Fix any bugs or issues you encounter.

To contribute, simply fork this repository, make your changes, and submit a pull request. Your contributions will be appreciated!

[Back to Top](#bad-hangman-game)
