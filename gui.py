import tkinter as tk
from board import Board
from commands import RevealCellCommand, MarkCellCommand


class MinesweeperGUI:
    def __init__(self, master, rows, cols, num_bombs):
        self.master = master
        self.master.title("Minesweeper")
        self.rows = rows
        self.cols = cols
        self.num_bombs = num_bombs
        self.board = Board(rows=rows, cols=cols, num_bombs=num_bombs)
        self.buttons = []
        self.create_widgets()

    # Sudeda GUI elementus
    def create_widgets(self):
        self.board = Board(self.rows, self.cols, self.num_bombs)

        for row in range(self.rows):
            button_row = []
            for col in range(self.cols):
                cell_button = tk.Button(
                    self.master,
                    # Langelio parametrai: tekstas ir dydis ir susiejamas bendravimas su handle_click metodu. Atverimu.
                    text="",
                    width=2,
                    height=1,
                    command=lambda r=row, c=col: self.handle_click(r, c),
                )
                # Kiekvienas mygtukas patalpinamas i mygtuku sarasa (specifines eilutes)
                cell_button.grid(row=row, column=col, sticky="nsew")
                button_row.append(cell_button)

                # Susiejamas bendravimas su handle_right_click metodu (zymejim), paspaudus desini mygtuka.
                cell_button.bind("<Button-3>", lambda event, r=row, c=col: self.handle_right_click(r, c))

            # Bendras mygtuku sarasas
            self.buttons.append(button_row)

        # Mygtukas zaidimui pradeti is naujo
        restart_button = tk.Button(
            self.master,
            text="Iš naujo",
            command=self.restart_game
        )
        restart_button.grid(row=self.rows, columnspan=self.cols, sticky="nsew")

    # Valdoma kas vyksta paspaudus kairiu klavisu ant langelio
    def handle_click(self, row, col):

        # Vykdoma RevealCell komanda, kuri turi atverti langeli
        command = RevealCellCommand(self.board, row, col)
        command.execute()

        # Jei langelis yra mina, tuomet zaidimas pralaimimas, vykdomas game_over metodas
        if self.board.board[row][col].is_bomb:
            self.game_over()

        # Jei ne tuomet atnaujimas GUI
        else:
            self.update_gui()

    # Valdoma kas vyksta paspaudus desiniu klavisu ant langelio
    def handle_right_click(self, row, col):

        # Vykdoma MarkCell komanda, kuri turi pazymeti (mina) langeli ir atnaujinti GUI
        command = MarkCellCommand(self.board, row, col)
        command.execute()
        self.update_gui()

    # Lentos atnaujinimas po kiekvieno zingsnio
    def update_gui(self):
        revealed_cells = 0
        marked_bombs = 0

        #Kiekviena karta GUI langelis priskiriamas kaip nenaudotas ir is naujo einama per visa turima informacija.
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.board.board[row][col]
                button_text = ""

                #Jei langelis atvertas
                if cell.is_revealed:
                    revealed_cells += 1

                    #Jei langelis mina, tuomet uzdedamas minai skirtas zenklas
                    if cell.is_bomb:
                        button_text = "B"

                    #Kitu atveju tikrinama kiek langelis turi kaimyniniu minu ir tas skaicius vaizduojamas.
                    else:
                        adjacent_bombs = self.board.get_adjacent_bombs(row, col)
                        button_text = str(adjacent_bombs) if adjacent_bombs > 0 else "0"

                #Jei langelis pazymetas, uzdedamas M zenklas ant langelio
                elif cell.is_marked:
                    marked_bombs += 1
                    button_text = "M"

                #Atnaujinami visi mygtukai (langeliai)
                button = self.buttons[row][col]
                button.config(text=button_text)

        #Jei visi langeliai atverti ir visos minos pazymetos, vykdomas game_won metodas
        if revealed_cells == (self.rows * self.cols - self.num_bombs) and marked_bombs == self.num_bombs:
            self.game_won()

    #Informacines zinutes vaizdavimas, laimejus zaidima
    def game_won(self):
        win_label = tk.Label(self.master, text="Sveikinu, laimėjai.", font=("Times New Roman", 16))
        win_label.grid(row=self.rows + 1, columnspan=self.cols, sticky="nsew")

        self.win_label = win_label

    #Atliekamos funkcijos pradedant zaidima is naujo
    def restart_game(self):

        #Sunaikinami visi mygtukai (langeliai)
        for widget_row in self.buttons:
            for button in widget_row:
                button.destroy()

        #Pasalinamas pralaimeto zaidimo langas
        game_over_label = getattr(self, 'game_over_label', None)
        if game_over_label:
            game_over_label.destroy()

        #Pasalinamas laimeto zaidimo langas
        win_label = getattr(self, 'win_label', None)
        if win_label:
            win_label.destroy()

        # Resetinamas zaidimas
        self.board.reset()

        #Is naujo pradedama initializacija
        self.__init__(self.master, self.rows, self.cols, self.num_bombs)

    #Veiksmai atliekami pralaimejus zaidima
    def game_over(self):

        #Parodoma pralaimejimo zinute
        game_over_label = tk.Label(self.master, text="Pataikei ant minos! Pralaimėjai.", font=("Times New Roman", 16))
        game_over_label.grid(row=self.rows + 1, columnspan=self.cols, sticky="nsew")

        #Issisaugoma informacine zinute, kad kito metodu, ja reikus butu galima pasalinti
        self.game_over_label = game_over_label

        #Rodomos visos minos
        self.reveal_all_bombs()

        #Atnaujinama lenta, kad matytusi minos
        self.master.update()

    #Minu parodymui skirtas metodas
    def reveal_all_bombs(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.board.board[row][col]

                #Jei langelis yra mina, tuomet jis atveriamas ir uzdedama B (minos) raide
                if cell.is_bomb:
                    cell.reveal()
                    button = self.buttons[row][col]
                    button.config(text="B")
