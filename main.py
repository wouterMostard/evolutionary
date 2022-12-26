from typing import List

from board import Individual

inds: List[Individual] = []

for i in range(1):
    inds.append(Individual())

sorted = sorted(inds, reverse=True)

for val in sorted[:1]:
    print(val.print_board())
    print(val.print_fitness())