from enum import Enum
import random


class Moves(Enum):
    U = 0
    Ui = 1
    D = 2
    Di = 3
    L = 4
    Li = 5
    R = 6
    Ri = 7
    F = 8
    Fi = 9
    B = 10
    Bi = 11


class Discrete():
    def __init__(self, num_actions):
        self.num_actions = num_actions

    def contains(self, x):
        if isinstance(x, int):
            return x >= 0 and x < self.num_actions
        else:
            return False

    def sample(self):
        return random.randint(0, self.num_actions)

    def __repr__(self):
        return "Discrete(%d)" % self.num_actions
