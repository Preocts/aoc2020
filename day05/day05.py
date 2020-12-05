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


class SeatingChart(object):
    """ Load a list of used seating IDs and find remaining seats """

    def __init__(self) -> None:
        self.used_ids = ()
        self._rows_per_plane = 128
        self._seats_per_row = 8

    def _generate_chart(self, row_start: int, row_count: int) -> tuple:
        """ Creates a seating chart

        Starts at row_start and generates the number of rows requested
        """
        seating_chart = []
        for row in range(row_start, row_count):
            for col in range(0, self._seats_per_row):
                seating_chart.append((row * self._seats_per_row) + col)
        return tuple(seating_chart)

    def load_used_ids(self, id_list: list) -> bool:
        self.used_ids = tuple(sorted(id_list))
        return True

    def remaining_ids(self) -> tuple:
        starting_row = self.used_ids[0] // 8
        number_of_rows = (self.used_ids[-1] // 8) + 1 - starting_row
        seating_list = self._generate_chart(starting_row, number_of_rows)
        remaining_list = []
        for seat in seating_list:
            if seat not in self.used_ids:
                remaining_list.append(seat)
        return tuple(remaining_list)


def main() -> None:
    print("Absolute Assinine Airlines Seating Systems v1")
    if len(sys.argv) != 2:
        print("Useage: python day05.py [filename]")
        exit()
    print("Processing scanned boarding passes...")
    with open(sys.argv[1], "r") as f:
        boarding_passes = f.read().split("\n")
    pass_check = BoardingPass()
    seating_chart = SeatingChart()

    id_list = []
    for boarding_pass in boarding_passes:
        pass_check.set_boarding_pass(boarding_pass)
        if not pass_check:
            print(f"Something is wrong with this one: {boarding_pass}")
        id_list.append(pass_check.get_id())

    id_list.sort()
    seating_chart.load_used_ids(id_list)
    print(f"Scanned {len(boarding_passes)} boarding passes.")
    print(f"Highest id: {id_list[-1]}")
    print(f"Remaining seats: {seating_chart.remaining_ids()}")


if __name__ == "__main__":
    main()
