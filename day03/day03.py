"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day 2
"""
import sys
import time
from typing import Callable


def sled_movement(slope_pattern: str, x_move: int, y_move: int) -> Callable:
    """
    Args:
        slope_pattern: Input from puzzle
        y_move: Number of steps left (+) or right (-)
        x_move: Number of steps down (+) or up (-)
    """
    slope = slope_pattern.split("\n")
    row_move = x_move
    col_move = y_move
    position = [0, 0]

    def tree_check() -> str:
        """
        Returns:
            "tree": Tree
            "ground: No tree
            "end: End of Map
        """
        nonlocal slope
        nonlocal row_move
        nonlocal col_move
        nonlocal position

        # Move the sled
        position[0] += row_move
        position[1] += col_move

        # Adjust for the wrap
        if position[0] >= len(slope[0]):
            position[0] = position[0] - len(slope[0])

        # Check for end of slope
        if position[1] >= len(slope):
            position[0] -= row_move
            position[1] -= col_move
            return "end"

        if slope[position[1]][position[0]] in "#":
            return "tree"
        return "ground"

    return tree_check


def load_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def main01(filename: str) -> None:
    slope = load_file(filename)
    map_point = "ground"
    shredding_sled = sled_movement(slope, 3, 1)
    tree_count = 0
    while map_point not in "end":
        map_point = shredding_sled()
        if map_point in "tree":
            tree_count += 1

    print(f"You hit {tree_count} trees, George would be proud.")
    return None


def main02(filename: str) -> None:
    movement_set = (
        (
            1,
            1,
        ),
        (
            3,
            1,
        ),
        (
            5,
            1,
        ),
        (
            7,
            1,
        ),
        (
            1,
            2,
        ),
    )
    slope = load_file(filename)
    tree_totals = []
    for x, y in movement_set:
        map_point = "ground"
        shredding_sled = sled_movement(slope, x, y)
        tree_count = 0
        while map_point not in "end":
            map_point = shredding_sled()
            if map_point in "tree":
                tree_count += 1
        tree_totals.append(tree_count)

    final_answer = 0
    for i, total in enumerate(tree_totals):
        print(
            f"Run {i + 1} - Movement {movement_set[i]}, You hit "
            f"{total} trees, George would be proud."
        )
        final_answer = final_answer * total if final_answer else total

    print(f"Final answer is: {final_answer}")
    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Advent of Code Challange, Day 03\n"
            "python day03.py [run]\n"
            "Valid options for run:\n"
            "test01, main01, test02, main02"
        )
        exit()

    if sys.argv[1] in "test01":
        main01("test_inputfile")
    if sys.argv[1] in "main01":
        main01("inputfile")
    if sys.argv[1] in "test02":
        main02("test_inputfile")
    if sys.argv[1] in "main02":
        main02("inputfile")

    if sys.argv[1] in "measure":
        toc_list = []
        for i in range(0, 10_000):
            tic = time.perf_counter_ns()
            main02("inputfile")
            toc_list.append(time.perf_counter_ns() - tic)
        toc_list.sort()
        print(f"Min run-time: {toc_list[0] / 1_000_000} ms")
        print(f"Max run-time: {toc_list[-1] / 1_000_000} ms")
        sum_all = 0
        for toc in toc_list:
            sum_all += toc
        average = (sum_all / len(toc_list)) / 1_000_000
        print(f"Average run-time: {average} ms")
