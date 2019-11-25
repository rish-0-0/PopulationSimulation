import random
from math import ceil

NUMBER_OF_ITERATIONS = 30
AMOUNT_OF_FOOD = 50
SHARING_HAPPENS = 0.5
A_POPULATION_GROWTH = 0.3
B_POPULATION_GROWTH = 0.3
A_INIT_POPULATION = 10
B_INIT_POPULATION = 10


def chance(probability):
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


A_population = [A() for i in range(A_INIT_POPULATION)]
B_population = [B() for i in range(B_INIT_POPULATION)]
A_population_indices = [i for i in range(A_INIT_POPULATION)]
B_population_indices = [i for i in range(B_INIT_POPULATION)]

A_POPULATION_COUNT = A_INIT_POPULATION
B_POPULATION_COUNT = B_INIT_POPULATION

# print(A_population_indices)
# print(B_population_indices)

for _ in range(NUMBER_OF_ITERATIONS):
    iteration_food = AMOUNT_OF_FOOD

    # Feed food
    for i in range(0, AMOUNT_OF_FOOD, 2):
        # 2 units of food to be shared
        two_people = random.choice([(0, 1), (1, 1), (0, 0)])
        if two_people == (1, 1):
            try:
                # Two B's meet
                two_B = random.sample(B_population_indices, 2)
                # print("two_B", two_B)
                # two_B is an array of choices
                # make a random decision to give one guy all the food
                # Let's say what is the chance that one dude get's both units of food
                if chance(0.5):
                    B_population[two_B[0]].food = 2

                else:
                    B_population[two_B[1]].food = 2
            except (IndexError, ValueError) as e:
                continue

        elif two_people == (0, 1):
            try:
                # One A, One B
                one_A = random.choice(A_population_indices)
                one_B = random.choice(B_population_indices)
                # print("one_A", one_A)
                # print("one_B", one_B)
                # there is a chance that A will share the food and
                # there is a chance that B will take all the food
                if chance(SHARING_HAPPENS):
                    A_population[one_A].food += 1
                    B_population[one_B].food += 1
                else:
                    B_population[one_B].food = 2
            except (IndexError, ValueError) as e:
                continue

        else:
            try:
                # Two A's meet
                two_A = random.sample(A_population_indices, 2)
                # print("two_A", two_A)
                # They will end up sharing it
                A_population[two_A[0]].food += 1
                A_population[two_A[1]].food += 1
            except (IndexError, ValueError) as e:
                continue

        for j in range(A_POPULATION_COUNT):
            if A_population[j].food >= 2:
                # Check if it has already been deleted
                try:
                    del A_population_indices[A_population_indices.index(j)]
                except ValueError:
                    continue

        for j in range(B_POPULATION_COUNT):
            if B_population[j].food >= 2:
                # check if it has already been deleted
                try:
                    del B_population_indices[B_population_indices.index(j)]
                except ValueError:
                    continue

    # Check who has died after food distribution
    temp_A_population_count = A_POPULATION_COUNT
    temp_B_population_count = B_POPULATION_COUNT
    for i in range(A_POPULATION_COUNT):
        if A_population[i].food == 0:
            try:
                del A_population_indices[A_population_indices.index(i)]
                temp_A_population_count -= 1
            except (ValueError, IndexError) as e:
                continue

    for i in range(B_POPULATION_COUNT):
        if B_population[i].food == 0:
            try:
                del B_population_indices[B_population_indices.index(i)]
                temp_B_population_count -= 1
            except (ValueError, IndexError) as e:
                continue

    # Reproduce the people with two units of food
    A_POPULATION_COUNT = temp_A_population_count
    B_POPULATION_COUNT = temp_B_population_count

    A_population = [A() for i in range(A_POPULATION_COUNT)]
    B_population = [B() for i in range(B_POPULATION_COUNT)]

    for i in range(ceil(A_POPULATION_GROWTH * A_POPULATION_COUNT)):
        A_population.append(A())
        A_POPULATION_COUNT += 1

    for i in range(ceil(B_POPULATION_COUNT * B_POPULATION_GROWTH)):
        B_population.append(B())
        B_POPULATION_COUNT += 1

    print(_, "a_population", A_POPULATION_COUNT)
    print(_, "b_population", B_POPULATION_COUNT)
    print()
