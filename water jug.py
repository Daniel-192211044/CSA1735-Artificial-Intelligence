from collections import deque

def is_valid_state(state, capacity):
    return 0 <= state[0] <= capacity[0] and 0 <= state[1] <= capacity[1]

def is_goal_state(state, goal):
    return state[0] == goal or state[1] == goal

def get_successors(state, capacity):
    successors = []
    jug1, jug2 = state
    cap1, cap2 = capacity

    successors.append((cap1, jug2))
    successors.append((jug1, cap2))
    successors.append((0, jug2))
    successors.append((jug1, 0))
    pour = min(jug1, cap2 - jug2)
    successors.append((jug1 - pour, jug2 + pour))
    pour = min(jug2, cap1 - jug1)
    successors.append((jug1 + pour, jug2 - pour))

    return [s for s in successors if is_valid_state(s, capacity)]

def bfs(start, goal, capacity):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (state, path) = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if is_goal_state(state, goal):
            return path + [state]
        for successor in get_successors(state, capacity):
            queue.append((successor, path + [state]))
    
    return None

def solve_water_jug(capacity, start, goal):
    solution = bfs(start, goal, capacity)
    if solution:
        for state in solution:
            print(state)
    else:
        print("No solution exists")

# Example usage
capacity = (4, 3)  # Jug1 capacity is 4 liters, Jug2 capacity is 3 liters
start = (0, 0)     # Both jugs are initially empty
goal = 2           # We want exactly 2 liters in either jug

solve_water_jug(capacity, start, goal)
