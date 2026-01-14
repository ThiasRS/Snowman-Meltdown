import random

# List of melting snowman stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_states(mistakes, secret_word, guessed_letter):
    """Displays the game states."""
    print(STAGES[mistakes])
    print("Word:", end=" ")
    for letter in secret_word:
        if guessed_letter.lower() == letter:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    guess = "x"
    mistakes = 0
    while True:
        display_game_states(mistakes, secret_word, guess)
        guess = input("Guess a letter: ").lower()
        if guess.lower() not in secret_word:
            mistakes += 1
        if mistakes == 3:
            print("Game Over! The word was: " + secret_word)
            print(STAGES[mistakes])
            break


if __name__ == "__main__":
    play_game()