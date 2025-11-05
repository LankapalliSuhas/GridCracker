import streamlit as st
import time

# Import our custom modules
from sudoku_solver import SudokuSolver
from puzzle_generator import generate_puzzle

def display_grid(grid, title, container):
    """
    A helper function to display the 9x9 grid neatly in Streamlit.
    (Functions)
    """
    with container:
        st.subheader(title)
        
        # Custom CSS for a grid-like appearance
        st.markdown("""
        <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(9, 35px);
            grid-template-rows: repeat(9, 35px);
            border: 2px solid #333;
            width: fit-content;
            margin-bottom: 20px;
        }
        .grid-cell {
            width: 35px;
            height: 35px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid #ccc;
            font-size: 1.2em;
            font-weight: bold;
            font-family: 'Courier New', Courier, monospace;
        }
        .grid-cell.zero {
            color: #aaa; /* Lighter color for empty cells */
        }
        /* Add thicker borders for 3x3 blocks */
        .grid-cell:nth-child(3n) { border-right-width: 2px; border-right-color: #333; }
        .grid-cell:nth-child(9n) { border-right: 1px solid #ccc; }
        
        .grid-row:nth-child(3n) .grid-cell { border-bottom-width: 2px; border-bottom-color: #333; }
        .grid-row:last-child .grid-cell { border-bottom: 1px solid #ccc; }
        
        .grid-cell:nth-child(1) { border-left-width: 2px; border-left-color: #333; }
        .grid-row:first-child .grid-cell { border-top-width: 2px; border-top-color: #333; }

        </style>
        """, unsafe_allow_html=True)
        
        html_grid = "<div class='grid-container'>"
        for r_idx, row in enumerate(grid):
            html_grid += f"<div class='grid-row' style='display: contents;'>"
            for c_idx, cell in enumerate(row):
                cell_display = cell if cell != 0 else "."
                cell_class = "grid-cell zero" if cell == 0 else "grid-cell"
                html_grid += f"<div class='{cell_class}'>{cell_display}</div>"
            html_grid += "</div>"
        html_grid += "</div>"
        
        st.markdown(html_grid, unsafe_allow_html=True)

# --- Main App Logic (Basic Programming) ---

st.set_page_config(page_title="GridCracker", layout="wide")
st.title("GridCracker: The Sudoku Solver")

# Initialize session state (Data Structure)
if 'current_puzzle' not in st.session_state:
    st.session_state.current_puzzle = None
if 'current_solution' not in st.session_state:
    st.session_state.current_solution = None

# Sidebar controls
with st.sidebar:
    st.header("Controls")
    difficulty = st.radio(
        "Select Difficulty",
        ('Easy', 'Medium', 'Hard'),
        index=1  # Default to Medium
    )
    
    if st.button("Generate New Puzzle"):
        st.session_state.current_puzzle = generate_puzzle(difficulty.lower())
        st.session_state.current_solution = None # Clear old solution
        st.success("New puzzle generated!")

# Main content area
col1, col2 = st.columns(2)

# Display Puzzle
puzzle_container = col1.empty()
if st.session_state.current_puzzle:
    display_grid(st.session_state.current_puzzle, "Puzzle", puzzle_container)
else:
    puzzle_container.info("Click 'Generate New Puzzle' in the sidebar to start.")

# Display Solution
solution_container = col2.empty()
if st.session_state.current_puzzle and not st.session_state.current_solution:
    if col1.button("Solve Puzzle"):
        with st.spinner("Cracking the grid..."):
            # Create an instance of our class (OOP)
            solver = SudokuSolver(st.session_state.current_puzzle)
            
            # Call the class method (OOP / Functions)
            solution = solver.get_solution()
            
            if solution:
                st.session_state.current_solution = solution
                st.balloons()
                display_grid(st.session_state.current_solution, "Solution", solution_container)
            else:
                solution_container.error("This puzzle is unsolvable.")

elif st.session_state.current_solution:
    display_grid(st.session_state.current_solution, "Solution", solution_container)