from typing import List

from board import Individual

inds: List[Individual] = []

for i in range(5000):
    inds.append(Individual(n_queens=8))

sorted = sorted(inds, reverse=True)

for val in sorted[:10]:
    val.print_fitness()