import random

AMOUNT_OF_FOOD = 30
NUMBER_OF_ITERATIONS_TO_SIMULATE = 10
A_REPRODUCTION_CHANCE = 0.2
B_REPRODUCTION_CHANCE = 0.2
A_INIT_POPULATION = 15
A_POPULATION_COUNT = A_INIT_POPULATION
B_INIT_POPULATION = 10
B_POPULATION_COUNT = B_INIT_POPULATION

# if A and B face off for a unit of food
B_CHANCE_OF_FOOD = 0.6
A_CHANCE_OF_FOOD = 1 - B_CHANCE_OF_FOOD


def chance(probability):
    """
    :param probability: Float
    :return: Boolean
    """
    if random.random() < probability:
        return True
    return False


class A:
    def __init__(self):
        self.alive = True
        self.food = 0


class B:
    def __init__(self):
        self.alive = True
        self.food = 0


# Set up initial values
A_population = [A() for i in range(A_INIT_POPULATION)]
A_population_indices = [i for i in range(A_INIT_POPULATION)]

B_population = [B() for i in range(B_INIT_POPULATION)]
B_population_indices = [i for i in range(B_INIT_POPULATION)]

for i in range(NUMBER_OF_ITERATIONS_TO_SIMULATE):
    iteration_food = AMOUNT_OF_FOOD

    # give food
    for j in range(min(iteration_food, A_POPULATION_COUNT, B_POPULATION_COUNT)):
        # random_choice = random.choice(A_population_indices)
        # # print("random: ", random_choice)
        # A_population[random_choice].food = 1
        # del A_population_indices[A_population_indices.index(random_choice)]
        if chance(A_CHANCE_OF_FOOD):
            random_choice = random.choice(A_population_indices)
            A_population[random_choice].food = 1
            del A_population_indices[A_population_indices.index(random_choice)]
        else:
            random_choice = random.choice(B_population_indices)
            B_population[random_choice].food = 1
            del B_population_indices[B_population_indices.index(random_choice)]

    # check if there's food left and some population still hungry
    if iteration_food > min(A_POPULATION_COUNT, B_POPULATION_COUNT):
        left_over_food = iteration_food - min(A_POPULATION_COUNT, B_POPULATION_COUNT)
        for j in range(left_over_food):
            A_chance = chance(A_CHANCE_OF_FOOD)
            if A_chance and len(A_population_indices) > 0:
                random_choice = random.choice(A_population_indices)
                A_population[random_choice].food = 1
                del A_population_indices[A_population_indices.index(random_choice)]
            elif not A_chance and len(B_population_indices) > 0:
                random_choice = random.choice(B_population_indices)
                B_population[random_choice].food = 1
                del B_population_indices[B_population_indices.index(random_choice)]
            else:
                continue

    # check for deaths for next iteration
    for j in range(A_POPULATION_COUNT):
        if A_population[j].food == 0:
            A_population[j].alive = False

    for j in range(B_POPULATION_COUNT):
        if B_population[j].food == 0:
            B_population[j].alive = False

    A_POPULATION_COUNT = 0
    B_POPULATION_COUNT = 0

    for j in range(len(A_population)):
        if A_population[j].alive:
            A_POPULATION_COUNT += 1

    for j in range(len(B_population)):
        if B_population[j].alive:
            B_POPULATION_COUNT += 1

    A_population = [A() for i in range(A_POPULATION_COUNT)]
    A_population_indices = [i for i in range(A_POPULATION_COUNT)]

    B_population = [B() for i in range(B_POPULATION_COUNT)]
    B_population_indices = [i for i in range(B_POPULATION_COUNT)]

    # simulate reproduction
    temp_population = A_POPULATION_COUNT
    for j in range(int(A_REPRODUCTION_CHANCE * A_POPULATION_COUNT)):
        temp_population += 1
        A_population.append(A())
    A_POPULATION_COUNT = temp_population
    A_population_indices = [i for i in range(A_POPULATION_COUNT)]

    temp_population = B_POPULATION_COUNT
    for j in range(int(B_REPRODUCTION_CHANCE * B_POPULATION_COUNT)):
        temp_population += 1
        B_population.append(B())

    B_POPULATION_COUNT = temp_population
    B_population_indices = [i for i in range(B_POPULATION_COUNT)]

    print("A_population_count: ", A_POPULATION_COUNT)
    print("B population count: ", B_POPULATION_COUNT)
    print()
