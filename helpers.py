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
    immutable = set()

    for r in range(9):
        for c in range(9):
            if not sudoku[r][c]:
                immutable.add( (r, c) )
    
    return immutable