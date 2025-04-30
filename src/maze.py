from cell import Cell, Wall
from window import Window
import time
import random

class Maze:
  def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.win = win

  def _create_cells(self):
    cells = []
    for i in range(self.num_rows):
      row =[]
      for j in range(self.num_cols):
        cell = Cell(i, j, self.x1, self.y1, self.cell_size_x, self.cell_size_y, self.win)
        row.append(cell)
      cells.append(row)
    self._cells = cells

  def _draw_cell(self, i, j):
    # Calculate the x, y pixel position of the cell
    x = self.x1 + j * self.cell_size_x
    y = self.y1 + i * self.cell_size_y
    
    # Get the cell object at (i, j) from the grid
    cell = self._cells[i][j]
    
    # Call the draw function for the cell with its calculated position and size
    cell.draw(self.win, x, y, self.cell_size_x, self.cell_size_y)
    
    # Animate the process for visualization
    self._animate()

  def _animate(self):
    self.win.redraw()  # Refresh the display
    time.sleep(0.05)   # Pause for 50 milliseconds
