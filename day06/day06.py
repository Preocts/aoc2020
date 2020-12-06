"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day06

Keeping it simple.  Game. Set. Match.
"""
import sys


def main(input_file: str) -> None:

    in_list = f"{input_file}\n".split("\n")
    answers = []
    groups = []
    small_set = set()
    count = 0
    for line in in_list:
        for char in line:
            small_set.add(char)
        if not line:
            answers.append(small_set)
            groups.append(count)
            small_set = set()
            count = 0
            continue
        count += 1

    total_yes = sum([len(i) for i in answers])

    print(f"Sum of yes counts: {total_yes}")

    counts = []
    newgroup = True
    for line in in_list:
        if newgroup:
            small_set = {c for c in line}
            newgroup = False
            continue
        if not line:
            counts.append(len(small_set))
            small_set = set()
            newgroup = True
            continue

        small_set = small_set.intersection({c for c in line})

    print(f"Sum of unanimous yes counts: {sum(counts)}")

    return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Useage: python day06.py [filename]")
        exit()

    try:
        with open(sys.argv[1], "r") as f:
            input_file = f.read()
    except Exception as err:
        print("I can't do that, Dave.")
        print(f">>> {err}")
        exit()

    main(input_file)
    exit()
