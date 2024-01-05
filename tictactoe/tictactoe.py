import random
import time

class TicTacToe:
    def __init__(self):
        self.mode = 0
        self.grid = [" "] * 9
    
    def set_mode(self, mode):
        self.mode = mode

    def reset_grid(self):
        self.grid = [" "] * 9
    
    def user_move(self, symbol):
        print("Enter move (1 - 9):")
        move = int(input())

        if self.grid[move - 1] == " ":
            self.grid[move - 1] = symbol
            return self.check_win()
        else:
            print("Illegal move. Try again!")
            self.user_move(symbol)

    def easy_move(self, symbol):
        possible_moves = []
        for i in range(len(self.grid)):
            if self.grid[i] == " ":
                possible_moves.append(i)
        
        bot_move = random.choice(possible_moves)
        self.grid[bot_move] = symbol
        print(f"Easy Bot move: {bot_move + 1}")

        return self.check_win()

    
    def check_win(self):
        if self.grid[0] == self.grid[1] == self.grid[2] != " ":
            return True
        elif self.grid[3] == self.grid[4] == self.grid[5] != " ":
            return True
        elif self.grid[6] == self.grid[7] == self.grid[8] != " ":
            return True
        elif self.grid[0] == self.grid[3] == self.grid[6] != " ":
            return True
        elif self.grid[1] == self.grid[4] == self.grid[7] != " ":
            return True
        elif self.grid[2] == self.grid[5] == self.grid[8] != " ":
            return True
        elif self.grid[0] == self.grid[4] == self.grid[8] != " ":
            return True
        elif self.grid[2] == self.grid[4] == self.grid[6] != " ":
            return True
        
        return False
    
    def check_draw(self):
        if " " not in self.grid:
            return True
        
        return False
    
    def print_grid(self):
        grid_string = f"  {self.grid[0]}  |  {self.grid[1]}  |  {self.grid[2]}  \n-----|-----|-----\n  {self.grid[3]}  |  {self.grid[4]}  |  {self.grid[5]}  \n-----|-----|-----\n  {self.grid[6]}  |  {self.grid[7]}  |  {self.grid[8]}  "
        return grid_string
    
    def play_2p(self):
        print("Player 1 Symbol: X")
        print("Player 2 Symbol: O\n")

        win = False

        print(self.print_grid() + "\n")

        while True:
            print("Player 1")
            win = self.user_move('X')
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Player 1 wins!")
                print("\n" + self.print_grid())
                break

            draw = self.check_draw()
            if draw:
                print("Draw!")
                break

            print("Player 2")
            win = self.user_move('O')
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Player 2 wins!")
                print("\n" + self.print_grid())
                break

            draw = self.check_draw()
            if draw:
                print("Draw!")
                break
        
        return 0
    
    def play_easy(self):
        first_player = random.randint(0, 1)

        player_symbol = "X"
        bot_symbol = "O"

        if first_player == 1:
            player_symbol = "O"
            bot_symbol = "X"

        print(f"Player Symbol: {player_symbol}")
        print(f"Easy Bot Symbol: {bot_symbol}\n")

        if first_player == 0:
            print("Player goes first!\n")
        else:
            print("Easy Bot goes first!\n")

        win = False

        print(self.print_grid() + "\n")

        if first_player == 1:
            win = self.easy_move(bot_symbol)
            print("\n" + self.print_grid() + "\n")

        while True:
            win = self.user_move(player_symbol)
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Player wins!")
                print("\n" + self.print_grid())
                break

            draw = self.check_draw()
            if draw:
                print("Draw!")
                break
            
            time.sleep(0.5)
            win = self.easy_move(bot_symbol)
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Easy Bot wins!")
                print("\n" + self.print_grid())
                break

            draw = self.check_draw()
            if draw:
                print("Draw!")
                break
        
        return 0

    def play_tictactoe(self):
        print("Enter mode (0: 2-Player, 1: Easy Bot, 2: Hard Bot):")
        self.mode = int(input())

        while self.mode < 0 or self.mode > 2:
            print("Invalid mode. Enter 0, 1, or 2:")
            self.mode = int(input())

        mode_name = ""
        if self.mode == 0:
            mode_name = "2-Player"
        elif self.mode == 1:
            mode_name = "Easy Bot"
        else:
            mode_name = "Hard Bot"

        print(f"\nYou picked: {mode_name}\n")

        sample_grid_string = "  1  |  2  |  3  \n-----|-----|-----\n  4  |  5  |  6  \n-----|-----|-----\n  7  |  8  |  9  "
        print(f"To mark a cell, enter the corresponding number as shown below:\n\n{sample_grid_string}\n________________________________________\n")

        if self.mode == 0:
            self.play_2p()
        elif self.mode == 1:
            self.play_easy()
    
game = TicTacToe()

game.play_tictactoe()