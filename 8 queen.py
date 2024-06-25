def print_board(positions):
    board = [['.' for _ in range(8)] for _ in range(8)]
    for row, col in enumerate(positions):
        board[row][col] = 'Q'
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(positions, row, col):
    for i in range(row):
        if positions[i] == col or \
           positions[i] - i == col - row or \
           positions[i] + i == col + row:
            return False
    return True

def solve_nq_util(positions, target_row, solutions):
    if target_row == len(positions):
        solutions.append(positions[:])
        return
    for col in range(len(positions)):
        if is_safe(positions, target_row, col):
            positions[target_row] = col
            solve_nq_util(positions, target_row + 1, solutions)

def solve_nq():
    positions = [-1] * 8
    solutions = []
    solve_nq_util(positions, 0, solutions)
    for solution in solutions:
        print_board(solution)
    if not solutions:
        print("Solution does not exist")
        return False
    return True

solve_nq()
