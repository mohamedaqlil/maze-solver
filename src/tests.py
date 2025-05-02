import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
      num_cols = 12
      num_rows = 10
      m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
      self.assertEqual(
          len(m1._cells),
          num_rows,
      )
      self.assertEqual(
          len(m1._cells[0]),
          num_cols,
      )

    def test_maze_different_dimensions(self):
       # Test with different dimensions
       num_cols = 5
       num_rows = 8
       m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
       self.assertEqual(len(m2._cells), num_rows)
       self.assertEqual(len(m2._cells[0]), num_cols)

    def test_maze_minimum_dimensions(self):
       # Test with minimum dimensions
       num_cols = 1
       num_rows = 1
       m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
       self.assertEqual(len(m3._cells), num_rows)
       self.assertEqual(len(m3._cells[0]), num_cols)

    def test_break_entrance_and_exit(self):
       num_cols = 9
       num_rows = 6
       m = Maze(0, 0, num_rows, num_cols, 10, 10)
       # Override _draw_cell with a dummy method for testing
       m._draw_cell = lambda x, y: None
       m._break_entrance_and_exit()
       # Check that the top-left cell has its top wall removed
       self.assertEqual(m._cells[0][0].has_top_wall, False)
       # Check that the bottom-right cell has its bottom wall removed
       self.assertEqual(m._cells[num_rows-1][num_cols-1].has_bottom_wall, False)
    
    def test_reset_cells_visited(self):
       num_cols = 12
       num_rows = 9
       maze = Maze(0, 0, num_rows, num_cols, 10, 10)

       maze._cells[0][0].visited = True
       maze._cells[1][2].visited = True
       maze._cells[3][4].visited = True

       maze._reset_cells_visited()
       # Check that all cells' visited property is now False
       for i in range(num_rows):
          for j in range(num_cols):
             self.assertFalse(maze._cells[i][j].visited)

if __name__ == "__main__":
   unittest.main()