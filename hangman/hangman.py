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
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for i in range(len(alphabet)):
            if alphabet[i] in self.prior_guess:
                if alphabet[i] in self.letter_list:
                    alphabet[i] = "✓"
                else:
                    alphabet[i] = "✗"

        formatted_letters_left = "| "

        for i in range(1, 3):
            for j in range(1, 14):
                formatted_letters_left += alphabet[j + (13 * (i - 1)) - 1] + " | "
            
            if i == 1:
                formatted_letters_left += "\n| "

        return formatted_letters_left

    def init_setup(self):
        self.set_random_word()
        print(f"{self.draw_hangman()}\n\n{self.format_guess_list()}\n\nLetters left:\n{self.update_letters_left()}")
    
    def guess_letter(self, letter):
        success = self.update_guess_list(letter)
        self.update_state(success)

        print(f"{self.draw_hangman()}\n\n{self.format_guess_list()}\n\nLetters left:\n{self.update_letters_left()}")

        return self.guess_list == self.letter_list

def play_hangman():
    score = 0
    num_games = 0
    cont = True
    alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

    while cont:
        num_games += 1
        hangman = Hangman()
        hangman.init_setup()
        terminate = False

        while not terminate:
            letter = input("\nEnter guess: ").lower()

            while letter in hangman.prior_guess or letter not in alphabet:
                if letter in hangman.prior_guess:
                    letter = input(f"\nAlready guessed '{letter}' before!\nEnter new guess: ").lower()
                elif letter not in alphabet:
                    letter = input(f"\n'{letter}' is not a letter!\nEnter new guess: ").lower()

            terminate = hangman.guess_letter(letter)

            if hangman.letter_list == hangman.guess_list:
                score += 1
                print(f"\nSuccessfully guessed '{hangman.word}'!\nCurrent score = {score}/{num_games} ({round(score / num_games * 100, 2)}%)")
                break
            elif hangman.state >= 7:
                print(f"\nYou have lost. The word was '{hangman.word}'\nCurrent score = {score}/{num_games} ({round(score / num_games * 100, 2)}%)")
                break
        
        print("________________________________________")

        cont = input("\nContinue (Y/N): ").lower() == 'y'

        print("________________________________________\n")

play_hangman()