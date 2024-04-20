
class BitMask:
    
    @staticmethod
    def get1BitIndexes(n: int, asarray: bool = False):
        res = []
        index = 1
        while n:
            if n & 1 == 1: res.append( index )
            n = n >> 1
            index += 1
        
        if asarray: return res
        # return '[' + ",".join( [str(x) for x in res] ) + ']'

        binary = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        for i in res: binary[i-1] = '1'
        return "".join(binary[::-1])

    @staticmethod
    def getEntropy(n: int):
        return n.bit_count()
    


class SuperPositions:

    def __init__(self) -> None:
        self.superpositions = [
            [int('111111111', 2) for c in range(9)]
            for r in range(9)
        ]
    

    def initSuperpositions(self, sudoku: list[list], immutable: set) -> list[list]:
        print("super positions initialized for given sudoku")

        # filling superposition matrix
        for r in range(9):
            for c in range(9):
                if (r, c) in immutable:
                    # only set that bit to 1 else all to 0
                    self.superpositions[r][c] = (1 << (sudoku[r][c] - 1))
        
        # updating neighboring superpositions from immutable sudoku positions
        for (r, c) in immutable:
            self.updateSuperpositions(sudoku, r, c)
                


    def updateSuperpositions(self, sudoku, r, c):
        """
        updating relevant superpositions[r][c] to update neighboring superpositions
        (r, c) is the row and column that is considered when updating neighbor superpositions
        """
        
        # collapse wave function of `self.superpositions[r][c]` to `sudoku[r][c]`
        self.superpositions[r][c] = (1 << (sudoku[r][c] - 1))

        # remove `sudoku[r][c]` from superpositions of each node in row `r`
        for j in range(9):
            if j == c: continue
            if self.superpositions[r][j] & (1 << (sudoku[r][c] - 1)) == 0: continue  # ignore if its not in the superpositions of [r][j]
            self.superpositions[r][j] = self.superpositions[r][j] ^ (1 << (sudoku[r][c] - 1))

        # remove `sudoku[r][c]` from superpositions of each node in column `c`
        for i in range(9):
            if i == r: continue
            if self.superpositions[i][c] & (1 << (sudoku[r][c] - 1)) == 0: continue  # ignore if its not in the superpositions of [i][c]
            self.superpositions[i][c] = self.superpositions[i][c] ^ (1 << (sudoku[r][c] - 1))
        
        # remove `sudoku[r][c]` from superpositions of each node in the sudoku block to which [r][c] belongs
        

    
    def getLowestEntropyIndex(self) -> tuple:
        """
        return the sudoku position with the lowest entropy
        the lowest number of superpositions have the lowest entropy
        """

        candidate, entropy = None, float('inf')

        for r in range(9):
            for c in range(9):
                # print(f"{(r, c)} -> {BitMask.get1BitIndexes(self.superpositions[r][c])} -> {BitMask.getEntropy(self.superpositions[r][c])}")
                if BitMask.getEntropy(self.superpositions[r][c]) != 1 and BitMask.getEntropy(self.superpositions[r][c]) < entropy:
                    candidate = (r, c)
                    entropy = BitMask.getEntropy(self.superpositions[r][c])

        return candidate, BitMask.get1BitIndexes(self.superpositions[candidate[0]][candidate[1]], asarray=True)
            

    def __repr__(self) -> str:
        
        representation = "SUPERPOSITION MATRIX :-\n"

        for i in range(len(self.superpositions)):
            line = ""
            if i == 3 or i == 6:
                representation += "---------------------\n"
            for j in range(len(self.superpositions[i])):
                if j == 3 or j == 6:
                    line += "| "
                line += "_ " if self.superpositions[i][j] & 511 == 511 else BitMask.get1BitIndexes(self.superpositions[i][j]) + " " 
                # line += BitMask.get1BitIndexes(self.superpositions[i][j]) + " " 
            representation += line + "\n"
        
        return representation
    


