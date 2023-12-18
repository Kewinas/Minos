import unittest
from board import Board
from commands import RevealCellCommand, MarkCellCommand

class TestCommandPattern(unittest.TestCase):

    def setUp(self):
        self.board = Board(rows=5, cols=5, num_bombs=5)

    #Tikrinamas Reveal Cell komandos veikimas
    def test_reveal_cell_command(self):
        row, col = 0, 0

        #Aprasoma komanda, siuo atveju RevealCell ir aprasomos koordinates kuri langeli atidengti
        command = RevealCellCommand(self.board, row, col)
        command.execute()

        #Tikrinama, ar langelis atidengtas, jei neatidengtas ismetama klaida
        self.assertTrue(self.board.board[row][col].is_revealed, "Cell should be revealed")

    # Tikrinamas Mark Cell komandos veikimas
    def test_mark_cell_command(self):
        row, col = 0, 0

        # Aprasoma komanda, siuo atveju MarkCell ir aprasomos koordinates kuri langeli pazymeti kaip mina
        command = MarkCellCommand(self.board, row, col)
        command.execute()

        # Tikrinama, ar langelis pazymetas, jei nepazymetas, testas nesekmingas
        self.assertTrue(self.board.board[row][col].is_marked, "Cell should be marked")


if __name__ == '__main__':
    unittest.main()
