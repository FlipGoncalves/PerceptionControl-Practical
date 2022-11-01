import random

colors = ['red', 'green', 'green', 'red' , 'red']

#motions = [[1]]                      # test 1
motions = [[1],[0],[-1],[1],[0]]     # test 2

p_move = 0.8


def move(p, U):
    """Update p after movement U"""

    for i in range(len(p)):
        population = [1] * int(p_move*100) + [0] * int((1-p_move)*100)
        choice = random.randint(0,len(population)-1)

        # moves
        if abs(U[0]) == 1 and population[choice] == 1:
            if (p[i] == 0 and U[0] == -1) or (p[i] == 4 and U[0] == 1):
                continue
            p[i] += U[0]

    return p


#main
p = []
for c in range(len(colors)):
    for i in range(10):
        p.append(c)

width  = len(colors)
n = width

for s in range(len(motions)):
    p = move(p,motions[s])
    print(f"p: {p}")

