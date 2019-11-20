import random

AMOUNT_OF_FOOD = 20
NUMBER_OF_ITERATIONS_TO_SIMULATE = 10
A_REPRODUCTION_CHANCE = 0.2
A_INIT_POPULATION = 10
A_POPULATION_COUNT = A_INIT_POPULATION

A_population = []
A_population_indices = []


class A:
    def __init__(self):
        self.alive = True
        self.food = 0


for i in range(A_INIT_POPULATION):
    A_population.append(A())
    A_population_indices.append(i)

for i in range(NUMBER_OF_ITERATIONS_TO_SIMULATE):
    iteration_food = AMOUNT_OF_FOOD
    # print(A_population_indices)
    # give food
    for j in range(min(iteration_food, A_POPULATION_COUNT)):
        random_choice = random.choice(A_population_indices)
        # print("random: ", random_choice)
        A_population[random_choice].food = 1
        del A_population_indices[A_population_indices.index(random_choice)]

    # check for deaths for next iteration
    for j in range(A_POPULATION_COUNT):
        if A_population[j].food == 0:
            A_population[j].alive = False

    A_POPULATION_COUNT = 0

    for j in range(len(A_population)):
        if A_population[j].alive:
            A_POPULATION_COUNT += 1

    A_population = [A() for i in range(A_POPULATION_COUNT)]
    A_population_indices = [i for i in range(A_POPULATION_COUNT)]

    # simulate reproduction
    temp_population = A_POPULATION_COUNT
    for j in range(int(A_REPRODUCTION_CHANCE * A_POPULATION_COUNT)):
        temp_population += 1
        A_population.append(A())
    A_POPULATION_COUNT = temp_population
    A_population_indices = [i for i in range(A_POPULATION_COUNT)]

    print("A_population_count: ", A_POPULATION_COUNT)
