import heapq

def manhattan_distance(board, goal):
    distance = 0
    goal_dict = {val: (i // 3, i % 3) for i, val in enumerate(goal)}
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                goal_x, goal_y = goal_dict[board[i][j]]
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def generate_children(board):
    children = []
    x, y = [(ix, iy) for ix, row in enumerate(board) for iy, i in enumerate(row) if i == 0][0]
    directions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    for dx, dy in directions:
        if 0 <= dx < 3 and 0 <= dy < 3:
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[dx][dy] = new_board[dx][dy], new_board[x][y]
            children.append(new_board)
    return children

def a_star_search(start_board, goal_board):
    goal_flat = [item for sublist in goal_board for item in sublist]
    start_cost = manhattan_distance(start_board, goal_flat)

    frontier = [(start_cost, start_board)]
    heapq.heapify(frontier)
    explored = set()
    parent_map = {str(start_board): None}
    depth_map = {str(start_board): 0}

    while frontier:
        _, current_board = heapq.heappop(frontier)

        if [item for sublist in current_board for item in sublist] == goal_flat:
            path = []
            while current_board:
                path.append(current_board)
                current_board = parent_map[str(current_board)]
            path.reverse()
            return path

        explored.add(str(current_board))
        for child in generate_children(current_board):
            child_str = str(child)
            if child_str not in explored:
                depth_map[child_str] = depth_map[str(current_board)] + 1
                cost = depth_map[child_str] + manhattan_distance(child, goal_flat)
                heapq.heappush(frontier, (cost, child))
                parent_map[child_str] = current_board

    return None

def print_solution(solution):
    for step in solution:
        for row in step:
            print(row)
        print()

def input_board(prompt):
    board = []
    print(prompt)
    for _ in range(3):
        row = list(map(int, input().split()))
        board.append(row)
    return board

if __name__ == "__main__":
    start_board = input_board("Enter the start board (use 0 for the blank space):")
    goal_board = input_board("Enter the goal board (use 0 for the blank space):")

    solution = a_star_search(start_board, goal_board)
    if solution:
        print("Solution found!")
        print_solution(solution)
    else:
        print("No solution exists.")
