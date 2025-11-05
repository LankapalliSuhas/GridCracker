import random

# This file acts as a module with functions.

def load_base_grid(filepath="base_grid.txt"):
    """
    Loads a solved Sudoku grid from a text file.
    (File Handling, Data Structures)
    """
    grid = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                # Basic Programming: stripping whitespace and splitting
                row_str = line.strip().split(',')
                # Data Structure: list comprehension to convert to int
                row_int = [int(num) for num in row_str if num.isdigit()]
                if len(row_int) == 9:
                    grid.append(row_int)
        
        if len(grid) != 9:
            print(f"Error: Base grid file '{filepath}' is not valid.")
            return get_fallback_grid()
            
        return grid
        
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found. Using fallback grid.")
        return get_fallback_grid()
    except Exception as e:
        print(f"Error reading file: {e}. Using fallback grid.")
        return get_fallback_grid()

def get_fallback_grid():
    """
    Provides a hardcoded grid if file loading fails.
    """
    return [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

def generate_puzzle(difficulty="medium"):
    """
    This is our simple "AI" puzzle generator.
    It takes a solved grid and removes numbers.
    (Functions, Basic Programming Concepts)
    """
    base_grid = load_base_grid()
    
    # Make a copy to create the puzzle
    puzzle = [row[:] for row in base_grid] # Data Structure
    
    # Determine how many cells to empty
    if difficulty == "easy":
        cells_to_remove = 30
    elif difficulty == "hard":
        cells_to_remove = 50
    else: # Medium
        cells_to_remove = 40
        
    # Create a list of all cell coordinates (Data Structure)
    all_cells = [(r, c) for r in range(9) for c in range(9)]
    
    # Randomly select cells to remove (Basic Concepts)
    cells_to_empty = random.sample(all_cells, cells_to_remove)
    
    for row, col in cells_to_empty:
        puzzle[row][col] = 0
        
    return puzzle