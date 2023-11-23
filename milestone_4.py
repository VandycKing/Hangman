import random
class Hangman:

    def __init__(self, word_list = None, num_lives = 5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        obj_guess = guess.lower()
        if obj_guess in self.word:
            print("Good guess! \"{obj_guess}\" is in the word")

            for obj_char in self.word:
                if obj_char == obj_guess:
                    index = self.word.index(obj_char)
                    self.word_guessed[index] = obj_char
            self.num_letters - 1
        else:
            self.num_lives - 1
            print("Sorry, \"{obj_guess}\" is not in the word")
            print("You have {num_lives} lives left")
            


    def ask_for_input(self):
        condition = True
        while condition:
            guess = input("Guess a letter: ")
            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                

            
            




obj_hangman = Hangman(["apples", "mangoes"])
obj_hangman.ask_for_input()