import copy

class SudokuSolver:
    """
    Solves a Sudoku puzzle using backtracking (OOP, Functions, Data Structures).
    """
    
    def __init__(self, grid):
        """
        Initializes the solver with a 9x9 grid (list of lists).
        """
        # Use deepcopy to avoid modifying the original puzzle
        self.grid = copy.deepcopy(grid)
        self.original_puzzle = copy.deepcopy(grid)

    def find_empty_location(self):
        """
        Finds the first empty cell (represented by 0).
        Returns a tuple (row, col) or (None, None) if no empty cell is found.
        """
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    return r, c
        return None, None

    def is_valid(self, row, col, num):
        """
        Checks if a number 'num' is valid to place at grid[row][col].
        (Basic Programming Concepts)
        """
        # Check row
        for c in range(9):
            if self.grid[row][c] == num:
                return False
        
        # Check column
        for r in range(9):
            if self.grid[r][col] == num:
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if self.grid[r][c] == num:
                    return False
        
        return True

    def solve(self):
        """
        Solves the Sudoku puzzle using a recursive backtracking algorithm.
        (Functions, Basic Programming Concepts)
        """
        row, col = self.find_empty_location()
        
        # Base case: If no empty location, puzzle is solved
        if row is None:
            return True
            
        # Try numbers 1-9
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                # Make a tentative move
                self.grid[row][col] = num
                
                # Recurse
                if self.solve():
                    return True
                
                # If recursion fails, backtrack
                self.grid[row][col] = 0
                
        # Trigger backtracking
        return False

    def get_solution(self):
        """
        Returns the solved grid.
        """
        if self.solve():
            return self.grid
        else:
            return None # Should not happen for a valid puzzle
            
    def get_original_puzzle(self):
        """
        Returns the original puzzle grid.
        """
        return self.original_puzzle