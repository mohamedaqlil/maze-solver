from window import Window
from drawing_utils import Point, Line

def main():
    # Create a window
    window = Window(800, 600)  # width=800, height=600
    
    # Create some point objects
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    p4 = Point(400, 300)
    
    # Create line objects using those points
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    
    # Draw the lines with different colors
    window.draw_line(line1, "red")
    window.draw_line(line2, "blue")
    window.draw_line(line3, "green")
    
    # Wait for the window to close
    window.wait_for_close()

if __name__ == "__main__":
    main()
