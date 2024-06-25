import sys

class TicTacToe:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Cell already occupied.")

    def check_winner(self):
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != ' ':
                return row[0]

        for col in range(len(self.board[0])):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]

        return None

    def minimax(self, depth, alpha, beta, maximizing_player):
        winner = self.check_winner()
        if winner:
            if winner == 'X':
                return -10 + depth, None
            elif winner == 'O':
                return 10 - depth, None
            else:
                return 0, None

        if maximizing_player:
            max_eval = -sys.maxsize
            best_move = None
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        eval, _ = self.minimax(depth + 1, alpha, beta, False)
                        self.board[i][j] = ' '
                        if eval > max_eval:
                            max_eval = eval
                            best_move = (i, j)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval, best_move
        else:
            min_eval = sys.maxsize
            best_move = None
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        eval, _ = self.minimax(depth + 1, alpha, beta, True)
                        self.board[i][j] = ' '
                        if eval < min_eval:
                            min_eval = eval
                            best_move = (i, j)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval, best_move

# Example usage:
game = TicTacToe()
game.make_move(0, 0)
game.make_move(1, 1)
game.make_move(0, 1)
game.make_move(1, 2)
game.make_move(0, 2)
game.make_move(2, 2)
game.print_board()

eval, (row, col) = game.minimax(0, -sys.maxsize, sys.maxsize, False)
game.make_move(row, col)
game.print_board()
winner = game.check_winner()
if winner:
    print(f"Winner: {winner}")
else:
    print("It's a tie!")
