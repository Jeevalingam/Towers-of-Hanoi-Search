
import sys
from pathlib import Path

# Add the project's src folder to Python's import path.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_FOLDER = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_FOLDER))

from hanoi_search import (
    create_initial_state,
    create_goal_state,
    get_neighbors,
    solve_hanoi,
)


def test_initial_state():
    assert create_initial_state(3) == ((3, 2, 1), (), ())


def test_goal_state():
    assert create_goal_state(3) == ((), (), (3, 2, 1))


def test_neighbors():
    state = ((2, 1), (), ())
    neighbors = get_neighbors(state)
    assert len(neighbors) == 2


def test_one_disk():
    result = solve_hanoi(1)
    assert result["success"] is True
    assert result["plan_length"] == 1


def test_two_disks():
    result = solve_hanoi(2)
    assert result["success"] is True
    assert result["plan_length"] == 3


def test_three_disks():
    result = solve_hanoi(3)
    assert result["success"] is True
    assert result["plan_length"] == 7


def test_invalid_disk_count():
    try:
        create_initial_state(0)
    except ValueError:
        return

    assert False, "Expected ValueError for zero disks"
