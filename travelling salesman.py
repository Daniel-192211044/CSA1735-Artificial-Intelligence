import sys

def tsp_dp(graph, start):
    n = len(graph)
    memo = {}
    
    def tsp(mask, current):
        if mask == (1 << n) - 1:
            return graph[current][start]
        if (mask, current) in memo:
            return memo[(mask, current)]
        
        min_cost = sys.maxsize
        for city in range(n):
            if not mask & (1 << city):
                new_mask = mask | (1 << city)
                cost = graph[current][city] + tsp(new_mask, city)
                min_cost = min(min_cost, cost)
        
        memo[(mask, current)] = min_cost
        return min_cost
    
    return tsp(1 << start, start)

# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start_node = 0
min_cost = tsp_dp(graph, start_node)
print(f"Minimum Cost: {min_cost}")

