"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day11
"""
import sys


class AOCGameofLife(object):
    """
    This is just an adjusted rule-set of Conway's Rule of Life
    We aren't going to use 2d lists though. Instead this will
    use a 1d string.
    """

    def __init__(self, input_file: tuple) -> None:
        assert isinstance(input_file, tuple)
        self._original = input_file
        self.game_board = "".join(self._original)
        self.width = len(self._original[0])
        self.height = len(self.game_board) // self.width
        self.stable = False
        return

    def __str__(self):
        return self.game_board

    def evole_board(self, debug: bool = False) -> None:
        copy = list(self.game_board)
        for idx, piece in enumerate(copy):
            if "." in piece:
                continue
            if self._count_neighbors(idx) >= 4:
                copy[idx] = "L"
                continue
            if self._count_neighbors(idx) == 0:
                copy[idx] = "#"
                continue
            # copy[idx] = "L" if self._count_neighbors(idx) >= 4 else piece
            # copy[idx] = "#" if not self._count_neighbors(idx) else piece
        self.game_board = "".join(copy)
        del copy
        return None

    def count_seats(self) -> int:
        return list(self.game_board).count("#")

    def _count_neighbors(self, idx: int) -> int:
        count = 0
        for row in range(-1, 2):
            row_shift = self.width * row
            for col in range(-1, 2):
                shift = row_shift + col + idx
                # Skip "us"
                if row == 0 and col == 0:
                    continue

                # Don't go out of bounds
                if shift < 0 or shift > (len(self.game_board) - 1):
                    continue

                # Don't wrap the board
                if (row_shift + idx) // self.width != shift // self.width:
                    continue

                count += 1 if self.game_board[shift] in "#" else 0
        return count


class AOCLineofSight(object):
    def __init__(self, input_file: tuple) -> None:
        assert isinstance(input_file, tuple)
        self._original = input_file
        self.game_board = "".join(self._original)
        self.width = len(self._original[0])
        self.height = len(self.game_board) // self.width
        self.stable = False
        return

    def __str__(self):
        return self.game_board

    def evole_board(self, debug: bool = False) -> None:
        copy = list(self.game_board)
        for idx, piece in enumerate(copy):
            if "." in piece:
                continue
            if self._see_neighbors(idx) >= 5:
                copy[idx] = "L"
                continue
            if self._see_neighbors(idx) == 0:
                copy[idx] = "#"
                continue
        self.game_board = "".join(copy)
        del copy
        return None

    def count_seats(self) -> int:
        return list(self.game_board).count("#")

    def _count_neighbors(self, idx: int) -> int:
        count = 0
        for row in range(-1, 2):
            row_shift = self.width * row
            for col in range(-1, 2):
                shift = row_shift + col + idx
                # Skip "us"
                if row == 0 and col == 0:
                    continue

                # Don't go out of bounds
                if shift < 0 or shift > (len(self.game_board) - 1):
                    continue

                # Don't wrap the board
                if (row_shift + idx) // self.width != shift // self.width:
                    continue

                count += 1 if self.game_board[shift] in "#" else 0
        return count

    def _see_neighbors(self, idx: int) -> int:
        count = self._count_northwest(idx)
        count += self._count_north(idx)
        count += self._count_northeast(idx)
        count += self._count_east(idx)
        count += self._count_southeast(idx)
        count += self._count_south(idx)
        count += self._count_southwest(idx)
        count += self._count_west(idx)
        return count

    def _move_index_x(self, idx: int, x: int) -> int:
        wrap_check = idx // self.width
        if wrap_check != (idx + x) // self.width:
            return idx
        return idx + x

    def _move_index_y(self, idx: int, y: int) -> int:
        return idx + y

    def _is_oob(self, idx: int) -> bool:
        return idx < 0 or idx > len(self.game_board) - 1

    def _count_north(self, idx: int) -> int:
        while not self._is_oob(idx):
            idx = self._move_index_y(idx, 1)
            if self.game_board[idx] == "#":
                return 1
            if self.game_board[idx] == "L":
                break
        return 0

    def _count_south(self, idx: int) -> int:
        seat = idx + self.width
        while seat <= len(self.game_board) - 1:
            if self.game_board[seat] == "#":
                return 1
            if self.game_board[seat] == "L":
                break
            seat += self.width
        return 0

    def _count_west(self, idx: int) -> int:
        row = idx // self.width
        seat = idx - 1
        while (seat // self.width) == row:
            if self.game_board[seat] == "#":
                return 1
            if self.game_board[seat] == "L":
                break
            seat -= 1
        return 0

    def _count_east(self, idx: int) -> int:
        row = idx // (self.width - 1)
        seat = idx + 1
        while (seat // self.width - 1) == row:
            if self.game_board[seat] == "#":
                return 1
            if self.game_board[seat] == "L":
                break
            seat += 1
        return 0

    def _count_northwest(self, idx: int) -> int:
        row = idx // self.width
        seat = idx - 1
        if (seat // self.width) != row:
            return 0
        seat = seat - self.width
        row = seat // self.width
        while seat >= 0:
            if self.game_board[seat] == "#":
                return 1
            if self.game_board[seat] == "L":
                break
            seat -= 1
            if (seat // self.width) != row:
                break
            seat -= self.width
            row = seat // self.width
        return 0

    def _count_northeast(self, idx: int) -> int:
        row = idx // self.width
        seat = idx + 1
        if (seat // self.width) != row:
            return 0
        seat = seat - self.width
        row = seat // self.width
        while seat >= 0:
            if self.game_board[seat] == "#":
                return 1
            if self.game_board[seat] == "L":
                break
            seat += 1
            if (seat // self.width) != row:
                break
            seat -= self.width
            row = seat // self.width
        return 0

    def _count_southwest(self, idx: int) -> int:
        row = idx // self.width
        seat = idx - 1
        if (seat // self.width) != row:
            return 0
        seat = seat + self.width
        row = seat // self.width
        while seat <= len(self.game_board) - 1:
            if self.game_board[seat] == "#":
                return 1
            if self.game_board[seat] == "L":
                break
            seat -= 1
            if (seat // self.width) != row:
                break
            seat += self.width
            row = seat // self.width
        return 0

    def _count_southeast(self, idx: int) -> int:
        row = idx // self.width
        seat = idx + 1
        if (seat // self.width) != row:
            return 0
        seat = seat + self.width
        row = seat // self.width
        while seat <= len(self.game_board) - 1:
            if self.game_board[seat] == "#":
                return 1
            if self.game_board[seat] == "L":
                break
            seat += 1
            if (seat // self.width) != row:
                break
            seat += self.width
            row = seat // self.width
        return 0


def main(input_file: tuple) -> None:
    game_board = AOCGameofLife(input_file)
    print(f"Board width: {game_board.width}")
    print(f"Board height: {game_board.height}")
    print(f"Board total size: {len(game_board.game_board)}")
    # prior_board = ""
    # while prior_board != game_board.game_board:
    #     prior_board = game_board.game_board
    #     game_board.evole_board()

    # print(f"Answer 1 Total seats: {game_board.count_seats()}")

    new_board = AOCLineofSight(input_file)
    prior_board = ""
    count = 0
    # idx = list(new_board.game_board).index("W")
    # print(f"start: {idx}")
    # print(new_board._see_neighbors(idx))
    # exit()

    while prior_board != new_board.game_board:
        count += 1
        prior_board = new_board.game_board
        new_board.evole_board()
        print(new_board.game_board)
        if count > 10:
            print("Something is wrong")
            exit()

    print(f"Answer 2 Total seats: {new_board.count_seats()}")
    for i in range(0, 10):
        print(new_board.game_board[i * 10 : i * 10 + 9])
    return


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Useage: python day11.py [filename]")
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
