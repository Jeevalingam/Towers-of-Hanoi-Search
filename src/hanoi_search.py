def create_initial_state(num_disks):
    """Create the initial Tower of Hanoi state."""
    return (tuple(range(num_disks, 0, -1)), (), ())


def create_goal_state(num_disks):
    """Create the goal Tower of Hanoi state."""
    return ((), (), tuple(range(num_disks, 0, -1)))


def main():
    num_disks = 3

    initial_state = create_initial_state(num_disks)
    goal_state = create_goal_state(num_disks)

    print("Tower of Hanoi Search Model")
    print("---------------------------")
    print("Number of disks:", num_disks)
    print("Initial state:", initial_state)
    print("Goal state:", goal_state)


if __name__ == "__main__":
    main()