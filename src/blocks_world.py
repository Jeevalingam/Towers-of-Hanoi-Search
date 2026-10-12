
from search_engine import breadth_first_search


def initial_state():
    # Each stack is stored from bottom to top.
    # The robot initially holds nothing.
    return ((("A",), ("B",)), None)


def goal_test(state):
    stacks, holding = state

    # Goal: A is on B and the robot is holding nothing.
    on_facts, clear_facts, holding_facts = get_facts(state)

    return (
        ("On", "A", "B") in on_facts
        and holding is None
    )


def get_facts(state):
    stacks, holding = state

    on_facts = set()
    clear_facts = set()
    holding_facts = set()

    for stack in stacks:
        if stack:
            clear_facts.add(("Clear", stack[-1]))

        for i in range(1, len(stack)):
            on_facts.add(("On", stack[i], stack[i - 1]))

        for block in stack:
            if len(stack) > 0 and stack.index(block) == 0:
                on_facts.add(("OnTable", block))

    if holding is not None:
        holding_facts.add(("Holding", holding))

    return on_facts, clear_facts, holding_facts


def get_successors(state):
    stacks, holding = state
    successors = []

    # STRIPS-style action: Pickup(x) or Unstack(x, y)
    # Preconditions: arm empty and x is clear.
    if holding is None:
        for i, stack in enumerate(stacks):
            if not stack:
                continue

            block = stack[-1]
            new_stacks = [list(s) for s in stacks]
            new_stacks[i].pop()

            new_stacks = tuple(
                tuple(s) for s in new_stacks if s
            )

            if len(stack) == 1:
                action = f"Pickup({block})"
            else:
                below = stack[-2]
                action = f"Unstack({block}, {below})"

            next_state = (new_stacks, block)
            successors.append((next_state, action))

    # STRIPS-style action: Putdown(x) or Stack(x, y)
    # Preconditions: robot holds x; destination is clear.
    else:
        block = holding

        # Put the held block on the table.
        new_stacks = stacks + ((block,),)
        successors.append(
            ((new_stacks, None), f"Putdown({block})")
        )

        # Put the held block on top of another stack.
        for i, stack in enumerate(stacks):
            if not stack:
                continue

            support = stack[-1]
            new_stacks = [list(s) for s in stacks]
            new_stacks[i].append(block)

            next_stacks = tuple(
                tuple(s) for s in new_stacks
            )

            successors.append(
                (
                    (next_stacks, None),
                    f"Stack({block}, {support})",
                )
            )

    return successors


def solve_blocks_world():
    return breadth_first_search(
        initial_state(),
        goal_test,
        get_successors,
    )


def main():
    result = solve_blocks_world()

    print("BLOCKS WORLD PLANNER")
    print("Success:", result["success"])

    for i, action in enumerate(result["plan"], start=1):
        print(f"{i}. {action}")

    print("Plan length:", result["plan_length"])
    print("Nodes expanded:", result["nodes_expanded"])


if __name__ == "__main__":
    main()
