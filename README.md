# Tower of Hanoi Search Model

## Problem Statement

Model the Tower of Hanoi puzzle as a state-space search problem and solve it using a search algorithm instead of direct recursion.

## Objective

To represent each Tower of Hanoi configuration as a state and use Breadth-First Search (BFS) to find a sequence of valid moves from the initial state to the goal state.

## State Representation

The puzzle contains three pegs: A, B and C.

A state is represented as:

(Peg A, Peg B, Peg C)

Example:

((3, 2, 1), (), ())

This means all three disks are on Peg A.

The goal state is:

((), (), (3, 2, 1))

This means all disks are moved to Peg C.

## Approach

1. Create the initial state.
2. Generate all legal moves.
3. Each legal move creates a new state.
4. Use Breadth-First Search to explore the states.
5. Store visited states to avoid repetition.
6. Stop when the goal state is reached.
7. Return the sequence of moves.

## How to Run

Open the terminal in VS Code and run:

python src/hanoi_search.py

Enter the number of disks when asked.

Example:

Enter number of disks: 3

## Sample Output

Tower of Hanoi - State Space Search

Number of disks: 3
Search algorithm: Breadth-First Search (BFS)

Move sequence:

1. Move disk 1 from A to C
2. Move disk 2 from A to B
3. Move disk 1 from C to B
4. Move disk 3 from A to C
5. Move disk 1 from B to A
6. Move disk 2 from B to C
7. Move disk 1 from A to C

Total moves: 7

## Testing

Run:

python tests/test_hanoi.py

Expected output:

All tests passed!

## Concepts Demonstrated

- State-space representation
- Breadth-First Search
- State transitions
- Legal move generation
- Visited-state tracking
- Path reconstruction