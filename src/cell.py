from tkinter import Tk, BOTH, Canvas
from window import Window

class Cell:
  def __init__(self, i, j, x1, y1, cell_size_x, cell_size_y, win, 
                 has_left_wall=True, has_right_wall=True, 
                 has_top_wall=True, has_bottom_wall=True):
        # Set default wall states
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        # Calculate pixel positions based on i, j, and maze attributes
        self._x1 = x1 + j * cell_size_x
        self._x2 = self._x1 + cell_size_x
        self._y1 = y1 + i * cell_size_y
        self._y2 = self._y1 + cell_size_y

        # Store the window object
        self._win = win

  def draw(self, fill_color="black"):
    if self.has_left_wall:
      self._win.create_line(
      self._x1, self._y1, self._x1, self._y2, fill=fill_color, width=2
      )
    else:
        # Draw a white line where the left wall would be
        self._win.create_line(
            self._x1, self._y1, self._x1, self._y2, fill="white", width=2
        )

    if self.has_right_wall:
      self._win.create_line(
      self._x2, self._y1, self._x2, self._y2, fill=fill_color, width=2
      )
    else:
        # Draw a white line where the right wall would be
        self._win.create_line(
            self._x2, self._y1, self._x2, self._y2, fill="white", width=2
        )

    if self.has_top_wall:
      self._win.create_line(
      self._x1, self._y1, self._x2, self._y1, fill=fill_color, width=2
      )
    else:
        # Draw a white line where the top wall would be
        self._win.create_line(
            self._x1, self._y1, self._x2, self._y1, fill="white", width=2
        )

    if self.has_bottom_wall:
      self._win.create_line(
      self._x1, self._y2, self._x2, self._y2, fill=fill_color, width=2
      )
    else:
       # Draw a white line where the bottom wall would be
       self._win.create_line(
          self._x1, self._y2, self._x2, self._y2, fill="white", width=2
          )

  def draw_move(self, to_cell, undo=False):
    # Calculate center of current cell
    center_x1 = (self._x1 + self._x2) / 2
    center_y1 = (self._y1 + self._y2) / 2
    
    # Calculate center of destination cell
    center_x2 = (to_cell._x1 + to_cell._x2) / 2
    center_y2 = (to_cell._y1 + to_cell._y2) / 2
    
    # Choose color based on undo parameter
    line_color = "gray" if undo else "red"

    # Draw the line between the two center points
    self._win.create_line(
        center_x1, center_y1, center_x2, center_y2, 
        fill=line_color, width=2
    )
