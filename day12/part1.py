"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day12
"""


class GarvyTug(object):
    def __init__(self):
        self.x_units = 0
        self.y_units = 0

        self._facing = 1
        self._matrix = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]

    def apply_command(self, command: str) -> None:
        action = command[0]
        if action in ["N", "W", "E", "S"]:
            self._move_a_direction(command)
        if action in ["L", "R"]:
            self._change_facing(command)
        if action in "F":
            self._move_forward(command)
        return None

    def manhattan_distance(self) -> int:
        return abs(self.x_units) + abs(self.y_units)

    def _move_a_direction(self, command: str) -> None:
        facing = ["N", "E", "S", "W"].index(command[0])
        move_matrix = self._matrix[facing]
        amount = int(command[1:])
        self.x_units += (amount * move_matrix[0])
        self.y_units += (amount * move_matrix[1])
        return None

    def _change_facing(self, command: str) -> None:
        direction = command[0]
        amt = int(command[1:])
        self._facing += -1 * (amt // 90) if direction == "L" else amt // 90
        if 0 > self._facing or self._facing > 3:
            self._facing = abs(abs(self._facing) - 4)
        return None

    def _move_forward(self, command: str) -> None:
        amount = int(command[1:])
        move_matrix = self._matrix[self._facing]
        self.x_units += (amount * move_matrix[0])
        self.y_units += (amount * move_matrix[1])
        return None
