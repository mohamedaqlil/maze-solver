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
    # Get the cell from the grid
    cell = self._cells[i][j]
    
    # Call the draw method without additional parameters
    cell.draw()
    
    # Animate if needed
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
    self._draw_cell(i, j)  # Draw the current cell
    
    # Shuffled directions to add randomness
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    random.shuffle(directions)
    
    for di, dj in directions:
        next_i, next_j = i + di, j + dj
        
        # Check if next cell is within grid and not visited
        if (0 <= next_i < self.num_rows and 
            0 <= next_j < self.num_cols and 
            not self._cells[next_i][next_j].visited):
            
            # Break down walls between current cell and chosen neighbor
            if di == -1:  # Moving up
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif di == 1:  # Moving down
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif dj == -1:  # Moving left
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif dj == 1:  # Moving right
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            
            self._draw_cell(i, j)
            self._draw_cell(next_i, next_j)
            
            # Recursively visit next cell
            self._break_walls_r(next_i, next_j)

  def _reset_cells_visited(self):
    # Iterate through all cells in the maze
    for i in range(self.num_rows):
        for j in range(self.num_cols):
            # Set visited to False for each cell
            self._cells[i][j].visited = False

  def solve(self):
    # Call the recursive solver starting at (0,0)
    return self._solve_r(0, 0)
  
  def _solve_r(self, i, j):
    self._animate()
    self._cells[i][j].visited = True

    if i == self.num_rows - 1 and j == self.num_cols - 1:
      return True
    
    if i > 0 and not self._cells[i][j].has_top_wall and not self._cells[i-1][j].visited:
      self._cells[i][j].draw_move(self._cells[i-1][j])
      if self._solve_r(i-1, j):
        return True
      self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)

    if j < self.num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i][j+1].visited:
      self._cells[i][j].draw_move(self._cells[i][j+1])
      if self._solve_r(i, j+1):
        return True
      self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)

    if i < self.num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i+1][j].visited:
      self._cells[i][j].draw_move(self._cells[i+1][j])
      if self._solve_r(i+1, j):
        return True
      self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)

    if j > 0 and not self._cells[i][j].has_left_wall and not self._cells[i][j-1].visited:
      self._cells[i][j].draw_move(self._cells[i][j-1])
      if self._solve_r(i, j-1):
        return True
      self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)

    return False
