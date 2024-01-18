import random

def getRandom(count: int, unique: set) -> set:
    """returns `count` random numbers from [1, 9] that dont exist in `unique`"""
    
    numbers = []
    while len(unique) < 9:
        n = random.randint(1, 9)
        if n not in unique: 
            numbers.append(n)
            unique.add(n)
    
    return numbers



def getImmutable(sudoku: list[list[int]]) -> set:
    """returns set of indexes which are immutable in the sudoku"""
    immutable = set()

    for r in range(9):
        for c in range(9):
            if sudoku[r][c] != 0:
                immutable.add( (r, c) )
    
    return immutable


def getCopy(sudoku: list[list[int]]) -> list[list[int]]:
    tempSudoku  = [
        [None for c in range(9)]
        for r in range(9)
    ]

    for r in range(9):
        for c in range(9):
            tempSudoku[r][c] = sudoku[r][c]
    
    return tempSudoku


def acceptState(curTemp: float):
    n = random.random()
    return n < curTemp