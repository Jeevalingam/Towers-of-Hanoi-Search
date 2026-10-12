
from search_engine import breadth_first_search


def create_initial_state(num_disks):
    if num_disks < 1:
        raise ValueError("Number of disks must be at least 1.")

    return (tuple(range(num_disks, 0, -1)), (), ())


def create_goal_state(num_disks):
    return ((), (), tuple(range(num_disks, 0, -1)))


def get_neighbors(state):
    neighbors = []

    for source in range(3):
        if not state[source]:
            continue

        disk = state[source][-1]

        for destination in range(3):
            if source == destination:
                continue

            if (
                not state[destination]
                or state[destination][-1] > disk
            ):
                new_state = [list(peg) for peg in state]

                new_state[source].pop()
                new_state[destination].append(disk)

                new_state = tuple(
                    tuple(peg) for peg in new_state
                )

                action = (
                    f"Move disk {disk} from "
                    f"{chr(65 + source)} to "
                    f"{chr(65 + destination)}"
                )

                neighbors.append((new_state, action))

    return neighbors


def solve_hanoi(num_disks):
    start = create_initial_state(num_disks)
    goal = create_goal_state(num_disks)

    return breadth_first_search(
        start,
        lambda state: state == goal,
        get_neighbors,
    )


def main():
    result = solve_hanoi(3)

    print("TOWER OF HANOI - STATE SPACE SEARCH")
    print("Algorithm: Breadth-First Search")
    print("Success:", result["success"])

    for i, action in enumerate(result["plan"], start=1):
        print(f"{i}. {action}")

    print("Plan length:", result["plan_length"])
    print("Nodes expanded:", result["nodes_expanded"])


if __name__ == "__main__":
    main()
