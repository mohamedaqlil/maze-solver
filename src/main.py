from window import Window
from drawing_utils import Point, Line
from cell import Cell
from maze import Maze
import sys


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("maze created")

    # Generate the maze
    maze._break_walls_r(0, 0)  # Start breaking walls from top-left
    maze._break_entrance_and_exit()  # Create entrance and exit
    maze._reset_cells_visited()  # Reset visited flags
    
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()


main()
