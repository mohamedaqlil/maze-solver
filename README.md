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
**Maze Solver** started as a personal exercise to practise object-oriented design and classic computer-science algorithms.  
It builds a *perfect maze* (exactly one path between any two cells) using the **Recursive-Backtracker** algorithm, then finds an exit path with a depth-first search—both fully animated.

---

## Features
- 🔀 Randomised *Recursive Backtracker* maze generator  
- 🧠 DFS solver with coloured path tracing & back-tracking  
- ⚙️ Adjustable grid size, cell size, margins, and animation speed  
- 💾 Zero external dependencies—everything is in the Python standard library  
- 🧹 Clean, well-documented source code ready for hacking or teaching  

---

## Installation
```bash
git clone https://github.com/<mohamedaqlil>/maze-solver.git
cd maze-solver
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # optional – Tkinter is stdlib

Note: On Debian/Ubuntu you might need sudo apt install python3-tk.

⸻

Usage

Run with the default parameters:

python src/main.py

Tweak parameters directly in src/main.py:

if __name__ == "__main__":
    main(
        num_rows = 20,
        num_cols = 30,
        screen_x = 1200,
        screen_y = 800,
        margin   = 40,
        seed     = 42,      # repeatable mazes
    )

Close the window (or hit ) to exit.

⸻

Project Structure

src/
├── cell.py          # Single-cell representation & drawing logic
├── drawing_utils.py # Point & Line helpers
├── maze.py          # Maze generator + solver algorithms
├── window.py        # Thin Tkinter wrapper for drawing & animation
├── main.py          # Entrypoint – adjust parameters here
└── tests.py         # Experiments / unit tests


⸻

Algorithms

Phase	File & Function	Description
Generation	maze._break_walls()	Recursive-Backtracker removes walls until every cell is visited
Solving	maze._solve()	Recursive DFS explores neighbours; backtracks & visually undoes wrong moves

Each step calls window.redraw() so the animation stays fluent at ~20 FPS.

⸻

Demo

![Maze generation & solving demo](demo)


⸻

Contributing

Pull requests are welcome! If you have:
	•	alternative algorithms (Prim, Kruskal, Wilson…)
	•	bug fixes or performance tweaks
	•	ideas for exporting the maze to images/GIFs

open an issue first to discuss ✨.

⸻

License

Distributed under the MIT License.
See the LICENSE file for full details.

⸻

Made with ❤️ by Mohamed Aqlil.

🔗 Connect with me on [LinkedIn](https://www.linkedin.com/in/mohamedaqlil/)  
🐦 Or follow me on [X (Twitter)](https://x.com/aqlil_mohamed)
