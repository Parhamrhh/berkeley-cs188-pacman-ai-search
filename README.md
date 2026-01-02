# Pacman Search Project

This repository contains the implementation of various search algorithms for the Pacman AI projects, specifically focusing on `search.py` and `searchAgents.py`. The project demonstrates the use of uninformed and informed search strategies to solve different navigation tasks in Pacman mazes.

---

## Overview

The goal of this project is to automate Pacman's movement through different mazes by generating a sequence of actions (`North`, `South`, `East`, `West`) that guides Pacman from the starting position to a defined goal. The project implements graph search algorithms including:

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- Greedy Search
- A* Search with heuristics

Additionally, the project extends `searchAgents.py` to support more complex problem definitions such as corners visiting and food collection.

---

## Problem Definition

The project defines search problems as subclasses of a general `SearchProblem` class. Each problem specifies:

- `getStartState()`: Returns the initial state of Pacman.
- `isGoalState(state)`: Determines if the current state is a goal.
- `expand(state)`: Returns all successor states from the current state, along with the action and step cost as `(next_state, action, step_cost)`.
- Helper methods (`getActions`, `getNextState`, `getActionCost`) to support the search algorithms.

This abstraction allows algorithms to be implemented independently of the maze structure or problem type.

---

## Implemented Search Algorithms

### Depth-First Search (DFS)
- Explores the deepest nodes first using a stack.
- Low memory usage.
- Does not guarantee optimal paths.
- Suitable for small mazes or when reaching a goal is more important than path optimality.

### Breadth-First Search (BFS)
- Explores shallowest nodes first using a queue.
- Guarantees shortest-path solution if all actions have uniform cost.
- High memory usage due to storing all nodes at the current level.
- Suitable for finding minimum-step paths in small to medium uniform-cost mazes.

### Uniform Cost Search (UCS)
- Expands nodes based on the least cumulative cost using a priority queue.
- Guarantees optimal paths even with variable movement costs.
- Higher memory usage than BFS due to priority queue.
- Suitable for environments with differing path costs.

### Greedy Search
- Chooses the node closest to the goal according to a heuristic function.
- Very fast and memory-efficient.
- Does not guarantee optimal paths; may follow misleading paths.
- Suitable for large mazes where reaching the goal quickly is more important than optimality.

### A* Search
- Combines cumulative cost (`g(n)`) and heuristic estimate (`h(n)`).
- Guarantees optimal paths if the heuristic is admissible and consistent.
- More memory-efficient than UCS but still requires exploration of multiple paths.
- Ideal for complex problems, such as visiting all corners or collecting all food pellets.
- Implemented heuristics include:
  - `cornersHeuristic`
  - `foodHeuristic`  

---

## Key Extensions in `searchAgents.py`

### CornersProblem
- Custom search problem for visiting all four corners.
- Methods implemented:
  - `__init__()`
  - `getStartState()`
  - `isGoalState(state)`
  - `expand(state)`
  - `getNextState(state, action)`
- Uses `cornersHeuristic` to improve A* performance.

### FoodSearchProblem
- Custom search problem for collecting all food pellets.
- Heuristic implemented: `foodHeuristic` (returns max maze distance to remaining food).

### ClosestDotSearchAgent
- Finds a path to the closest food dot iteratively.
- Method implemented:
  - `findPathToClosestDot(gameState)` uses BFS to navigate to the nearest food.

### AnyFoodSearchProblem
- Defines a goal as reaching any remaining food dot.
- Method implemented:
  - `isGoalState(state)`

---

## Usage

Run the search algorithms in different mazes using the Pacman command-line interface:

```bash
# Run BFS on tinyMaze
python3 pacman.py -l tinyMaze -p SearchAgent -a fn=bfs,prob=PositionSearchProblem

# Run A* with corners heuristic
python3 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

# Run ClosestDotSearchAgent
python3 pacman.py -l trickySearch -p ClosestDotSearchAgent

```

The project includes an autograder to automatically evaluate your implementations:
```
bash
python3 autograder.py
```

- autograder.py tests your search.py and searchAgents.py implementations against predefined test cases.
- Provides detailed feedback on correctness, edge cases, and common mistakes.
- Supports options such as:
  - `--print-tests` to display test case details.
  - `--generate-solutions` to create reference solution files.
  - `--question` to grade a specific problem.
  - `--no-graphics` to run tests without visual output.

The autograder helps ensure that your algorithms behave as expected in multiple maze scenarios, covering DFS, BFS, UCS, Greedy, and A* with different heuristics.

---

## Results and Evaluation

- DFS: Low memory usage, fast in small mazes, but paths may be suboptimal.
- BFS: Guarantees shortest paths for uniform-cost moves; higher memory usage.
- UCS: Guarantees optimal paths even with variable movement costs.
- Greedy: Very fast and memory-efficient, but may take non-optimal paths.
- A*: Balances speed and optimality using heuristics; best choice for complex mazes.
