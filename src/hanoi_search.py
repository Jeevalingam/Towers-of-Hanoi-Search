def create_initial_state(num_disks):
    """Create the initial Tower of Hanoi state."""
    return (tuple(range(num_disks, 0, -1)), (), ())


def create_goal_state(num_disks):
    """Create the goal Tower of Hanoi state."""
    return ((), (), tuple(range(num_disks, 0, -1)))


def get_neighbors(state):
    """
    Generate all legal states that can be reached
    from the current state using one move.
    """

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


def display_state(state):
    print("Peg A:", state[0])
    print("Peg B:", state[1])
    print("Peg C:", state[2])


def main():
    num_disks = 3

    initial_state = create_initial_state(num_disks)

    print("Tower of Hanoi State Transitions")
    print("--------------------------------")

    print("\nInitial state:")
    display_state(initial_state)

    print("\nPossible next states:")

    neighbors = get_neighbors(initial_state)

    for number, (state, move) in enumerate(neighbors, start=1):
        print(f"\n{number}. {move}")
        display_state(state)


if __name__ == "__main__":
    main()