import unittest
from board import Board


class TestSingletonPattern(unittest.TestCase):

    #Tikrinama ar yra tik vienas lentos instance, nepriklausomai nuo to kiek lentu sukuriama
    def test_singleton_instance(self):

        #Sukuriamos 2 lentos
        board1 = Board()
        board2 = Board()

        #Jei Singleton patternas veikia teisingai, tai tuomet bus tik vienas instance
        self.assertIs(board1, board2, "Board instances are not the same")


    def test_singleton_initialized_once(self):

        #Sukuriamos 2 lentos, su skirtingais parametrais
        board1 = Board(rows=10, cols=10, num_bombs=20)
        board2 = Board(rows=5, cols=5, num_bombs=5)

        #Tikrinama ar ivedus skirtingus parametrus, bus islaikomas vienas board instance su tokiais paciais paremetrais.
        self.assertEqual(board1.rows, board2.rows, "Rows should be the same")
        self.assertEqual(board1.cols, board2.cols, "Cols should be the same")
        self.assertEqual(board1.num_bombs, board2.num_bombs, "Number of bombs should be the same")


if __name__ == '__main__':
    unittest.main()
