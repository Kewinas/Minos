from gui import MinesweeperGUI
import tkinter as tk
from settings import ROWS, COLS, NUM_BOMBS

#Main funkcija
def main():
    root = tk.Tk()
    game = MinesweeperGUI(root, ROWS, COLS, NUM_BOMBS)
    root.mainloop()


if __name__ == "__main__":
    main()
