#Enkapsuliacija? Atributai paslepti ir juos galima pasiekti tik per pateiktus metodus.
#Abstrakcija? Paslepiama, kaip keiciamos busenos.
class Cell:

    #Aprasoma kokie pradinio langelio parametrai
    def __init__(self):
        self.is_bomb = False
        self.is_marked = False
        self.is_revealed = False
        self.adjacent_bombs = 0

    #Isjungimo/ijungimo "mygtukas" minos zymejimu. Kai iskvieciamas metodas, sokineja is False i True. (COMMAND)
    def mark(self):
        self.is_marked = not self.is_marked

    #Kai iskvieciamas reveal metodas, langelio busena tampa revealed. (reveal_cell, reveal_all_bombs)
    def reveal(self):
        self.is_revealed = True

    #Atlikus reset, visi langeliai grizta i pradines busenas. (restart_game)
    def reset(self):
        self.is_bomb = False
        self.is_marked = False
        self.is_revealed = False
        self.adjacent_bombs = 0