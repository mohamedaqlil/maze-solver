# 🧩 Maze Solver

A lightweight **Python/Tkinter** project that *generates* a perfect maze, then *solves* it while you watch the animation in real-time.  
Great for learning depth-first search, recursion, and a dash of GUI programming.

---

## Table of Contents
1. [About](#about)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Algorithms](#algorithms)
7. [Demo](#demo)
8. [Contributing](#contributing)
9. [License](#license)

---

## About

**Maze Solver** is a visualization tool for generating and solving mazes using classic recursive algorithms.  
It focuses on simplicity, animation, and readability, built with Python and Tkinter only.

---

## Features

- 🔀 Random maze generation using Recursive Backtracker  
- 🧠 Maze solving with animated depth-first search (DFS)  
- 🎨 Real-time cell drawing and backtracking  
- 🧰 Built entirely with Python standard library  
- 🧪 Educational and clean OOP design  

---

## Installation

```bash
git clone https://github.com/mohamedaqlil/maze-solver.git
cd maze-solver
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # optional – Tkinter is stdlib
```

> 💡 **Note:** On Linux you may need `sudo apt install python3-tk`.

---

## Usage

Start the maze application:

```bash
python src/main.py
```

You can modify the behavior in `main.py`:

```python
main(
    num_rows = 20,
    num_cols = 30,
    screen_x = 1200,
    screen_y = 800,
    margin   = 40,
    seed     = 42,
)
```

Hit **Escape** or close the window to stop the program.

---

## Project Structure

```
src/
├── main.py          # Entry point and parameter configuration
├── maze.py          # Maze grid, generation and solving logic
├── cell.py          # Cell class (walls, drawing, movement)
├── window.py        # Tkinter window wrapper for drawing
├── drawing_utils.py # Utility classes for points and lines
└── tests.py         # Optional experiments and debug
```

---

## Algorithms

### 🔧 Maze Generation — Recursive Backtracker

1. Pick a starting cell, mark it as visited.  
2. While there are unvisited neighbors:
   - Randomly choose one.
   - Remove the wall between current and neighbor.
   - Recursively visit the neighbor.

```python
maze._break_walls()  # Depth-first maze generation
```

### 🧭 Maze Solving — Recursive DFS

1. Start at the entrance.  
2. Visit neighbors in order, mark path as visited.  
3. If a dead-end is hit, backtrack and try another route.

```python
maze._solve()  # Recursive DFS search with drawing
```

The solving animation draws red for path and gray for backtracking.

---

## Demo

```markdown
![Maze generation and solving demo](demo)
```

---

## Contributing

Have ideas or improvements? PRs are welcome!

- Add more generation algorithms (e.g. Prim’s, Kruskal’s)  
- Improve animation controls  
- Add exporting options (image/GIF)  
- Bug fixes, code cleanup, etc.  

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Made with ❤️ by [Mohamed Aqlil](https://github.com/mohamedaqlil)

🔗 Connect with me on [LinkedIn](https://www.linkedin.com/in/mohamedaqlil/)  
🐦 Or follow me on [X (Twitter)](https://x.com/aqlil_mohamed)
