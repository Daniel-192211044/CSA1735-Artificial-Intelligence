import heapq

def astar(grid, start, goal):
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = [(0, start)]
    heapq.heapify(pq)
    cost_so_far = {start: 0}
    
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        
        if current_node == goal:
            return cost_so_far[current_node]
        
        for direction in directions:
            neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])
            new_cost = current_cost + 1  # Assuming uniform cost for simplicity
            
            if neighbor in grid and (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]):
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor)
                heapq.heappush(pq, (priority, neighbor))
    
    return float('inf')  # No path found

# Example usage:
grid = {(0, 0), (0, 1), (1, 0), (1, 1), (2, 1), (2, 2)}
start = (0, 0)
goal = (2, 2)
min_cost = astar(grid, start, goal)
print(f"Minimum Cost to reach from {start} to {goal}: {min_cost}")
