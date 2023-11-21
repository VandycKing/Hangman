import random

# Creates a word list
word_list = ["apple", "mango", "orange", "banana", "grape"]

for word in word_list:
    print(f"{word}: {len(word)} letters")

word = random.choice(word_list)
print(word)

guess = input("Enter a letter of your choice: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess")

else:
    print("Oops! that is not a valid input")