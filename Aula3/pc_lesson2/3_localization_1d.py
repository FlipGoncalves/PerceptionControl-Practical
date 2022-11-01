import random

colors = ['red', 'green', 'green', 'red' , 'red']

#measurements = ['green']                                            # test 1
#motions = [[1]]                                                     # test 1
measurements = ['green', 'green', 'green' ,'green', 'green','red']  # test 2
motions = [[1],[0],[-1],[1],[1],[0]]                                # test 2

sensor_right = {}
sensor_right['green'] = 0.6
sensor_right['red'] = 0.8


p_move = 0.8

def sense(p, Z):
    """Update belief array p according to new measurement Z"""

    weight = []

    for i in range(len(p)):
        if colors[p[i]] == 'red':
            weight.append(sensor_right['red'] if Z == 'red' else 1 - sensor_right['red'])
        else:
            weight.append(sensor_right['green'] if Z == 'green' else 1 - sensor_right['green'])

    return random.choices(population=p, weights=weight, k=len(p))


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

width  = len(colors)

for c in range(len(colors)):
    for i in range(10):
        p.append(c)

for s in range(len(measurements)):
    print("sense ",measurements[s])
    p = sense(p,measurements[s])
    print(p)
    print("move ", motions[s])
    p = move(p,motions[s])
    print(p)


