import random
import os, time
from helpers import getImmutable, calculateError
from superpostions import SuperPositions


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

        self.superObj = SuperPositions()
        self.superObj.initSuperpositions(self.sudoku, self.immutable)

        print(self.superObj)

        while self.superObj.getLowestEntropyIndex(self.immutable):
            self.solveLowestEntropy()
            print(self)
            print(self.superObj)
            print(f"error -> {calculateError(self.sudoku)}")
            time.sleep(0.5); os.system('clear')

    
    def solveLowestEntropy(self):
        """gets the lowest entropy superpositions from the matrix and collapses its wave function"""

        (r, c), superpositions = self.superObj.getLowestEntropyIndex(self.immutable)
        # print(r, c, superpositions)

        # collapse the superpositions of `sudoku[r][c]`
        candidate = random.choice(superpositions)  # this is the new candidate from the collapsed superpositions
        # print(f"candidate selected -> {candidate}")

        self.sudoku[r][c] = candidate
        self.immutable.add( (r, c) )

        self.superObj.updateSuperpositions(self.sudoku, r, c)


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