
from hanoi_search import solve_hanoi
from blocks_world import solve_blocks_world
from container_csp import solve_container_csp
from robot_simulator import simulate_plan, validate_container_assignment


def show_hanoi():
    try:
        disks = int(input("Enter number of disks (1-8): "))
        if not 1 <= disks <= 8:
            print("Please enter a number from 1 to 8.")
            return

        result = solve_hanoi(disks)
        print("\nSuccess:", result["success"])

        for i, action in enumerate(result["plan"], start=1):
            print(f"{i}. {action}")

        print("Plan length:", result["plan_length"])
        print("Nodes expanded:", result["nodes_expanded"])
        simulate_plan(result["plan"])

    except ValueError:
        print("Please enter a valid integer.")


def show_blocks_world():
    result = solve_blocks_world()

    print("\nBlocks World")
    print("Success:", result["success"])

    for i, action in enumerate(result["plan"], start=1):
        print(f"{i}. {action}")

    print("Plan length:", result["plan_length"])
    print("Nodes expanded:", result["nodes_expanded"])

    if result["success"]:
        simulate_plan(result["plan"])


def show_container_csp():
    containers = [
        {"id": "C1", "weight": 12, "departure_order": 3,
         "hazardous": False},
        {"id": "C2", "weight": 8, "departure_order": 2,
         "hazardous": False},
        {"id": "C3", "weight": 5, "departure_order": 1,
         "hazardous": False},
    ]

    max_height = 3
    result = solve_container_csp(containers, 2, max_height)

    print("\nContainer CSP")
    print("Success:", result["success"])
    print("Assignment:", result["stacks"])
    print("Search nodes:", result["nodes_explored"])

    if result["success"]:
        valid, message = validate_container_assignment(
            containers, result["stacks"], max_height
        )
        print("Safety validation:", message)

        if valid:
            simulate_plan([
                f"Place container {container_id}"
                for stack in result["stacks"]
                for container_id in stack
            ])


def show_benchmarks():
    print("\nHANOI PERFORMANCE")
    print("Disks | Plan length | Nodes expanded")

    for disks in (2, 3, 4):
        result = solve_hanoi(disks)
        print(
            f"{disks:5} | "
            f"{result['plan_length']:11} | "
            f"{result['nodes_expanded']}"
        )

    print("\nBlocks World currently has a single small example.")
    print("Add two more defined initial/goal cases for a full comparison.")


def main():
    while True:
        print("\n==============================")
        print("ROBOTIC CONTAINER-STACKING PLANNER")
        print("==============================")
        print("1. Solve Tower of Hanoi")
        print("2. Solve Blocks World")
        print("3. Run Container-Stacking CSP")
        print("4. Run Hanoi performance experiments")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_hanoi()
        elif choice == "2":
            show_blocks_world()
        elif choice == "3":
            show_container_csp()
        elif choice == "4":
            show_benchmarks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select 1 to 5.")


if __name__ == "__main__":
    main()
