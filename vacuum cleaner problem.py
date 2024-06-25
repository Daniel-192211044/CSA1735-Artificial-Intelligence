import random

class VacuumCleaner:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice(['clean', 'dirty']) for _ in range(cols)] for _ in range(rows)]
        self.position = (random.randint(0, rows-1), random.randint(0, cols-1))

    def print_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.grid[r][c], end=' ')
            print()
        print()

    def clean(self):
        while True:
            r, c = self.position
            if self.grid[r][c] == 'dirty':
                print(f"Cleaning position {self.position}")
                self.grid[r][c] = 'clean'
            if not self.move():
                break
            self.print_grid()

    def move(self):
        r, c = self.position
        if self.grid[r][c] == 'dirty':
            return True
        possible_moves = []
        if r > 0:
            possible_moves.append((-1, 0))  # Move up
        if r < self.rows - 1:
            possible_moves.append((1, 0))   # Move down
        if c > 0:
            possible_moves.append((0, -1))  # Move left
        if c < self.cols - 1:
            possible_moves.append((0, 1))   # Move right
        
        if possible_moves:
            dr, dc = random.choice(possible_moves)
            self.position = (r + dr, c + dc)
            print(f"Moving to position {self.position}")
            return True
        return False

# Example usage:
rows = 2
cols = 2
vacuum = VacuumCleaner(rows, cols)
print("Initial Grid:")
vacuum.print_grid()
print("Cleaning Process:")
vacuum.clean()
print("Final Grid:")
vacuum.print_grid()
