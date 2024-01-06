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
        move = input("Enter move (1 - 9) or 'h' to view grid indices: ")

        if move.lower() == 'h':
            sample_grid_string = "  1  |  2  |  3  \n-----|-----|-----\n  4  |  5  |  6  \n-----|-----|-----\n  7  |  8  |  9  "
            print(f"________________________________________\n\nTo mark a cell, enter the corresponding number as shown below:\n\n{sample_grid_string}\n________________________________________\n")
            print(self.print_grid() + "\n")
            return self.user_move(symbol)
        elif not move.isnumeric() or (move.isnumeric and (int(move) < 1 or int(move) > 9)):
            print("Illegal move. Try again!")
            print("\n" + self.print_grid() + "\n")
            return self.user_move(symbol)
        
        move = int(move)

        if self.grid[move - 1] == " ":
            self.grid[move - 1] = symbol
            return self.check_win()
        else:
            print("Cell is not empty. Try again!")
            print("\n" + self.print_grid() + "\n")
            return self.user_move(symbol)

    def easy_move(self, symbol):
        possible_moves = []
        for i in range(len(self.grid)):
            if self.grid[i] == " ":
                possible_moves.append(i)
        
        bot_move = random.choice(possible_moves)
        self.grid[bot_move] = symbol
        print(f"Easy Bot move: {bot_move + 1}")

        return self.check_win()
    
    def hard_evaluate(self, depth, symbol):
        win, winner, _ = self.check_win()

        if win:
            return 10 - depth if winner == symbol else -10 + depth
        elif self.check_draw():
            return 0
        
        return None

    def hard_minimax(self, depth, maximizing, symbol):
        score = self.hard_evaluate(depth, symbol)

        player_symbol = "O"

        if symbol == "O":
            player_symbol = "X"

        if score != None:
            return score
        
        if maximizing:
            best_score = float('-inf')
            for i in range(9):
                if self.grid[i] == " ":
                    self.grid[i] = symbol
                    score = self.hard_minimax(depth + 1, False, symbol)
                    self.grid[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.grid[i] == " ":
                    self.grid[i] = player_symbol
                    score = self.hard_minimax(depth + 1, True, symbol)
                    self.grid[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def hard_move(self, symbol, first_move):
        if first_move:
            self.grid[4] = symbol
            print(f"Hard Bot move: {5}")

            return self.check_win()

        best_score = float('-inf')
        best_move = None

        for i in range(9):
            if self.grid[i] == " ":
                self.grid[i] = symbol
                score = self.hard_minimax(0, False, symbol)
                self.grid[i] = " "

                if score > best_score:
                    best_score = score
                    best_move = i

        self.grid[best_move] = symbol
        print(f"Hard Bot move: {best_move + 1}")

        return self.check_win()
    
    def check_win(self):
        if self.grid[0] == self.grid[1] == self.grid[2] != " ":
            return True, self.grid[0], 1
        elif self.grid[3] == self.grid[4] == self.grid[5] != " ":
            return True, self.grid[3], 2
        elif self.grid[6] == self.grid[7] == self.grid[8] != " ":
            return True, self.grid[6], 3
        elif self.grid[0] == self.grid[3] == self.grid[6] != " ":
            return True, self.grid[0], 4
        elif self.grid[1] == self.grid[4] == self.grid[7] != " ":
            return True, self.grid[1], 5
        elif self.grid[2] == self.grid[5] == self.grid[8] != " ":
            return True, self.grid[2], 6
        elif self.grid[0] == self.grid[4] == self.grid[8] != " ":
            return True, self.grid[0], 7
        elif self.grid[2] == self.grid[4] == self.grid[6] != " ":
            return True, self.grid[2], 8
        
        return False, None, 0
    
    def check_draw(self):
        if " " not in self.grid:
            return True
        
        return False
    
    def print_grid(self):
        grid_string = f"  {self.grid[0]}  |  {self.grid[1]}  |  {self.grid[2]}  \n-----|-----|-----\n  {self.grid[3]}  |  {self.grid[4]}  |  {self.grid[5]}  \n-----|-----|-----\n  {self.grid[6]}  |  {self.grid[7]}  |  {self.grid[8]}  "
        return grid_string
    
    def print_win_grid(self, win_dir):
        if win_dir == 1:
            grid_string = f"  ―  |  ―  |  ―  \n-----|-----|-----\n  {self.grid[3]}  |  {self.grid[4]}  |  {self.grid[5]}  \n-----|-----|-----\n  {self.grid[6]}  |  {self.grid[7]}  |  {self.grid[8]}  "
        elif win_dir == 2:
            grid_string = f"  {self.grid[0]}  |  {self.grid[1]}  |  {self.grid[2]}  \n-----|-----|-----\n  ―  |  ―  |  ―  \n-----|-----|-----\n  {self.grid[6]}  |  {self.grid[7]}  |  {self.grid[8]}  "
        elif win_dir == 3:
            grid_string = f"  {self.grid[0]}  |  {self.grid[1]}  |  {self.grid[2]}  \n-----|-----|-----\n  {self.grid[3]}  |  {self.grid[4]}  |  {self.grid[5]}  \n-----|-----|-----\n  ―  |  ―  |  ―  "
        elif win_dir == 4:
            grid_string = f"  |  |  {self.grid[1]}  |  {self.grid[2]}  \n-----|-----|-----\n  |  |  {self.grid[4]}  |  {self.grid[5]}  \n-----|-----|-----\n  |  |  {self.grid[7]}  |  {self.grid[8]}  "
        elif win_dir == 5:
            grid_string = f"  {self.grid[0]}  |  |  |  {self.grid[2]}  \n-----|-----|-----\n  {self.grid[3]}  |  |  |  {self.grid[5]}  \n-----|-----|-----\n  {self.grid[6]}  |  |  |  {self.grid[8]}  "
        elif win_dir == 6:
            grid_string = f"  {self.grid[0]}  |  {self.grid[1]}  |  |  \n-----|-----|-----\n  {self.grid[3]}  |  {self.grid[4]}  |  |  \n-----|-----|-----\n  {self.grid[6]}  |  {self.grid[7]}  |  |  "
        elif win_dir == 7:
            grid_string = f"  ⟍  |  {self.grid[1]}  |  {self.grid[2]}  \n-----|-----|-----\n  {self.grid[3]}  |  ⟍  |  {self.grid[5]}  \n-----|-----|-----\n  {self.grid[6]}  |  {self.grid[7]}  |  ⟍  "
        elif win_dir == 8:
            grid_string = f"  {self.grid[0]}  |  {self.grid[1]}  |  ⟋  \n-----|-----|-----\n  {self.grid[3]}  |  ⟋  |  {self.grid[5]}  \n-----|-----|-----\n  ⟋  |  {self.grid[7]}  |  {self.grid[8]}  "
        else:
            grid_string = f"  {self.grid[0]}  |  {self.grid[1]}  |  {self.grid[2]}  \n-----|-----|-----\n  {self.grid[3]}  |  {self.grid[4]}  |  {self.grid[5]}  \n-----|-----|-----\n  {self.grid[6]}  |  {self.grid[7]}  |  {self.grid[8]}  "

        return grid_string

    def play_2p(self):
        print("Player 1 Symbol: X")
        print("Player 2 Symbol: O\n")

        win = False
        win_dir = 0

        print(self.print_grid() + "\n")

        while True:
            print("Player 1")
            win, _, win_dir = self.user_move('X')
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Player 1 wins!")
                print("\n" + self.print_win_grid(win_dir))
                break

            draw = self.check_draw()
            if draw:
                print("Draw!")
                break

            print("Player 2")
            win, _, win_dir = self.user_move('O')
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Player 2 wins!")
                print("\n" + self.print_win_grid(win_dir))
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
        win_dir = 0

        print(self.print_grid() + "\n")

        if first_player == 1:
            win = self.easy_move(bot_symbol)
            print("\n" + self.print_grid() + "\n")

        while True:
            win, _, win_dir = self.user_move(player_symbol)
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Player wins!")
                print("\n" + self.print_win_grid(win_dir))
                break

            draw = self.check_draw()
            if draw:
                print("Draw!")
                break
            
            time.sleep(0.5)
            win, _, win_dir = self.easy_move(bot_symbol)
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Easy Bot wins!")
                print("\n" + self.print_win_grid(win_dir))
                break

            draw = self.check_draw()
            if draw:
                print("Draw!")
                break
        
        return 0
    
    def play_hard(self):
        first_player = random.randint(0, 1)

        player_symbol = "X"
        bot_symbol = "O"

        if first_player == 1:
            player_symbol = "O"
            bot_symbol = "X"

        print(f"Player Symbol: {player_symbol}")
        print(f"Hard Bot Symbol: {bot_symbol}\n")

        if first_player == 0:
            print("Player goes first!\n")
        else:
            print("Hard Bot goes first!\n")

        win = False
        win_dir = 0

        print(self.print_grid() + "\n")

        if first_player == 1:
            win, _, win_dir = self.hard_move(bot_symbol, True)
            print("\n" + self.print_grid() + "\n")

        while True:
            win, _, win_dir = self.user_move(player_symbol)
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Player wins!")
                print("\n" + self.print_win_grid(win_dir))
                break

            draw = self.check_draw()
            if draw:
                print("Draw!")
                break
            
            time.sleep(0.5)
            win, _, win_dir = self.hard_move(bot_symbol, False)
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Hard Bot wins!")
                print("\n" + self.print_win_grid(win_dir))
                break

            draw = self.check_draw()
            if draw:
                print("Draw!")
                break

        return 0

    def pick_mode_play(self, prev_mode):
        if prev_mode == -1:
            self.mode = int(input("Enter mode (1: 2-Player, 2: Easy Bot, 3: Hard Bot): "))

            while self.mode < 1 or self.mode > 3:
                self.mode = int(input("Invalid mode. Enter 1, 2, or 3: "))
        else:
            self.mode = prev_mode

        mode_name = ""
        if self.mode == 1:
            mode_name = "2-Player"
        elif self.mode == 2:
            mode_name = "Easy Bot"
        else:
            mode_name = "Hard Bot"

        print(f"\nNow Playing: {mode_name}\n")

        sample_grid_string = "  1  |  2  |  3  \n-----|-----|-----\n  4  |  5  |  6  \n-----|-----|-----\n  7  |  8  |  9  "
        print(f"To mark a cell, enter the corresponding number as shown below:\n\n{sample_grid_string}\n________________________________________\n")

        if self.mode == 1:
            self.play_2p()
            return 1
        elif self.mode == 2:
            self.play_easy()
            return 2
        elif self.mode == 3:
            self.play_hard()
            return 3
    
def play_tictactoe():
    cont = True
    prev_mode = -1

    while cont:
        tictactoe = TicTacToe()

        prev_mode = tictactoe.pick_mode_play(prev_mode)
        
        print("________________________________________")

        cont = input("\nPlay Again (Y/N): ").lower() == 'y'
        repeat = False

        if cont:
            repeat = input("Same Mode (Y/N): ").lower() == 'y'

        if not repeat:
            prev_mode = -1

        print("________________________________________\n")

play_tictactoe()