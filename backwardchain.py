# Backward chaining 


def backward_chaining(knowledge_base, goal, inferred=None):
    if inferred is None:
        inferred = {}

    if goal in inferred:
        return inferred[goal]

    for consequent, antecedents in knowledge_base:
        if goal in consequent:
            temp_inferred = inferred.copy()
            if all(backward_chaining(knowledge_base, premise, temp_inferred) for premise in antecedents):
                inferred.update(temp_inferred)
                inferred[goal] = True
                return True

    inferred[goal] = False
    return False


knowledge_base = [
    (['A'], ['B']),
    (['B'], ['C']),
    (['C'], []),
    (['D'], ['E']),
    (['E'], ['F']),
    (['F'], []),
    (['G'], ['H']),
    (['H'], ['I']),
    (['I'], []),
]


goal = 'A'

result = backward_chaining(knowledge_base, goal)

if result:
    print(f"The goal '{goal}' can be inferred.")
else:
    print(f"The goal '{goal}' cannot be inferred.")
