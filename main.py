class SudokuSolver:

    def __init__(self, startingSudoku: str) -> None:
    
        self.sudoku = [ 
            [int(i) for i in line] 
            for line in startingSudoku.split()
        ]
        
        self.solve()


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

    
    def fillBlock(self):
        pass





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