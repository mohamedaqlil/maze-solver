from window import Window
from drawing_utils import Point, Line
from cell import Cell
from maze import Maze

def main():
    # Adjust these values as needed
    num_rows = 10
    num_cols = 10
    window_width = 800
    window_height = 600
    cell_size_x = window_width // num_cols
    cell_size_y = window_height // num_rows
    
    maze = Maze(num_rows, num_cols, window_width, window_height, cell_size_x, cell_size_y)
    maze._create_cells()
    maze._break_entrance_and_exit()
    maze._win.mainloop()

if __name__ == "__main__":
    main()
