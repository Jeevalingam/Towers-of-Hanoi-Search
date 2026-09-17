from collections import deque


def get_neighbors(state):
    """
    Generate all valid states that can be reached
    by making one legal Tower of Hanoi move.
    """

    neighbors = []

    # Three pegs: A, B and C
    for source in range(3):
        # Cannot move from an empty peg
        if not state[source]:
            continue

        # Top disk is the last element
        disk = state[source][-1]

        for destination in range(3):
            if source == destination:
                continue

            # Destination is empty or its top disk is larger
            if not state[destination] or state[destination][-1] > disk:

                new_state = [list(peg) for peg in state]

                # Move disk
                new_state[source].pop()
                new_state[destination].append(disk)

                new_state = tuple(tuple(peg) for peg in new_state)

                move = (
                    f"Move disk {disk} "
                    f"from {chr(65 + source)} "
                    f"to {chr(65 + destination)}"
                )

                neighbors.append((new_state, move))

    return neighbors


def bfs_hanoi(num_disks):
    """
    Solve Tower of Hanoi using Breadth-First Search.
    """

    # Initial state:
    # All disks are on peg A
    start = (tuple(range(num_disks, 0, -1)), (), ())

    # Goal state:
    # All disks must be on peg C
    goal = ((), (), tuple(range(num_disks, 0, -1)))

    queue = deque([(start, [])])

    visited = {start}

    while queue:
        current_state, path = queue.popleft()

        # Goal reached
        if current_state == goal:
            return path

        # Explore possible next states
        for next_state, move in get_neighbors(current_state):

            if next_state not in visited:
                visited.add(next_state)

                new_path = path + [move]

                queue.append((next_state, new_path))

    return []


def print_solution(num_disks, solution):
    """Display the solution."""

    print("\nTower of Hanoi - State Space Search")
    print("-----------------------------------")
    print(f"Number of disks: {num_disks}")
    print("Search algorithm: Breadth-First Search (BFS)")

    print("\nMove sequence:")

    for number, move in enumerate(solution, start=1):
        print(f"{number}. {move}")

    print(f"\nTotal moves: {len(solution)}")


def main():
    try:
        num_disks = int(input("Enter number of disks: "))

        if num_disks <= 0:
            print("Please enter a positive number.")
            return

        if num_disks > 8:
            print("Please enter 8 or fewer disks for faster BFS execution.")
            return

        solution = bfs_hanoi(num_disks)

        if solution:
            print_solution(num_disks, solution)
        else:
            print("No solution found.")

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()