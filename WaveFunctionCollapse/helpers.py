import random


def getImmutable(sudoku: list[list[int]]) -> set:
    """returns set of indexes which are immutable in the sudoku"""
    immutable = set()

    for r in range(9):
        for c in range(9):
            if sudoku[r][c] != 0:
                immutable.add( (r, c) )
    
    return immutable


def calculateError(sudoku: list[list[int]]) -> int:
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