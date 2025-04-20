from tkinter import Tk, BOTH, Canvas
from drawing_utils import Line

class Window:
  def __init__(self, width, height):
    self.__root = Tk()
    self.__root.geometry(f"{width}x{height}")
    self.__root.title("Maze Solver")
    self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
    self.__canvas.pack(fill="both", expand=True)
    self.__running = False
    self.__root.protocol("WM_DELETE_WINDOW", self.close)

  
  def redraw(self):
    self.__root.update_idletasks()  # Handle layout and idle updates
    self.__root.update()  # Redraw the entire window with any changes

  def draw_line(self, line, fill_color):
    # Call the line's draw method with our canvas
    line.draw(self.__canvas, fill_color)

  def wait_for_close(self):
    self.__running = True
    while self.__running:  # While the window is running
      self.redraw()  # Refresh the window
    print("window closed...")

  def close(self):
    self.__running = False

  def create_line(self, *args, **kwargs):
    return self.__canvas.create_line(*args, **kwargs)
