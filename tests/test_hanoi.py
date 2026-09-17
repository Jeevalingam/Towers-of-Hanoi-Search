import sys

sys.path.append("src")

from hanoi_search import bfs_hanoi, get_neighbors


def test_one_disk():
    solution = bfs_hanoi(1)
    assert len(solution) == 1


def test_two_disks():
    solution = bfs_hanoi(2)
    assert len(solution) == 3


def test_three_disks():
    solution = bfs_hanoi(3)
    assert len(solution) == 7


def test_neighbors():
    state = ((2, 1), (), ())

    neighbors = get_neighbors(state)

    assert len(neighbors) == 2


print("All tests passed!")