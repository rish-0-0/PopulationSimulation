import random

AMOUNT_OF_FOOD = 20


class Faster:
    def __init__(self):
        self.speed = 2
        self.size = 1
        self.sense = 1
        self.alive = True
        self.food = 0


class Bigger:
    def __init__(self):
        self.speed = 1
        self.size = 2
        self.sense = 1
        self.alive = True
        self.food = 0


class Aware:
    def __init__(self):
        self.speed = 1
        self.size = 1
        self.sense = 2
        self.alive = True
        self.food = 0
