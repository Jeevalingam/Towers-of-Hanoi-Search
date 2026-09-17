from collections import deque


def create_initial_state(num_disks):
    """Create the initial Tower of Hanoi state."""
    return (tuple(range(num_disks, 0, -1)), (), ())


def create_goal_state(num_disks):
    """Create the goal Tower of Hanoi state."""
    return ((), (), tuple(range(num_disks, 0, -1)))


def get_neighbors(state):
    """Generate all legal next states."""

    neighbors = []

    for source in range(3):

        if not state[source]:
            continue

        disk = state[source][-1]

        for destination in range(3):

            if source == destination:
                continue

            if not state[destination] or state[destination][-1] > disk:

                new_state = [list(peg) for peg in state]

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
    """Solve Tower of Hanoi using Breadth-First Search."""

    start = create_initial_state(num_disks)
    goal = create_goal_state(num_disks)

    queue = deque([(start, [])])

    visited = {start}

    while queue:

        current_state, path = queue.popleft()

        if current_state == goal:
            return path

        for next_state, move in get_neighbors(current_state):

            if next_state not in visited:

                visited.add(next_state)

                new_path = path + [move]

                queue.append((next_state, new_path))

    return []


def main():

    num_disks = 3

    solution = bfs_hanoi(num_disks)

    print("Tower of Hanoi - State Space Search")
    print("-----------------------------------")
    print("Number of disks:", num_disks)
    print("Search algorithm: Breadth-First Search (BFS)")

    print("\nMove sequence:")

    for number, move in enumerate(solution, start=1):
        print(f"{number}. {move}")

    print("\nTotal moves:", len(solution))


if __name__ == "__main__":
    main()