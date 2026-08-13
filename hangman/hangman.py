import random

# Word bank
WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "algorithm",
    "database",
    "keyboard",
    "internet",
    "software",
    "variable",
    "function",
    "github",
    "terminal",
    "science",
    "technology"
]

# Hangman stages
HANGMAN = [" |||||| ", "|||||", "||||", "|||", "||","|",  "No Chances Left!"]


def choose_word():
    """Select a random word from the word bank."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Display guessed letters and hide the remaining letters."""
    displayed = ""

    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "

    return displayed


def play_game():
    """Run one complete game of Hangman."""

    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = len(HANGMAN) - 1

    print("\n  Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {max_wrong_guesses} incorrect guesses available.\n")

    while wrong_guesses < max_wrong_guesses:

        # Display hangman
        print(HANGMAN[wrong_guesses])

        # Display current word
        print("Word:", display_word(word, guessed_letters))

        # Display guessed letters
        if guessed_letters:
            print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Get user input
        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1:
            print("Please enter exactly ONE letter.")
            continue

        if not guess.isalpha():
            print("Please enter a letter, not a number or symbol.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add guess to guessed letters
        guessed_letters.add(guess)

        # Check guess
        if guess in word:
            print("Nice! That letter is in the word!")

            # Check if the entire word has been guessed
            if all(letter in guessed_letters for letter in word):
                print("\n" + "=" * 40)
                print("YOU WON!")
                print(f"The word was: {word}")
                print("=" * 40)
                return

        else:
            wrong_guesses += 1
            remaining = max_wrong_guesses - wrong_guesses

            print("Nope! That letter isn't in the word.")
            print(f"Incorrect guesses remaining: {remaining}")

    # Game over
    print(HANGMAN[wrong_guesses])
    print("\n  GAME OVER!")
    print(f"The word was: {word}")


def main():
    """Main program loop."""

    while True:
        play_game()

        print("\nWould you like to play again?")
        choice = input("Enter Y for yes or N for no: ").lower().strip()

        if choice == "n":
            print("\nThanks for playing! ")
            break

        elif choice != "y":
            print("Invalid choice. Exiting game.")
            break


# Start the game
if __name__ == "__main__":
    main()
