"""
This module contains a Scrabble game implementation.
The game computes the Scrabble score for words entered by the user.
"""

import time
import random

# Define letter values
LETTER_VALUES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
    'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

# Basic dictionary of words
WORD_DICTIONARY = {
    "apple", "banana", "cabbage", "dog", "hello", "world",
    "brown", "jumps", "lazy", "elephant", "umbrella", "Hussein"
    "computer", "scrabble", "puzzles", "mystical", "alphabet"
}


def compute_score(word):
    """Compute the Scrabble score for a given word."""
    score = 0
    for letter in word.upper():
        if letter in LETTER_VALUES:
            score += LETTER_VALUES[letter]
    return score


def is_valid_word(word, word_dictionary):
    """Check if the word is in the given dictionary."""
    return word.lower() in word_dictionary


def play_round():
    """Play a round of the Scrabble game."""
    word_length = random.randint(3, 8)
    start_time = time.time()

    print(f"Please enter a word with exactly {word_length} letters:")

    while True:
        user_word = input("Your word: ").strip()
        elapsed_time = time.time() - start_time

        if not user_word.isalpha():
            print("Please enter a valid word containing only letters.")
            continue

        if len(user_word) != word_length:
            print(f"The word must be exactly {word_length} letters long.")
            continue

        if not is_valid_word(user_word, WORD_DICTIONARY):
            print("This is not a valid word. Please enter a valid word.")
            continue

        score = compute_score(user_word)

        # Score adjustment based on time taken to enter the word
        if elapsed_time < 15:
            score += max(0, 15 - int(elapsed_time))

        print(f"Your score for '{user_word}' is: {score}")
        return score


def scrabble_game():
    """Run the Scrabble game."""
    total_score = 0
    round_count = 0

    while True:
        round_count += 1
        round_score = play_round()
        total_score += round_score

        print(f"Total Score: {total_score}")

        if round_count >= 10:
            break

        play_again = input(
            "Do you want to play another round? (yes/no): "
        ).lower()
        if play_again != 'yes':
            break

    print(f"Game Over! Your final score is: {total_score}")


if __name__ == "__main__":
    scrabble_game()
