import numpy as np

class Individual:
    def __init__(self, n_queens: int = 8) -> None:
        self.board_size = n_queens
        self.col_indices = np.random.choice(np.arange(0, n_queens), size=n_queens, replace=False)
        self.genes = np.zeros(shape=(n_queens, n_queens))
        self.fill_genes()

        self.max_fitness = (n_queens * (n_queens - 1)) / 2
        self.fitness = self.calculate_fitness()
        
    def calculate_fitness(self):
        return self.max_fitness - self._calculate_diagonal_collisions()

    def fill_genes(self):
        self.genes = np.zeros(shape=(self.board_size, self.board_size))

        for row, col in enumerate(self.col_indices):
            self.genes[row, col] = 1

    def __eq__(self, __o: object) -> bool:
        return __o.fitness == self.fitness

    def __gt__(self, __o: object) -> bool:
        return self.fitness > __o.fitness

    def _calculate_diagonal_collisions(self):
        self.fill_genes()
        rows, cols = np.where(self.genes == 1)
        diagonal_collides = 0

        for row, col in zip(rows, cols):
            # go to top right
            row_i = row
            col_i = col
    
            while row_i >= 0 and col_i < self.board_size:
                if self.genes[row_i, col_i] == 1 and (row != row_i and col_i != col):
                    diagonal_collides += 1
                
                row_i -= 1
                col_i += 1

            # go to bottom right
            row_i = row
            col_i = col

            while row_i < 8 and col_i < self.board_size:
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

            while row_i < self.board_size and col_i >= 0:
                if self.genes[row_i, col_i] == 1 and (row != row_i and col_i != col):
                    diagonal_collides += 1
    
                row_i += 1
                col_i -= 1
        
        return diagonal_collides

    def mutate(self) -> None:
        i, j = np.random.choice(np.arange(0, self.board_size), size=2, replace=False)

        val1 = self.col_indices[i]
        self.col_indices[i] = self.col_indices[j]
        self.col_indices[j] = val1
        self.fill_genes()

    def crossover(self, __0: object) -> object:
        split_point = np.random.randint(0, self.board_size)
        new_item = Individual(n_queens=self.board_size)

        new_item.genes[:split_point] = __0.genes[:split_point]
        new_item.genes[split_point:] = self.genes[split_point:]

        new_item.fill_genes()

        return new_item

    def print_fitness(self):
        print(f"Fitness: {self.fitness:.0f}/{self.max_fitness:.0f}")

    def print_board(self):
        self.fill_genes()
        print(self.genes.astype(int))
        print(self.col_indices)
