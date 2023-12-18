from cell import Cell
from settings import ROWS, COLS, NUM_BOMBS
import random


class Board:
    # SINGLETON pattern (Užtikrina, kad yra tik viena lenta, kad ir kiek ju butu sukurta)
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Board, cls).__new__(cls)
        return cls._instance

    def __init__(self, rows=None, cols=None, num_bombs=None):
        if not self._initialized:
            self.rows = rows if rows is not None else ROWS
            self.cols = cols if cols is not None else COLS
            self.num_bombs = num_bombs if num_bombs is not None else NUM_BOMBS

            #Sukuriama tam tikro dydzio lenta
            self.board = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]
            self.place_bombs()

    #Sudedamos minos
    def place_bombs(self):

        #Sugeneruoja sarasa vietu kur bus sudedamos minos
        bomb_positions = random.sample(range(self.rows * self.cols), self.num_bombs)

        #I visas sugeneruotas vietas sudedamos minos, priskiriama True
        for position in bomb_positions:
            row = position // self.cols
            col = position % self.cols
            self.board[row][col].is_bomb = True

    #Skaiciuoja, kiek salia saves kiekvienas langelis turi minu
    def get_adjacent_bombs(self, row, col):
        adjacent_bombs = 0

        #Tikrina 3x3 principu aplinkinius langelius
        #(-1; -1) (-1; 0) (-1; 1)
        #(0; -1)  (0; 0)  (0; 1)
        #(1; -1)  (1; 0)  (1; 1)
        for i in range(-1, 2):
            for j in range(-1, 2):

                #Saves netikrina
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j

                #Prie minu sumos pridedami tik tie langeliai, kurie yra lentoje ir yra minos
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.board[new_row][new_col].is_bomb:
                    adjacent_bombs += 1
        return adjacent_bombs

    #Lentos resetinimas, sukuriami langeliai ir sudedamos bombos.
    def reset(self):
        self.board = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]
        self.place_bombs()

    #Langelio atidengimas
    def reveal_cell(self, row, col):
        #Jei langelio pozicija yra neteisinga arba langelis yra jau atvertas tuomet praleidziama
        if not self.is_valid_position(row, col) or self.board[row][col].is_revealed:
            return

        #Langelio busena pakeiciama i revealed
        self.board[row][col].reveal()

        #Jei salia nera bombu, tuomet atveriami salia esantys langeliai ir pats paspaustas langelis
        if self.get_adjacent_bombs(row, col) == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.reveal_cell(row + i, col + j)

    #Tikrina ar langelio pozicija yra teisinga, telpa i lenta
    def is_valid_position(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
