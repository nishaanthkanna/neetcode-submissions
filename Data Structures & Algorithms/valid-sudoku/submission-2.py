from copy import copy
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = {}
        # better to save as a row, column number flag to check row, cou,n wise occurence faster
        sudoku_sub = defaultdict(list)
        # check for duplicates within grid
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number != '.':
                    sudoku[number] = sudoku.get(number, ([0]*9, [0]*9))
                    sudoku[number][0][i] += 1
                    sudoku[number][1][j] += 1
                    # assign grid number
                    gr, gc = i//3, j//3
                    sudoku_sub[number].append((gr, gc))
   
        # check for rule 1, rule 2
        for i in sudoku.keys():
            r, c = sudoku[i]
            for j in range(9):
                if r[j] > 1 or c[j] > 1:
                    return False
            # check rule 3
            grid = sudoku_sub[i]
            if len(set(grid)) != len(grid):
                return False
        return True

        