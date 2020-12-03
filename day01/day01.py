"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day 1 part 1
"""


def get_input(filename: str) -> tuple:
    final_output = []
    with open(filename, "r") as f:
        input_file = f.read()
    for line in input_file.split("\n"):
        final_output.append(int(line))
    return tuple(final_output)


def main_a() -> None:
    accounting = get_input("inputfile")
    # accounting = [1721, 979, 366, 299, 675, 1456]
    for i in accounting:
        for j in accounting:
            if i + j == 2020:
                print(f"{i} * {j} = {i * j}")


def main_b() -> None:
    accounting = get_input("inputfile")
    # accounting = [1721, 979, 366, 299, 675, 1456]
    for i in accounting:
        for j in accounting:
            for k in accounting:
                if i + j + k == 2020:
                    print(f"{i} * {j} * {k}= {i * j * k}")


if __name__ == "__main__":
    main_a()
    main_b()
