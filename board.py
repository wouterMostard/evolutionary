import numpy as np

class Individual:
    def __init__(self, n_queens: int = 8) -> None:
        self.board_size = 8
        self.col_indices = np.random.choice(np.arange(0, 8), size=n_queens, replace=False)
        self.genes = np.zeros(shape=(self.board_size, self.board_size))

        for row, col in enumerate(self.col_indices):
            self.genes[row, col] = 1

        self.fitness = self.fitness()

    def fitness(self):
        return 28 - self._calculate_diagonal_collisions()

    def __eq__(self, __o: object) -> bool:
        return __o.fitness == self.fitness

    def __gt__(self, __o: object) -> bool:
        return self.fitness > __o.fitness

    def _calculate_diagonal_collisions(self):
        rows, cols = np.where(self.genes == 1)
        diagonal_collides = 0

        for row, col in zip(rows, cols):
            # go to top right
            row_i = row
            col_i = col
    
            while row_i >= 0 and col_i < 8:
                if self.genes[row_i, col_i] == 1 and (row != row_i and col_i != col):
                    diagonal_collides += 1
                
                row_i -= 1
                col_i += 1

            # go to bottom right
            row_i = row
            col_i = col

            while row_i < 8 and col_i < 8:
                if self.genes[row_i, col_i] == 1 and (row != row_i and col_i != col):
                    diagonal_collides += 1
            
                row_i += 1
                col_i += 1

            # got to top left
            row_i = row
            col_i = col

            while row_i >= 0 and col_i >= 0:
                if self.genes[row_i, col_i] == 1 and (row != row_i and col_i != col):
                    diagonal_collides += 1
            
                row_i -= 1
                col_i -= 1

            # go to bottom left
            row_i = row
            col_i = col

            while row_i < 8 and col_i >= 0:
                if self.genes[row_i, col_i] == 1 and (row != row_i and col_i != col):
                    diagonal_collides += 1
    
                row_i += 1
                col_i -= 1
        
        return diagonal_collides

    def print_fitness(self):
        print(f"Fitness: {self.fitness}")
        print(f"Genes: {self.col_indices}")

    def print_board(self):
        print(self.genes.astype(int))
