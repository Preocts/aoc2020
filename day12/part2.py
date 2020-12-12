"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day12
"""


class GhostShip(object):
    def __init__(self):
        self.ship_x_units = 0
        self.ship_y_units = 0
        self.ghost_x_units = 10
        self.ghost_y_units = 1

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
            self._rotate_ghost(command)
            self._change_facing(command)
        if action in "F":
            self._move_to_waypoint(command)
        return None

    def manhattan_distance(self) -> int:
        return abs(self.ship_x_units) + abs(self.ship_y_units)

    def _move_a_direction(self, command: str) -> None:
        facing = ["N", "E", "S", "W"].index(command[0])
        move_matrix = self._matrix[facing]
        amount = int(command[1:])
        self.ghost_x_units += (amount * move_matrix[0])
        self.ghost_y_units += (amount * move_matrix[1])
        return None

    def _change_facing(self, command: str) -> None:
        direction = command[0]
        amt = int(command[1:])
        self._facing += -1 * (amt // 90) if direction == "L" else amt // 90
        if 0 > self._facing or self._facing > 3:
            self._facing = abs(abs(self._facing) - 4)
        return None

    def _rotate_ghost(self, command: str) -> None:
        degree = int(command[1:])
        shift = -1 if command[0] == "R" else 1
        for _ in range(0, degree // 90):
            self.ghost_x_units, self.ghost_y_units = [
                self.ghost_y_units * -(shift),
                self.ghost_x_units * shift,
            ]

    def _move_to_waypoint(self, command: str) -> None:
        amount = int(command[1:])
        self.ship_x_units += (self.ghost_x_units * amount)
        self.ship_y_units += (self.ghost_y_units * amount)
        return None
