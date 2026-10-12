
from collections import deque


def breadth_first_search(start_state, goal_test, get_successors):
    """
    Generic BFS planner.

    start_state: initial configuration
    goal_test: function that checks the goal
    get_successors: function returning (next_state, action) pairs
    """

    queue = deque([(start_state, [])])
    visited = {start_state}
    nodes_expanded = 0

    while queue:
        current_state, path = queue.popleft()
        nodes_expanded += 1

        if goal_test(current_state):
            return {
                "success": True,
                "plan": path,
                "plan_length": len(path),
                "nodes_expanded": nodes_expanded,
            }

        for next_state, action in get_successors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))

    return {
        "success": False,
        "plan": [],
        "plan_length": 0,
        "nodes_expanded": nodes_expanded,
    }
