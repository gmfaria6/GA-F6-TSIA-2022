import random
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm


def calculate_FO(x, y):
    F6 = 0.5 - ((math.sin(math.sqrt(x*x + y*y)))**2 - 0.5)/((1.0 + 0.001 * (x**2 + y**2))**2)

    return F6


def roulette_selection(parents_pool, population_size):
    roulette = []

    new_parents = []

    while len(new_parents) < population_size:
        for parent in parents_pool:
            slot_size = int(parent["fitness"] * 10)

            for i in range(0, slot_size):
                roulette.append({"id": parent["id"], "fitness": parent["fitness"]})

        selected = random.randrange(0, len(roulette))

        new_parents.append(roulette[selected])

    return new_parents


def crossover(parent1, parent2):
    position = random.randrange(0, 22)

    new_parent1 = parent1[0:position] + parent2[position:len(parent1)]
    new_parent2 = parent2[0:position] + parent1[position:len(parent1)]

    return new_parent1, new_parent2


def mutation(parent1, parent2, mutation_param):
    for i in range(0, len(parent1)):
        if random.randrange(0, 100) < mutation_param+1:
            if parent1[i] == '1':
                parent1 = parent1[:i] + '0' + parent1[i + 1:]
            else:
                parent1 = parent1[:i] + '1' + parent1[i + 1:]

    return parent1, parent2


def my_AG(population_size, number_of_generations, crossover_param, mutation_param, considered):
    random.seed(55)
    population = {}
    population[0] = []

    for generation in range(0, number_of_generations):
        print("----------------------------------------------------------------------------------------------")
        print("Generation", generation)
        print("----------------------------------------------------------------------------------------------")

        population[generation + 1] = []

        if not generation:
            for i in range(0, int(population_size/2)):
                new_cromo = np.binary_repr(random.randrange(-100, 100), width=22) +\
                                 np.binary_repr(random.randrange(-100, 100), width=22)

                x = (int(new_cromo[0:22], 2) * (200 / (2 ** 22 - 1))) - 100
                y = (int(new_cromo[22:44], 2) * (200 / (2 ** 22 - 1))) - 100

                population[generation].append({"id": new_cromo, "fitness": round(calculate_FO(x, y), considered)})

        value = 0

        for cromo in population[generation]:
            if cromo["fitness"] > value:
                value = cromo["fitness"]
                best_cromo = cromo
        print("BEST CROMO FITNESS", best_cromo["fitness"])

        parents_pool = []

        for cromo in population[generation]:
            parents_pool.append({"id": cromo["id"][0:22], "fitness": cromo["fitness"]})
            parents_pool.append({"id": cromo["id"][22:44], "fitness": cromo["fitness"]})

        selected_parents = roulette_selection(parents_pool, population_size)

        it = 0

        while it < len(selected_parents):
            parent1 = selected_parents[it]
            it += 1
            parent2 = selected_parents[it]

            if random.randrange(0, 100) < crossover_param+1:
                parent1["id"], parent2["id"] = crossover(parent1["id"], parent2["id"])

            parent1["id"], parent2["id"] = mutation(parent1["id"], parent2["id"], mutation_param)

            x = (int(parent1["id"], 2) * (200 / (2 ** 22 - 1))) - 100
            y = (int(parent2["id"], 2) * (200 / (2 ** 22 - 1))) - 100

            population[generation + 1].append({"id": parent1["id"]+parent2["id"], "fitness": round(calculate_FO(x, y), considered)})
            it += 1

        index_out = random.randrange(0, len(population[generation + 1]))
        population[generation + 1][index_out] = best_cromo

        # print((int(best_cromo["id"][0:22], 2) * (200 / (2 ** 22 - 1))) - 100)
        # print((int(best_cromo["id"][22:44], 2) * (200 / (2 ** 22 - 1))) - 100)

        generation += 1
    return population


if __name__ == '__main__':
    all_population = my_AG(population_size=200,
                           number_of_generations=200,
                           crossover_param=75,
                           mutation_param=1,
                           considered=7)

    x = []
    y = []
    z = []
    c = []

    for generation in all_population:
        for croma in all_population[generation]:
            c.append(generation)
            x.append((int(croma["id"][0:22], 2) * (200 / (2 ** 22 - 1))) - 100)
            y.append((int(croma["id"][22:44], 2) * (200 / (2 ** 22 - 1))) - 100)
            z.append(croma["fitness"])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z, c=c, cmap=cm.coolwarm, marker='o')

    # plt.colorbar(label="Generation", orientation="horizontal", c=c, cmap=cm.coolwarm)
    plt.show()

    plt.save("GA_F6.png")

    # (100 - 40) BEST CROMO FITNESS 0.9999993979950594
    # (10 - 400) BEST CROMO FITNESS 0.9999999988619942
