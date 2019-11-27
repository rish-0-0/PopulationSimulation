import random
from matplotlib import pyplot as plt

WORLD_SIZE = 50

world = [[False] * WORLD_SIZE for _ in range(WORLD_SIZE)]

# place food random locations
# There are at max WORLD_SIZE*WORLD_SIZE locations, choose like hundred?
AMOUNT_OF_FOOD = 30
NUMBER_OF_ITERATIONS = 5
INIT_POPULATION = 20
FOOD_INTAKE = 50
REPLICATION_THRESHOLD = 70

INIT_SPEED = 2
INIT_SIZE = 2
INIT_SENSE = 2


def chance(probability):
    return random.random() <= probability


def random_position(size):
    if chance(0.5):
        if chance(0.5):
            return [random.randint(0, size - 1), 0]
        else:
            return [random.randint(0, size - 1), size - 1]
    else:
        if chance(0.5):
            return [0, random.randint(0, size - 1)]
        else:
            return [size - 1, random.randint(0, size - 1)]


def energy_value(tup):
    return (tup[0] ** 2) * (tup[1] ** 3) + tup[2]


def refactor(loss, spd, siz, sen):
    temp_loss = loss
    values = [(spd + 1, siz - 1, sen + 1),
              (spd - 1, siz + 1, sen + 1),
              (spd + 1, siz + 1, sen - 1),
              (spd + 1, siz - 1, sen - 1),
              (spd - 1, siz + 1, sen - 1),
              (spd - 1, siz - 1, sen + 1),
              ]
    mini = values[0]
    for i in range(1, len(values)):
        if energy_value(values[i]) < energy_value(mini):
            mini = values[i]

    return mini


class People:
    def __init__(self, speed, size, sense, position):
        self.energy = 1000
        self.speed = speed
        self.size = size
        self.sense = sense
        self.position = position

    def energy_per_step(self):
        return pow(self.speed, 2) * pow(self.size, 3) + self.sense


POPULATION_COUNT = INIT_POPULATION
Population = [People(INIT_SPEED, INIT_SIZE, INIT_SENSE, random_position(WORLD_SIZE)) for _ in range(POPULATION_COUNT)]
Energy_loss = [0]
Speed = [INIT_SPEED]
Size = [INIT_SIZE]
Sense = [INIT_SENSE]

for _ in range(NUMBER_OF_ITERATIONS):
    energy_loss = 0
    speed = Speed[_]
    size = Speed[_]
    sense = Speed[_]

    temp_population_count = POPULATION_COUNT

    random_food_x = random.sample([i for i in range(WORLD_SIZE)], AMOUNT_OF_FOOD)
    random_food_y = random.sample([i for i in range(WORLD_SIZE)], AMOUNT_OF_FOOD)
    # Distribute food randomly in the world
    for m in range(AMOUNT_OF_FOOD):
        world[random_food_x[m]][random_food_y[m]] = True

    # Move around and search for food
    for i in range(POPULATION_COUNT):
        # find out how many steps ith member can take
        number_of_steps = Population[i].energy // Population[i].energy_per_step()
        for j in range(number_of_steps):
            # Move left or right
            if chance(0.5):
                if Population[i].position[0] >= Population[i].speed:
                    Population[i].position[0] -= Population[i].speed
                elif Population[i].position[0] + Population[i].speed < WORLD_SIZE:
                    Population[i].position[0] += Population[i].speed
                else:
                    if Population[i].position[1] >= Population[i].speed:
                        Population[i].position[1] -= Population[i].speed
                    elif Population[i].position[1] + Population[i].speed < WORLD_SIZE:
                        Population[i].position[1] += Population[i].speed
            # Move up or down
            else:
                if Population[i].position[1] >= Population[i].speed:
                    Population[i].position[1] -= Population[i].speed
                elif Population[i].position[1] + Population[i].speed < WORLD_SIZE:
                    Population[i].position[1] += Population[i].speed
                else:
                    if Population[i].position[0] >= Population[i].speed:
                        Population[i].position[0] -= Population[i].speed
                    elif Population[i].position[0] + Population[i].speed < WORLD_SIZE:
                        Population[i].position[0] += Population[i].speed

            Population[i].energy -= Population[i].energy_per_step()
            energy_loss += Population[i].energy_per_step()

            if world[Population[i].position[0]][Population[i].position[1]]:
                Population[i].energy += FOOD_INTAKE

            if Population[i].energy <= 0:
                temp_population_count -= 1

            if chance(0.2):
                temp_population_count += 1

        speed = Population[i].speed
        sense = Population[i].sense
        size = Population[i].size

    speed, size, sense = refactor(energy_loss, speed, size, sense)
    Speed.append(speed)
    Size.append(size)
    Sense.append(sense)
    Energy_loss.append(energy_loss)

    POPULATION_COUNT = temp_population_count
    Population = [People(speed, size, sense, random_position(WORLD_SIZE)) for i in range(POPULATION_COUNT)]


print(Energy_loss)
print(Speed)
print(Size)
print(Sense)
plt.bar(Energy_loss, Speed)

