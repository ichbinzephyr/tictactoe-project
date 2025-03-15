class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def empty_squares(self):
        return ' ' in [square for row in self.board for square in row]

    def num_empty_squares(self):
        return len(self.available_moves())

    def make_move(self, square, letter):
        if self.board[square[0]][square[1]] == ' ':
            self.board[square[0]][square[1]] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind, col_ind = square
        row = self.board[row_ind]
        if all([s == letter for s in row]):
            return True
        col = [self.board[r][col_ind] for r in range(3)]
        if all([s == letter for s in col]):
            return True
        if square[0] == square[1]:
            diagonal1 = [self.board[i][i] for i in range(3)]
            if all([s == letter for s in diagonal1]):
                return True
        if square[0] + square[1] == 2:
            diagonal2 = [self.board[i][2-i] for i in range(3)]
            if all([s == letter for s in diagonal2]):
                return True
        return False
