"""
import random

# List of words to guess
words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for letter_ in chosen_word]  # Create a list of underscores
attempts = 8  #Number of allowed attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" +" ".join(word_display))
    guess=input("choose the letter")
    if guess in chosen_word:
        for index,letter in enumerate(chosen_word):
            if guess==letter:
                word_display[index]=guess
    else:
        print("broo Wrong answer")
        attempts-=1
    # Check for repeated guesses or invalid input
    # Note: This simple version does not handle repeated guesses or validate input.
    # Consider adding these features for a more complete game experience.

# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")
"""
