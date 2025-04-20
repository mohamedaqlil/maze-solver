from tkinter import Tk, BOTH, Canvas
from window import draw_line

class Cell:
  def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, _x1, _x2, _y1, _y2, _win):
    self.has_left_wall = has_left_wall
    self.has_right_wall = has_right_wall
    self.has_top_wall = has_top_wall
    self.has_bottom_wall = has_bottom_wall
    self._x1 = _x1
    self._x2 = _x2
    self._y1 = _y1
    self._y2 = _y2
    self._win = _win

  def draw(self, fill_color="black"):
    if self.has_left_wall:
      self._win.create_line(
      self._x1, self._y1, self._x1, self._y2, fill=fill_color, width=2
      )

    if self.has_right_wall:
      self._win.create_line(
      self._x2, self._y1, self._x2, self._y2, fill=fill_color, width=2
      )

    if self.has_top_wall:
      self._win.create_line(
      self._x1, self._y1, self._x2, self._y1, fill=fill_color, width=2
      )

    if self.has_bottom_wall:
      self._win.create_line(
      self._x1, self._y2, self._x2, self._y2, fill=fill_color, width=2
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
