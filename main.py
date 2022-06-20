import random
import numpy as np

def random_individual_gen(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp
    return (key1)


def my_AG(population_size=10):
    random.seed(10)
    generation = 0
    population = {}
    population[generation] = []
    for i in range(0, population_size):
        new_individual = np.binary_repr(random.randrange(-100, 100), width=22) +\
                         np.binary_repr(random.randrange(-100, 100), width=22)

        # changing the first string element
        # new_individual = new_individual[:0] + 'A' + new_individual[0 + 1:]
        population[generation].append(new_individual)

    print(population)

    # BEFORE APLYING THE FO
    # new_individual = (int(new_individual[0:21], 2) * (200/(2**22-1))) - 100


if __name__ == '__main__':
    my_AG()
