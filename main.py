import random
from helpers import getRandom, getImmutable

class SudokuSolver:

    def __init__(self, startingSudoku: str) -> None:
    
        self.sudoku = [ 
            [int(i) for i in line] 
            for line in startingSudoku.split()
        ]

        # set of all the indexes that cannot be changed / are fixed
        self.immutable = getImmutable(self.sudoku)
        
        self.solve()

        print("\n")


    @staticmethod
    def PrintSudoku(sudoku):
        print("\n")

        for i in range(len(sudoku)):
            line = ""
            if i == 3 or i == 6:
                print("---------------------")
            for j in range(len(sudoku[i])):
                if j == 3 or j == 6:
                    line += "| "
                line += str(sudoku[i][j]) + " "
            print(line)
            
        print("\n")


    def solve(self):
        self.PrintSudoku(self.sudoku)
        self.getRandomState()
        self.PrintSudoku(self.sudoku)

    
    def getRandomState(self):
        
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

        # print(f"unique -> {unique} | toFill = {toFill}")
        # choosing `toFill` random numbers from [1, 9] that don't exist in `unique`
        
        randomNumbers = getRandom(toFill, unique)
        # print(f"recieved randoms -> { randomNumbers }")

        # now filling block with `randomNumbers` sequentially
        for r in range(x*3, x*3+3):
            for c in range(y*3, y*3+3):
                if not self.sudoku[r][c]:
                    self.sudoku[r][c] = randomNumbers.pop()
        
        # print(f"block[{x}][{y}] filled.")



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