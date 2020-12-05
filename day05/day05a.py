"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day05
"""
import sys


class BoardingPass(object):
    """ Boarding Pass object

    The first 7 characters will either be F or B; these specify exactly
    one of the 128 rows on the plane (numbered 0 through 127). Each letter
    tells you which half of a region the given seat is in. Start with the
    whole list of rows; the first letter indicates whether the seat is in
    the front (0 through 63) or the back (64 through 127). The next letter
    indicates which half of that region the seat is in, and so on until
    you're left with exactly one row.

    The last three characters will be either L or R; these specify exactly
    one of the 8 columns of seats on the plane (numbered 0 through 7). The
    same process as above proceeds again, this time with only three steps.
    L means to keep the lower half, while R means to keep the upper half.

    Attributes:
        boarding_pass: [str] 10 character binary code for seat location
    """

    def __init__(self) -> None:
        self.__boarding_pass = ""
        return None

    def __str__(self) -> str:
        return self.__boarding_pass

    def __bool__(self) -> bool:
        return True if self.__boarding_pass else False

    def set_boarding_pass(self, boarding_pass: str) -> bool:
        if not self.pass_validate(boarding_pass):
            self.__boarding_pass = ""
            return False
        self.__boarding_pass = boarding_pass
        return True

    def get_row(self):
        """ Get a row between 0 and 128 """
        row_values = (i for i in range(0, 128))
        row_codes = self.__boarding_pass[:-3]
        binary_codes = row_codes.replace("F", "0").replace("B", "1")
        return BoardingPass._binary_hop(binary_codes, row_values)

    def get_column(self):
        """ Get a col between 0 and 7 """
        row_values = (i for i in range(0, 8))
        row_codes = self.__boarding_pass[-3:]
        binary_codes = row_codes.replace("L", "0").replace("R", "1")
        return BoardingPass._binary_hop(binary_codes, row_values)

    def get_id(self) -> int:
        return (self.get_row() * 8) + self.get_column()

    def pass_validate(self, boarding_pass: str) -> bool:
        """ Validates input """
        if len(boarding_pass) != 10:
            return False
        codes_row = ("F", "B",)
        codes_col = ("L", "R",)

        for letter in boarding_pass[0:6]:
            if letter not in codes_row:
                return False

        for letter in boarding_pass[7:9]:
            if letter not in codes_col:
                return False
        return True

    @classmethod
    def _binary_hop(cls, row_codes: str, row_values: tuple) -> int:
        """ It's just a step to the left... and then a slide to the right! """
        row_list = list(row_values)
        for code in row_codes[0:-1]:
            length = len(row_list) - 1
            mark = (length) // 2  # Oh hi Mark
            if code in "0":
                row_list = row_list[0:mark + 1]
            else:
                row_list = row_list[mark + 1:length + 1]

        return row_list[0] if row_codes[-1] in "0" else row_list[1]


def main():
    print("Absolute Assinine Airlines Seating Systems v1")
    if len(sys.argv) != 2:
        print("Useage: python day05a.py [filename]")
        exit()
    print("Processing scanned boarding passes...")
    with open(sys.argv[1], "r") as f:
        boarding_passes = f.read().split("\n")
    pass_check = BoardingPass()

    id_list = []
    for boarding_pass in boarding_passes:
        pass_check.set_boarding_pass(boarding_pass)
        if not pass_check:
            print(f"Something is wrong with this one: {boarding_pass}")
        id_list.append(pass_check.get_id())

    id_list.sort()
    print(f"Scanned {len(boarding_passes)} boarding passes.")
    print(f"Highest id: {id_list[-1]}")

    lowest = id_list[0]
    for index, seat_id in enumerate(id_list):
        if seat_id != (index + lowest):
            print(f"Your seat ID is: {seat_id}")
            exit()


if __name__ == "__main__":
    main()
