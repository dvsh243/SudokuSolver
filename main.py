import random
import os, time
from helpers import getRandom, getImmutable, getCopy, acceptState

class SudokuSolver:

    def __init__(self, startingSudoku: str) -> None:
    
        self.sudoku = [ 
            [int(i) for i in line] 
            for line in startingSudoku.split()
        ]

        # set of all the indexes that cannot be changed / are fixed
        self.immutable = getImmutable(self.sudoku)
        print(f"SudokuSolver class initialized.")

        self.simulatedAnnealing()

        print("\n")


    def simulatedAnnealing(self, stopTemp: float = 0.003, decay: float = 0.995):
        print(self)
        self.RandomInitialize()
        print("intialized random state...")
        print(self)

        curTemp = 1

        while curTemp > stopTemp:

            tempState = self.randomSwap()  # temporary state that holds a copy of the sudoku
            print(self)

            if (
                self.calculateError(self.sudoku) > self.calculateError(tempState) and 
                acceptState(curTemp)
            ):
                self.sudoku = tempState

            print(f"curTemp = {curTemp}")
            print(f"error -> {self.calculateError(self.sudoku)}")

            os.system('clear')
            curTemp = curTemp * decay
        

        print(self)
        print(f"error -> {self.calculateError(self.sudoku)}")
    
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


##########################################################################
##########################################################################
    
    def RandomInitialize(self):
        
        # `x` & `y` are block indexes.
        for x in range(3):
            for y in range(3):
                self.fillBlock(x, y)
        

    def fillBlock(self, x: int, y: int):
        """ranges --- r -> [{x*3}, {x*3+2}]    c -> [{y*3}, {y*3+2}]"""

        toFill, unique = 0, set()

        for r in range(x*3, x*3+3):
            for c in range(y*3, y*3+3):
                if not self.sudoku[r][c]: 
                    toFill += 1
                    continue
                unique.add( self.sudoku[r][c] )

        # choosing `toFill` random numbers from [1, 9] that don't exist in `unique`
        randomNumbers = getRandom(toFill, unique)

        # now filling block with `randomNumbers` sequentially
        for r in range(x*3, x*3+3):
            for c in range(y*3, y*3+3):
                if not self.sudoku[r][c]:
                    self.sudoku[r][c] = randomNumbers.pop()
        
        # print(f"block[{x}][{y}] filled.")


##########################################################################
##########################################################################
                    
    def randomSwap(self) -> list[list[int]]:
        """create a new random state for the sudoku 
        by selecting a random block and swapping 2 elements in that block"""

        tempSudoku = getCopy(self.sudoku)
        # block ID
        x, y = random.randint(0, 2), random.randint(0, 2)
    
        # getting the immutable indexes for this block
        swapCandidates = []
        for r in range(x*3, x*3+3):
            for c in range(y*3, y*3+3):
                if (r, c) not in self.immutable:
                    swapCandidates.append( (r, c) )
        
        # choosing two swap candidates at random
        s1, s2 = random.choice(swapCandidates), random.choice(swapCandidates)        
        tempSudoku[s1[0]][s1[1]], tempSudoku[s2[0]][s2[1]] = tempSudoku[s2[0]][s2[1]], tempSudoku[s1[0]][s1[1]]
        # print(f"swapped.")

        return tempSudoku
    

    def calculateError(self, sudoku: list[list[int]]) -> int:
        """number of duplicated by row & by column"""
        cost = 0
        
        # row wise iteration
        for r in range(9):
            unique = set()

            for c in range(9):
                if sudoku[r][c] in unique:
                    cost += 1
                unique.add( sudoku[r][c] )

        # column wise iteration
        for c in range(9):
            unique = set()

            for r in range(9):
                if sudoku[r][c] in unique:
                    cost += 1
                unique.add( sudoku[r][c] )
        
        return cost


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