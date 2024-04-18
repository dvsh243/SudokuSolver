import random
import os, time
from helpers import getImmutable


class SudokuSolver:

    def __init__(self, startingSudoku: str) -> None:
    
        self.sudoku = [ 
            [int(i) for i in line] 
            for line in startingSudoku.split()
        ]

        # set of all the indexes that cannot be changed / are fixed
        self.immutable = getImmutable(self.sudoku)
        print(f"SudokuSolver class initialized.")

        print(self)


    def updateSuperpositions():
        return

    def getSuperpositions():
        return

    def propagateEffect():
        return


    def __repr__(self) -> str:
        """prints the current sudoku board"""
        representation = "\n"

        for i in range(len(self.sudoku)):
            line = ""
            if i == 3 or i == 6:
                # print("---------------------")
                representation += "---------------------\n"
            for j in range(len(self.sudoku[i])):
                if j == 3 or j == 6:
                    line += "| "
                line += str(self.sudoku[i][j]) + " "
            # print(line)
            representation += line + "\n"
        
        return representation





if __name__ == "__main__":

    startingSudoku = """
                        024007000
                        600000000
                        003680415
                        431005000
                        500000032
                        790000060
                        209710800
                        040093000
                        310004750
                    """
    
    SudokuSolver(startingSudoku)