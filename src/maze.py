from cell import Cell
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
        win=None,
        seed=None
    ):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.win = win
    self._create_cells()
    self.seed = seed
    if self.seed is not None:
      random.seed(seed)

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

  def _break_entrance_and_exit(self):
    # Break the top wall of the top-left cell (entrance)
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0, 0)
    
    # Break the bottom wall of the bottom-right cell (exit)
    self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
    self._draw_cell(self.num_rows-1, self.num_cols-1)

  def _break_walls_r(self, i, j):
    # Mark current cell as visited
    self._cells[i][j].visited = True

    while(1):
       directions = []

       # Check up (i, j-1)
       if j > 0 and not self._cells[i][j-1].visited:
         directions.append((i, j-1))

       # Check Down (i, j+1)
       if j < self._height - 1 and not self._cells[i][j+1].visited:
         directions.append((i, j+1))

       # Check Left (i-1, j)
       if i > 0 and not self._cells[i-1][j].visited:
         directions.append((i-1, j))

       # Check Right (i+1, j)
       if i < self._width - 1 and not self._cells[i+1][j].visited:
         directions.append((i+1, j))

       if len(directions) == 0:
         return
       
       # Choose a random direction
       random_index = random.randrange(len(directions))
       next_i, next_j = directions[random_index]

       # Break down the walls between the current cell and the chosen cell
       # This depends on which direction we're moving
       if next_i < i:  # Moving left
        self._cells[i][j].left_wall = False
       elif next_i > i:  # Moving right
         self._cells[next_i][next_j].left_wall = False
       elif next_j < j:  # Moving up
         self._cells[i][j].top_wall = False
       elif next_j > j:  # Moving down
         self._cells[next_i][next_j].top_wall = False

       # Recursively call with the new position
       self._break_walls_r(next_i, next_j)

  def _reset_cells_visited(self):
    # Iterate through all cells in the maze
    for i in range(self.num_rows):
        for j in range(self.num_cols):
            # Set visited to False for each cell
            self._cells[i][j].visited = False
