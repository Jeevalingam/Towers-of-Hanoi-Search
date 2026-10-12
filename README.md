# Tower of Hanoi Search Model — State Space

## 1. Project Overview

The **Tower of Hanoi Search Model** is a Python-based Artificial Intelligence project that demonstrates state-space search, planning, and constraint satisfaction.

The project uses search algorithms to solve the Tower of Hanoi puzzle and the Blocks World problem. It also includes a Container Stacking Constraint Satisfaction Problem (CSP) and a software simulation of robotic-arm actions.

The main objective is to demonstrate how AI can find valid action sequences, satisfy constraints, and explain the resulting plans.

## 2. Objectives

- Model Tower of Hanoi as a state-space search problem.
- Implement Breadth-First Search (BFS) using a reusable search engine.
- Represent Blocks World facts and actions using STRIPS-style planning.
- Solve container-stacking assignments using backtracking and forward checking.
- Simulate planned robotic actions with preliminary validation checks.
- Compare plan lengths and expanded-node counts for different problem configurations.

## 3. Technologies Used

- **Programming language:** Python
- **Editor:** Visual Studio Code
- **Search algorithm:** Breadth-First Search (BFS)
- **Planning approach:** STRIPS-style actions
- **Constraint-solving method:** Backtracking with forward checking
- **Testing framework:** pytest
- **Version control:** Git and GitHub

## 4. Project Modules

### 4.1 Tower of Hanoi

The puzzle consists of three pegs and a set of disks of different sizes.

Rules:
- Move only one disk at a time.
- Only the top disk of a peg can be moved.
- A larger disk cannot be placed on a smaller disk.

The program represents each configuration as a state and searches for a sequence of legal moves from the initial state to the goal state.

### 4.2 Shared Search Engine

The file `search_engine.py` implements a reusable Breadth-First Search algorithm.

BFS explores states level by level and returns a plan containing the actions needed to reach a goal state. It also records the number of expanded nodes.

The same search engine is used by both Tower of Hanoi and Blocks World.

### 4.3 Blocks World Planner

Blocks World represents blocks that can be placed on a table or stacked on one another.

The planner uses STRIPS-style actions:

- `Pickup(x)` — pick up a clear block from the table.
- `Putdown(x)` — place a held block on the table.
- `Unstack(x, y)` — remove block `x` from block `y`.
- `Stack(x, y)` — place block `x` on block `y`.

Each action has preconditions, add effects, and delete effects. The planner searches for an action sequence that satisfies the goal facts.

### 4.4 Container Stacking CSP

The container-stacking module assigns containers to stacks while satisfying the model's constraints.

Constraints include:
- Heavier containers must be below lighter containers.
- Containers with earlier departure orders must be nearer the top.
- Stack height must not exceed the specified limit.
- Hazardous containers must be stored alone under the simplified assumption used in this prototype.

The solver uses backtracking to explore assignments and forward checking to reject choices that leave a remaining container without a feasible stack.

### 4.5 Robotic-Arm Simulation

The robotic-arm module demonstrates planned actions in software.

It displays each action, performs preliminary format checks, and stops when an unsupported action is encountered. It also validates container-stack assignments against the implemented constraints.

**Scope:** This is a software simulation. It does not control a physical robotic arm or certify real-world operational safety.

## 5. Project Structure

```text
Towers-of-Hanoi-Search/
│
├── src/
│   ├── main.py
│   ├── search_engine.py
│   ├── hanoi_search.py
│   ├── blocks_world.py
│   ├── container_csp.py
│   └── robot_simulator.py
│
├── tests/
│   └── test_hanoi.py
│
├── docs/
│   └── Project documentation and results
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## 6. Installation and Setup

### Prerequisites

- Python installed on your computer.
- Visual Studio Code or another Python-compatible editor.
- Git, if you want to clone or manage the repository.

### Step 1: Open the project folder

Open the `Towers-of-Hanoi-Search` folder in Visual Studio Code.

### Step 2: Install dependencies

Open the terminal in the project folder and run:

```powershell
py -m pip install -r requirements.txt
```

### Step 3: Run the main program

```powershell
py src/main.py
```

The program provides a menu to solve Tower of Hanoi, solve Blocks World, run the container-stacking CSP, perform search experiments, or exit.

## 7. Running Individual Modules

Run Tower of Hanoi:

```powershell
py src/hanoi_search.py
```

Run Blocks World:

```powershell
py src/blocks_world.py
```

Run the container-stacking CSP:

```powershell
py src/container_csp.py
```

Run the robotic-arm simulation module:

```powershell
py src/robot_simulator.py
```

The robotic-arm module defines reusable functions and may produce no output when run independently. Its simulation function can be called from the main program or a dedicated test.

## 8. Testing

The project includes pytest tests for the Tower of Hanoi module.

Run the test suite using:

```powershell
py -m pytest -v
```

The tests check:
- Initial and goal states.
- Legal neighboring states.
- Successful solutions for small disk counts.
- Expected optimal plan lengths for one, two, and three disks.
- Handling of an invalid disk count.

The current test suite contains seven Hanoi tests. Additional automated tests can be added for Blocks World, CSP constraints, and simulator validation.

## 9. Results and Performance Evaluation

The project records two important search metrics:

- **Plan length:** Number of actions in the returned solution.
- **Nodes expanded:** Number of states removed from the BFS queue and examined by the search engine.

For Tower of Hanoi, the minimum number of moves for \(n\) disks is:

\[
T(n)=2^n-1
\]

Example results from the current implementation:

| Number of disks | Plan length |
|---:|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 7 |
| 4 | 15 |

The number of expanded nodes depends on the state representation, successor-generation order, and search implementation.

The performance experiment also evaluates several Blocks World configurations. Use the actual output from your program when recording expanded-node counts in your final report.

## 10. Applications

- Understanding state-space search in Artificial Intelligence.
- Automated planning and action sequencing.
- Constraint-based resource allocation.
- Simplified warehouse and container-stacking planning.
- Demonstrating safety checks in simulated robotic workflows.
- Comparing search behavior across different problem configurations.

## 11. Limitations

- BFS can require considerable memory for large state spaces.
- The current automated test suite focuses primarily on Tower of Hanoi.
- Container hazard separation is a simplified model and does not represent complete hazardous-material regulations.
- The robotic-arm module is a software simulation, not a physical robot controller.
- Search performance results depend on the implementation and tested configurations.

## 12. Future Enhancements

- Add automated tests for Blocks World and container-stacking constraints.
- Add a graphical visualization of state transitions.
- Extend the planner to larger problem configurations.
- Add more realistic container compatibility rules.
- Improve simulation checks to validate action preconditions against changing world states.
- Integrate a physical robotic arm only after appropriate hardware, control, and safety validation.

## 13. Conclusion

The Tower of Hanoi Search Model demonstrates how AI search, symbolic planning, and constraint satisfaction can solve different problem types using structured representations.

By combining a reusable BFS engine, STRIPS-style planning, backtracking with forward checking, and a software simulation, the project provides a foundation for understanding intelligent planning and its potential applications in logistics and robotics.

## 14. License

This project is distributed under the MIT License. See the `LICENSE` file for details.