"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day12
"""
import sys

from part1 import GarvyTug
from part2 import GhostShip


def main(input_file) -> None:
    my_tug_boat = GarvyTug()
    for line in input_file:
        my_tug_boat.apply_command(line)

    print(f"Current North/South Location: {my_tug_boat.y_units}")
    print(f"Current East/West Location: {my_tug_boat.x_units}")
    print(f"Answer one: {my_tug_boat.manhattan_distance()}")

    the_love_boat = GhostShip()
    for line in input_file:
        the_love_boat.apply_command(line)

    print(f"Current North/South Location: {the_love_boat.ship_y_units}")
    print(f"Current East/West Location: {the_love_boat.ship_x_units}")
    print(f"Answer two: {the_love_boat.manhattan_distance()}")

    return None


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Useage: python day12.py [filename]")
        exit()

    try:
        with open(sys.argv[1], "r") as f:
            input_file = f.read().split("\n")
    except Exception as err:
        print("I can't do that, Dave.")
        print(f">>> {err}")
        exit()
    main(tuple(input_file))

    exit()
