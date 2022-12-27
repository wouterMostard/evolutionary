from typing import List

import numpy as np

from board import Individual

inds: List[Individual] = []

for i in range(100):
    inds.append(Individual(n_queens=8))

# Selection, select 2 from the top K fitness and replace this one with a bad one from the bottom P
max_fitness = 0
iter_counter = 0

while True:
    iter_counter += 1

    if iter_counter == 1000:
        print('did not improve for 1000 iterations, stopping..')
        break

    inds: List[Individual] = sorted(inds, reverse=True)
    mean_fitness = np.mean([x.fitness for x in inds])

    print(f'Mean fitness: {mean_fitness}')

    if mean_fitness > max_fitness:
        max_fitness = mean_fitness
        iter_counter = 0

    # Get 2 from the top 10
    item1: Individual
    item2: Individual
    item1, item2 = np.random.choice(inds[:10], size=2, replace=False)

    new_item = item1.crossover(item2)

    if item1.fitness != item1.max_fitness:
        item1.mutate()

    if item2.fitness != item2.max_fitness:
        item2.mutate()

    inds[-1] = new_item

# For each item

# If the fitness is max then we can add this one to the solution and don't mutate

for val in inds[:10]:
    val.print_board()