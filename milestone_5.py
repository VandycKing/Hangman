import random
class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []


    def check_guess(self, guess):
        obj_guess = guess.lower()
        if obj_guess in self.word:
            print(f"Good guess! \"{obj_guess}\" is in the word")

            for obj_char in self.word:
                if obj_char == obj_guess:
                    index = self.word.index(obj_char)
                    self.word_guessed[index] = obj_char
            self.num_letters =- 1
            print(f"{self.word_guessed}")
        else:
            self.num_lives -= 1
            print(f"Sorry, \"{obj_guess}\" is not in the word")
            print(f"You have {self.num_lives} lives left")


    def ask_for_input(self):

        while True:
            guess = input("Guess a letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)   

    while True:

        if game.num_lives == 0:
            print("You lost!")

        elif game.num_letters > 0:
            game.ask_for_input()  

        elif not (game.num_lives == 0  and game.num_letters > 0):
            print("Congratulations. You won the game!")          


word_list = ["apples", "mangoes", "oranges", "grapes", "Guavas"]
obj_hangman = Hangman(word_list)
obj_hangman.check_guess("a")