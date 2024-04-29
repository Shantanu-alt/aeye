# 8 queen 
class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

def queen_constraint(q1, q2):
    i1, j1 = q1
    i2, j2 = q2
    return i1 != i2 and j1 != j2 and abs(i1 - i2) != abs(j1 - j2)

def generate_constraints(variables):
    constraints = {}
    for i, q1 in enumerate(variables):
        for j, q2 in enumerate(variables):
            if i != j:
                constraints[(q1, q2)] = queen_constraint
    return constraints

def backtracking_search(csp):
    assignment = {}
    return backtrack(assignment, csp)

def backtrack(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(var, value, assignment, csp):
            assignment[var] = value
            result = backtrack(assignment, csp)
            if result is not None:
                return result
            assignment.pop(var)
    return None

def select_unassigned_variable(assignment, csp):
    unassigned = [var for var in csp.variables if var not in assignment]
    return min(unassigned, key=lambda var: len(csp.domains[var]))

def order_domain_values(var, assignment, csp):
    return csp.domains[var]

def is_consistent(var, value, assignment, csp):
    for neighbor in csp.variables:
        if neighbor in assignment and (neighbor, var) in csp.constraints:
            if not csp.constraints[(neighbor, var)](assignment[neighbor], value):
                return False
    return True

def print_solution(solution):
    board = [['.' for _ in range(8)] for _ in range(8)]
    for queen, position in solution.items():
        i, j = position
        board[i][j] = 'Q'
    for row in board:
        print(' '.join(row))

def main():
    variables = ['Q' + str(i) for i in range(8)]
    domains = {var: [(i, j) for i in range(8) for j in range(8)] for var in variables}
    constraints = generate_constraints(variables)
    csp = CSP(variables, domains, constraints)

    solution = backtracking_search(csp)
    if solution is not None:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()