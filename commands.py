from abc import ABC, abstractmethod


#Inheritance? RevealCellCommand ir MarkCellCommand paveldi Command klases metodus ir atritubutus, teoriskai.
#Command pattern.
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

#Langelio atverimo komanda
class RevealCellCommand(Command):

    # Aprasomi parametrai reikalingi langelio atverimo komandai atlikti
    def __init__(self, board, row, col):
        self.board = board
        self.row = row
        self.col = col

    #Aprasoma kaip atveriamas langelis
    def execute(self):
        self.board.reveal_cell(self.row, self.col)


#Langelio pazymejimo kaip minos komanda
class MarkCellCommand(Command):

    # Aprasomi parametrai reikalingi langelio atverimo komandai atlikti
    def __init__(self, board, row, col):
        self.board = board
        self.row = row
        self.col = col

    # Aprasoma kaip pazymimas langelis
    def execute(self):
        self.board.board[self.row][self.col].mark()
