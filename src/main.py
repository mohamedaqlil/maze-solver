from window import Window
from drawing_utils import Point, Line
from cell import Cell

def main():
    # Create a window
    window = Window(800, 600)  # width=800, height=600
    
    # Create some cells with different wall configurations
    # Parameters: left_wall, right_wall, top_wall, bottom_wall, x1, x2, y1, y2, win
    
    # Cell with all walls
    cell1 = Cell(True, True, True, True, 50, 150, 50, 150, window)
    
    # Cell with no left wall
    cell2 = Cell(False, True, True, True, 200, 300, 50, 150, window)
    
    # Cell with no top wall
    cell3 = Cell(True, True, False, True, 50, 150, 200, 300, window)
    
    # Cell with only right wall
    cell4 = Cell(False, True, False, False, 200, 300, 200, 300, window)
    
    # Draw all cells
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    
    # Wait for the window to close
    window.wait_for_close()

if __name__ == "__main__":
    main()
