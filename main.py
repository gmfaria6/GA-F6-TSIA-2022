import random
import numpy as np
import math

def random_individual_gen(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp
    return (key1)


def calculate_FO(x, y):
    F6 = 0.5 - ((math.sin(math.sqrt(x*x + y*y)))**2 - 0.5)/((1.0 + 0.001 * (x**2 + y**2))**2)

    return F6


def my_AG(population_size=10):
    random.seed(10)
    generation = 0
    population = {}
    population[generation] = []
    for i in range(0, population_size):
        new_individual = np.binary_repr(random.randrange(-100, 100), width=22) +\
                         np.binary_repr(random.randrange(-100, 100), width=22)

        # BEFORE APLYING THE FO
        x = (int(new_individual[0:21], 2) * (200 / (2 ** 22 - 1))) - 100
        y = (int(new_individual[21:44], 2) * (200 / (2 ** 22 - 1))) - 100

        population[generation].append({'id': new_individual, 'fitness': calculate_FO(x, y)})

    print(population)


    # changing the first string element
    # new_individual = new_individual[:0] + 'A' + new_individual[0 + 1:]

    # SELECIONA CONJUNTO DE PAIS (N/2 PARES) - ROLETA
    # SE DER CRUZAMENTO - CRUZA GERANDO 2 FILHOS - TAXA DE CROSSOVER
    # SE DER MUTAÇÃO - MUTA FILHOS (APENAS FILHOS) - TAXA DE MUTAÇÃO
    # PROXIMA GERAÇÃO - TODOS OS FILHOS - 1 (MELHOR PAI, NO LUGAR DE 1 FILHO ALEATÓRIO)


if __name__ == '__main__':
    my_AG()
