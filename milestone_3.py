import random

# Create a word list
word_list = ["apple", "mango", "orange", "banana", "grape"]

# Chooses a random word
word = random.choice(word_list)


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess \"{guess}\" is in the word")
    else:
        print(f"Sorry \"{guess}\" is not in the word")


def ask_for_input():
    guess = input("Enter a letter: ").lower()
    while len(guess) == 1 and not guess.isalpha():
        print("Invalid entry, please enter a single alphabetical character.")
        guess = input("Enter a letter: ")
    check_guess(guess)
    
ask_for_input()






