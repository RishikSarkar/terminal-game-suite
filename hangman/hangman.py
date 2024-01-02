import random

class Hangman:
    def __init__(self):
        self.word = ""
        self.state = 0
        self.letter_set = set()
        self.letter_list = []
        self.guess_list = []
        self.prior_guess = set()
    
    def set_random_word(self):
        self.word = random.choice(open("hangman\hangman.txt").read().splitlines()).lower()
        self.letter_set = set(self.word)
        self.letter_list = list(self.word)
        self.guess_list = [None] * len(self.letter_list)
        return self.word, self.letter_set, self.letter_list, self.guess_list

    def draw_hangman(self):
        if self.state == 0:
            return "      \n|     \n|     \n|     \n|     \n|_____"
        elif self.state == 1:
            return "_____ \n|   | \n|     \n|     \n|     \n|_____"
        elif self.state == 2:
            return "_____ \n|   | \n|   O \n|     \n|     \n|_____"
        elif self.state == 3:
            return "_____ \n|   | \n|   O \n|   | \n|     \n|_____"
        elif self.state == 4:
            return "_____ \n|   | \n|   O \n|  /| \n|     \n|_____"
        elif self.state == 5:
            return "_____ \n|   | \n|   O \n|  /|\\\n|    \n|_____"
        elif self.state == 6:
            return "_____ \n|   | \n|   O \n|  /|\\\n|  / \n|_____"
        else:
            return "_____ \n|   | \n|   O \n|  /|\\\n|  / \\\n|_____"

    def update_guess_list(self, letter):
        
        if letter not in self.prior_guess:
            self.prior_guess.add(letter)

        if letter not in self.letter_set:
            return False

        self.letter_set.remove(letter)

        for i in range(len(self.letter_list)):
            if self.letter_list[i] == letter:
                self.guess_list[i] = letter
                
        return True

    def format_guess_list(self):
        blank_word = ""

        for letter in self.guess_list:
            if letter == None:
                blank_word += " _ "
            else:
                blank_word += " " + letter + " "

        return "Word:" + blank_word

    def update_state(self, success):
        if not success:
            self.state += 1

    def update_letters_left(self):
        alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

        return alphabet - self.prior_guess

    def init_setup(self):
        self.set_random_word()
        print(f"{self.draw_hangman()}\n\n{self.format_guess_list()}\n\nLetters left: {self.update_letters_left()}")
    
    def guess_letter(self, letter):
        success = self.update_guess_list(letter)
        self.update_state(success)

        print(f"{self.draw_hangman()}\n\n{self.format_guess_list()}\n\nLetters left: {self.update_letters_left()}")

        return self.guess_list == self.letter_list

def play_hangman():
    score = 0
    num_games = 0
    cont = True

    while cont:
        num_games += 1
        hangman = Hangman()
        hangman.init_setup()
        terminate = False

        while not terminate:
            print("\nEnter guess: ")
            letter = input().lower()

            while letter in hangman.prior_guess:
                print(f"\nAlready guessed '{letter}' before!\nEnter new guess: ")
                letter = input().lower()

            terminate = hangman.guess_letter(letter)

            if hangman.letter_list == hangman.guess_list:
                score += 1
                print(f"Successfully guessed '{hangman.word}'!\nCurrent score = {score}/{num_games} ({round(score / num_games * 100, 2)}%)")
                break
            elif hangman.state >= 7:
                print(f"You have lost. The word was '{hangman.word}'\nCurrent score = {score}/{num_games} ({round(score / num_games * 100, 2)}%)")
                break
        
        print("________________________________________")

        print("Continue (Y/N): ")
        cont = input().lower() == 'y'

play_hangman()