"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day13
"""
import sys


def depart_time(my_time: int, increment: int) -> int:
    depart_time = increment
    depart_time = depart_time * (my_time // depart_time)
    while depart_time <= my_time:
        depart_time += increment
    return depart_time


def main(input_file) -> None:
    my_time = int(input_file[0])
    bus_list = input_file[1].replace("x,", "").split(",")
    depart_times = []
    for increment in bus_list:
        depart_times.append(depart_time(my_time, int(increment)))
    sort_list = sorted(depart_times)
    index = depart_times.index(sort_list[0])
    diff = sort_list[0] - my_time
    print(f"Answer 1: {int(bus_list[index]) * diff}")

    return None


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Useage: python day13.py [filename]")
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
