def create_initial_state(num_disks):
    """Create the initial Tower of Hanoi state."""
    return (tuple(range(num_disks, 0, -1)), (), ())


def create_goal_state(num_disks):
    """Create the goal Tower of Hanoi state."""
    return ((), (), tuple(range(num_disks, 0, -1)))


def is_goal_state(state, num_disks):
    """Check whether the current state is the goal state."""
    return state == create_goal_state(num_disks)


def display_state(state):
    """Display the three pegs."""
    print("Peg A:", state[0])
    print("Peg B:", state[1])
    print("Peg C:", state[2])


def main():
    num_disks = 3

    initial_state = create_initial_state(num_disks)

    print("Tower of Hanoi State Representation")
    print("-----------------------------------")

    print("\nInitial State:")
    display_state(initial_state)

    print("\nIs goal state?", is_goal_state(initial_state, num_disks))


if __name__ == "__main__":
    main()