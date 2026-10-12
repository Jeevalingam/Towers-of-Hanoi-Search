
def compatible(container, stack, max_height):
    """
    The stack is stored bottom to top.
    Earlier departures use smaller departure_order values.
    """
    if len(stack) >= max_height:
        return False

    if not stack:
        return True

    top = stack[-1]

    # A heavier container must be below a lighter one.
    if top["weight"] < container["weight"]:
        return False

    # Earlier-departing containers should be nearer the top.
    if top["departure_order"] < container["departure_order"]:
        return False

    # Conservative rule: hazardous containers cannot share a stack.
    if top["hazardous"] or container["hazardous"]:
        return False

    return True


def solve_container_csp(containers, num_stacks=2, max_height=3):
    stacks = [[] for _ in range(num_stacks)]
    nodes = 0

    # Try more constrained / heavier containers first.
    ordered = sorted(
        containers,
        key=lambda c: (-c["weight"], c["departure_order"])
    )

    def backtrack(index):
        nonlocal nodes
        nodes += 1

        if index == len(ordered):
            return True

        container = ordered[index]

        for stack in stacks:
            if compatible(container, stack, max_height):
                stack.append(container)

                # Forward-checking: the next container must have
                # at least one currently feasible stack.
                next_index = index + 1
                if next_index == len(ordered):
                    feasible = True
                else:
                    next_container = ordered[next_index]
                    feasible = any(
                        compatible(next_container, candidate, max_height)
                        for candidate in stacks
                    )

                if feasible and backtrack(index + 1):
                    return True

                stack.pop()

        return False

    success = backtrack(0)

    return {
        "success": success,
        "stacks": [
            [c["id"] for c in stack] for stack in stacks
        ] if success else [],
        "nodes_explored": nodes,
    }


def main():
    containers = [
        {"id": "C1", "weight": 12, "departure_order": 3,
         "hazardous": False},
        {"id": "C2", "weight": 8, "departure_order": 2,
         "hazardous": False},
        {"id": "C3", "weight": 5, "departure_order": 1,
         "hazardous": False},
    ]

    result = solve_container_csp(containers)

    print("CONTAINER-STACKING CSP")
    print("Success:", result["success"])
    print("Assignment:", result["stacks"])
    print("Search nodes:", result["nodes_explored"])


if __name__ == "__main__":
    main()
