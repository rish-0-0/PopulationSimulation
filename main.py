import random


def chance(probability):
    return random.random() < probability


AMOUNT_OF_FOOD = 100
NUMBER_OF_ITERATIONS = 20

A_INIT_POPULATION = 10
B_INIT_POPULATION = 10
C_INIT_POPULATION = 10

# A is faster, B is bigger, C is smarter
# Also, B can eat either A or C
A_CHANCE_EATEN = 0.3
C_CHANCE_EATEN = 0.1

# A is faster, but burns energy twice as fast too so will need more food
# B is bigger, slow moving so less energy usage but food requirements are huge
# C is smarter, burn regular amount of energy
A_GROWTH_RATE = 1
B_GROWTH_RATE = 1
C_GROWTH_RATE = 1

ENERGY_GAIN = 50
ENERGY_LOSS = 25

# Natural Selection will try to always increase growth rate
# All the factors increase growth rate so, if growth rate drops, the dominating factor increases
# The greedy algorithm will work that way

A_SPEED = 2
B_SPEED = 0.5
C_SPEED = 1

A_SIZE = 0.5
B_SIZE = 2
C_SIZE = 1

# Food gathering is proportional to speed of the person and inversely proportional to size: k*speed / size

A_FOOD_GATHERING = 0.7
B_FOOD_GATHERING = 0.4
C_FOOD_GATHERING = 0.6

A_POPULATION_COUNT = A_INIT_POPULATION
B_POPULATION_COUNT = B_INIT_POPULATION
C_POPULATION_COUNT = C_INIT_POPULATION

A_ENERGY_CAP = 75
B_ENERGY_CAP = 150
C_ENERGY_CAP = 100

A_population = [A_ENERGY_CAP//2 for _ in range(A_INIT_POPULATION)]
B_population = [B_ENERGY_CAP//2 for _ in range(B_INIT_POPULATION)]
C_population = [C_ENERGY_CAP//2 for _ in range(C_INIT_POPULATION)]

A_hungry_population_indices = [i for i in range(A_INIT_POPULATION)]
B_hungry_population_indices = [i for i in range(B_INIT_POPULATION)]
C_hungry_population_indices = [i for i in range(C_INIT_POPULATION)]


for _ in range(NUMBER_OF_ITERATIONS):

    # give food
    iteration_food = AMOUNT_OF_FOOD

    for i in range(iteration_food):
        if chance(A_FOOD_GATHERING):
            random_A = random.choice(A_hungry_population_indices)
            A_population[random_A] = min(A_population[random_A]+ENERGY_GAIN, A_ENERGY_CAP)
            if A_population[random_A] == A_ENERGY_CAP:
                try:
                    del A_hungry_population_indices[random_A]
                except (ValueError, IndexError) as e:
                    continue
        else:
            if chance(C_FOOD_GATHERING):
                random_C = random.choice(C_hungry_population_indices)
                C_population[random_C] = min(C_population[random_C] + ENERGY_GAIN, C_ENERGY_CAP)
                if C_population[random_C] == C_ENERGY_CAP:
                    try:
                        del C_hungry_population_indices[random_C]
                    except (ValueError, IndexError) as e:
                        continue
            else:
                random_B = random.choice(B_hungry_population_indices)
                B_population[random_B] = min(B_population[random_B] + ENERGY_GAIN, B_ENERGY_CAP)
                if B_population[random_B] == B_ENERGY_CAP:
                    try:
                        del B_hungry_population_indices[random_B]
                    except (ValueError, IndexError) as e:
                        continue
        # All the hungry people will lose energy
        temp_A_hungry = []
        for j in range(len(A_hungry_population_indices)):
            if A_population[A_hungry_population_indices[j]] == 0 or (A_population[A_hungry_population_indices[j]]
                                                                     - A_SPEED*ENERGY_LOSS <= 0):
                del A_population[A_hungry_population_indices[j]]
                temp_A_hungry.append(j)
            else:
                A_population[A_hungry_population_indices[j]] -= A_SPEED*ENERGY_LOSS

        for x in range(len(temp_A_hungry)):
            del A_hungry_population_indices[x]

        temp_C_hungry = []
        for j in range(len(C_hungry_population_indices)):
            if C_population[C_hungry_population_indices[j]] == 0 or (C_population[C_hungry_population_indices[j]]
                                                                     - C_SPEED*ENERGY_LOSS <= 0):
                del C_population[C_hungry_population_indices[j]]
                temp_C_hungry.append(j)
            else:
                C_population[C_hungry_population_indices[j]] -= C_SPEED*ENERGY_LOSS

        for x in range(len(temp_C_hungry)):
            del C_hungry_population_indices[x]

        temp_B_hungry = []
        for j in range(len(B_hungry_population_indices)):
            # feed on A or C
            if chance(C_CHANCE_EATEN):
                random_C = random.choice([i for i in range(len(C_population))])
                del C_population[random_C]
                B_population[B_hungry_population_indices[j]] = B_ENERGY_CAP
                temp_B_hungry.append(j)
            else:
                if chance(A_CHANCE_EATEN):
                    random_A = random.choice([i for i in range(len(A_population))])
                    del A_population[random_A]
                    B_population[B_hungry_population_indices[j]] = B_ENERGY_CAP
                    temp_B_hungry.append(j)
                else:
                    if B_population[B_hungry_population_indices[j]] == 0 or (
                            B_population[B_hungry_population_indices[j]] - B_SPEED*ENERGY_LOSS <= 0):

                        del B_population[B_hungry_population_indices[j]]
                        temp_B_hungry.append(j)
                    else:
                        B_population[B_hungry_population_indices[j]] -= B_SPEED*ENERGY_LOSS

        for x in range(len(temp_B_hungry)):
            del B_hungry_population_indices[x]



