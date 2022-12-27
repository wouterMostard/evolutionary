from typing import List
import pickle

import numpy as np

from board import Individual

inds: List[Individual] = []
max_iters = 10000

for i in range(1000):
    inds.append(Individual(n_queens=8))

# Selection, select 2 from the top K fitness and replace this one with a bad one from the bottom P
max_fitness = 0
iter_counter = 0
convergence = []

while True:
    iter_counter += 1

    if iter_counter == max_iters:
        print(f'did not improve for {max_iters} iterations, stopping..')
        break

    inds: List[Individual] = sorted(inds, reverse=True)
    mean_fitness = np.mean([x.fitness for x in inds])
    convergence.append(mean_fitness)

    print(f'Mean fitness: {mean_fitness}')

    if mean_fitness > max_fitness:
        max_fitness = mean_fitness
        iter_counter = 0

    # Get 2 from the top 10
    item1: Individual
    item2: Individual
    item1, item2 = np.random.choice(inds[:100], size=2, replace=False)

    new_item = item1.crossover(item2)

    if item1.calculate_fitness() != item1.max_fitness:
        item1.mutate()

    if item2.calculate_fitness() != item2.max_fitness:
        item2.mutate()

    inds[-1] = new_item

inds[0].print_board()
inds[0].print_fitness()

inds[-1].print_board()
inds[-1].print_fitness()

# Store the final boards
with open('./boards.pkl', 'wb') as file:
    pickle.dump(inds, file)
convergence = np.array(convergence)

np.save(open('./convergence.npy', 'wb'), convergence)