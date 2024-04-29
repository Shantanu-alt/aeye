# tic tac toe
import itertools
def tic_tac_toe():
    b,p=[' ']*9,['X','O']
    for i in itertools.cycle(p):
        print('\n'.join('|'.join(b[j:j+3]) for j in range(0,9,3)))
        m=int(input(f"Player {i}, enter your move (0-8): "))
        if b[m]!=' ':print("Invalid move! Try again.");continue
        b[m]=i
        if any(all(b[j]==i for j in c) for c in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]):return f"Player {i} wins!"
        if ' ' not in b:return "It's a draw!"
print(tic_tac_toe())
