from constraint import Problem, AllDifferentConstraint

def map_coloring_csp():
    problem = Problem()
    problem.addVariables(['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T'], ['Red', 'Green', 'Blue'])
    problem.addConstraint(AllDifferentConstraint(), ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T'])
    solutions = problem.getSolutions()
    print(solutions)

# Example usage:
map_coloring_csp()
