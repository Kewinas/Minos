import unittest
from board import Board
from settings import ROWS, COLS, NUM_BOMBS


class TestBoard(unittest.TestCase):
    def test_reset_method_with_reveal_cell(self):
        board = Board(rows=ROWS, cols=COLS, num_bombs=NUM_BOMBS)

        #Atidengiami langeliai testavimui
        board.reveal_cell(0, 0)
        board.reveal_cell(1, 1)

        #Resetinama lenta
        board.reset()

        #Tikrinama ar grazina "false", nes resetinus lenta, cell nebeturi buti atidengti.
        self.assertFalse(board.board[0][0].is_revealed, "Po reset, langelis neturi buti atviras")
        self.assertFalse(board.board[1][1].is_revealed, "Po reset, langelis neturi buti atviras")


if __name__ == "__main__":
    unittest.main()
