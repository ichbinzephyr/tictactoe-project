import unittest
from src.tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board(self):
        self.assertEqual(self.game.board, [[' ' for _ in range(3)] for _ in range(3)])

    def test_available_moves(self):
        self.assertEqual(self.game.available_moves(), [(r, c) for r in range(3) for c in range(3) if self.game.board[r][c] == ' '])

    def test_empty_squares(self):
        self.assertTrue(self.game.empty_squares())
        self.game.board = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
        self.assertFalse(self.game.empty_squares())

    def test_num_empty_squares(self):
        self.assertEqual(self.game.num_empty_squares(), 9)
        self.game.board[0][0] = 'X'
        self.assertEqual(self.game.num_empty_squares(), 8)

    def test_make_move(self):
        self.assertTrue(self.game.make_move((0, 0), 'X'))
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertFalse(self.game.make_move((0, 0), 'O'))

    def test_winner(self):
        self.game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(self.game.winner((0, 0), 'X'))
        self.game.board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertTrue(self.game.winner((0, 0), 'X'))
        self.game.board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(self.game.winner((0, 0), 'X'))
        self.game.board = [[' ', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']]
        self.assertTrue(self.game.winner((0, 2), 'X'))
        self.game.board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertFalse(self.game.winner((0, 0), 'X'))

if __name__ == '__main__':
    unittest.main()
