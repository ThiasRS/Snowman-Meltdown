import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_states(mistakes, secret_word, guessed_letters):
    """Displays the game states."""
    print(STAGES[mistakes])
    print("Word:", end=" ")
    for letter in secret_word:
        if letter.lower() in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


def check_win(secret_word, guessed_letters):
    """checks if all letters are guessed correctly."""
    for letter in secret_word:
        # Even if one letter of the word is not
        # in our list, we have not won yet.
        if letter not in guessed_letters:
            return False

    # When our loop without a 'return False' runs,
    # all letters are correctly -> win!
    return True


def replay():
    """Replays the game if user wants to play again."""
    while True:
        user_input = input("Do you want to play again? (y/n): ")
        if len(user_input) == 1 and user_input.isalpha():
            if user_input == "y":
                play_game()
                break
            if user_input == "n":
                print("Thank you for playing.")
                break
        else:
            print("Please enter either 'y' or 'n'.")



def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistakes = 0
    while True:
        display_game_states(mistakes, secret_word, guessed_letters)
        if check_win(secret_word, guessed_letters):
            print("Congratulations, you won!")
            break

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("Please enter just one letter.")

        if guess not in guessed_letters:
            guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1

        if mistakes == 7:
            print("Game Over! The word was: " + secret_word)
            print(STAGES[mistakes])
            break



if __name__ == "__main__":
    play_game()
    replay()