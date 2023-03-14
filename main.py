# Rather than expand on the existing solution from lab 1, I decided to attempt
# my own complete implementation, in order to achieve a greater understanding
# of the underlying algorithms.

from enum import Enum


class State(Enum):
    CLEAN = 0
    DIRTY = 1
    BLOCKED = 2

# Movement action has an arbitrary cost of 2
# Suck action has an arbitrary cost of 3


class Cell:
    def __init__(self, state: State):
        self.state = state
        self.is_explored = False

    def setNeighbours(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right


floor_plan = [
    [Cell(State.DIRTY), Cell(State.DIRTY), None],
    [Cell(State.DIRTY), Cell(State.CLEAN), Cell(State.DIRTY)],
    [Cell(State.CLEAN), None, None]
]

CURRENT_CELL = floor_plan[0]


def run():
    print('Run A* here')


if __name__ == '__main__':
    run()
