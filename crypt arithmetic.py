import itertools

def is_valid(puzzle, solution):
    words = puzzle.split()
    equation = puzzle.replace(" ", "")
    for word in words:
        equation = equation.replace(word, str(solution[word[0]]), 1)
    return eval(equation)

def solve_cryptarithmetic(puzzle):
    letters = set(char for char in puzzle if char.isalpha())
    if len(letters) > 10:
        print("Invalid puzzle. More than 10 unique letters.")
        return
    
    letters = list(letters)

    for perm in itertools.permutations(range(10), len(letters)):
        solution = {letters[i]: perm[i] for i in range(len(letters))}
        
        # Check if any word starts with 0 (except single-letter words)
        valid_solution = True
        for word in puzzle.split():
            if solution.get(word[0]) == 0 and len(word) > 1:
                valid_solution = False
                break
        
        if valid_solution and is_valid(puzzle, solution):
            for word in puzzle.split():
                print(word, ":", "".join(str(solution[char]) for char in word))
            return True
    
    print("No solution found.")
    return False

# Example usage:
puzzle = "SEND + MORE = MONEY"
solve_cryptarithmetic(puzzle)
