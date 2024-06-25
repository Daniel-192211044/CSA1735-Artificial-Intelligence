from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __str__(self):
        return f"M: {self.missionaries}, C: {self.cannibals}, B: {self.boat}"

def is_valid(state):
    if state.missionaries < 0 or state.missionaries > 3 or state.cannibals < 0 or state.cannibals > 3:
        return False
    if state.missionaries > 0 and state.missionaries < state.cannibals:
        return False
    if state.missionaries < 3 and (3 - state.missionaries) < (3 - state.cannibals):
        return False
    return True

def get_successors(current_state):
    successors = []
    if current_state.boat == 'left':
        for m in range(0, 3 + 1):
            for c in range(0, 3 + 1):
                if m + c >= 1 and m + c <= 2:
                    new_state = State(current_state.missionaries - m, current_state.cannibals - c, 'right')
                    if is_valid(new_state):
                        successors.append(new_state)
    else:
        for m in range(0, 3 + 1):
            for c in range(0, 3 + 1):
                if m + c >= 1 and m + c <= 2:
                    new_state = State(current_state.missionaries + m, current_state.cannibals + c, 'left')
                    if is_valid(new_state):
                        successors.append(new_state)
    return successors

def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state in visited:
            continue
        visited.add(current_state)
        
        if current_state == goal_state:
            return path + [current_state]
        
        for successor in get_successors(current_state):
            queue.append((successor, path + [current_state]))
    
    return None

def solve_missionaries_cannibals():
    initial_state = State(3, 3, 'left')
    goal_state = State(0, 0, 'right')
    
    solution = bfs(initial_state, goal_state)
    
    if solution:
        for i, state in enumerate(solution):
            print(f"Step {i + 1}: {state}")
    else:
        print("No solution found.")

# Solve the problem
solve_missionaries_cannibals()
