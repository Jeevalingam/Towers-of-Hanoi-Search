
def simulate_plan(actions):
    print("\nROBOTIC EXECUTION SIMULATION")

    for step, action in enumerate(actions, start=1):
        # This demo accepts only non-empty action descriptions.
        if not isinstance(action, str) or not action.strip():
            print(f"Step {step}: Invalid action. STOP.")
            return False

        print(f"\nStep: {step}")
        print("Action:", action)
        print("Pre-execution check: Passed")
        print("Reason: The planner selected this action as a legal transition.")
        print("Status: Simulated successfully")

    print("\nSimulation completed.")
    return True


def validate_container_assignment(containers, stacks, max_height):
    """
    Recheck an assignment before simulated execution.
    Stack lists are ordered bottom to top.
    """
    by_id = {c["id"]: c for c in containers}
    seen = []

    for stack in stacks:
        if len(stack) > max_height:
            return False, "Maximum stack height exceeded."

        items = [by_id[item] for item in stack]

        for item in items:
            if item["id"] in seen:
                return False, "A container appears more than once."
            seen.append(item["id"])

        for lower, upper in zip(items, items[1:]):
            if lower["weight"] < upper["weight"]:
                return False, "Weight ordering is invalid."

            if lower["departure_order"] < upper["departure_order"]:
                return False, "Departure ordering is invalid."

        hazardous = sum(1 for item in items if item["hazardous"])
        if hazardous > 0 and len(items) > 1:
            return False, "Hazardous container separation failed."

    if len(seen) != len(containers):
        return False, "Some containers are missing."

    return True, "All defined checks passed."
