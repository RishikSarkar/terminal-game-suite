class TicTacToe:
    def __init__(self):
        self.mode = 0
        self.grid = [" "] * 9
    
    def set_mode(self, mode):
        self.mode = mode
    
    def user_move(self, symbol):
        print("Enter move (1 - 9):")
        move = int(input())

        if self.grid[move - 1] == " ":
            self.grid[move - 1] = symbol
            return self.check_win()
        else:
            print("Illegal move. Try again!")
            self.user_move(symbol)
    
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

            print("Player 2")
            win = self.user_move('O')
            print("\n" + self.print_grid() + "\n")

            if win:
                print("Player 2 wins!")
                print("\n" + self.print_grid())
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
    
game = TicTacToe()

game.play_tictactoe()