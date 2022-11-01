import random

colors = ['red', 'green', 'green', 'red' , 'red']

#measurements = ['green']                                       # test 1
measurements = ['green', 'green', 'green' ,'green', 'green']   # test 2

sensor_right = {}
sensor_right['green'] = 0.6     # P(Gm | Gc)
sensor_right['red'] = 0.8       # P(Rm | Rc)

def sense(p, Z):
    """Update belief array p according to new measurement Z"""

    weight = []

    for i in range(len(p)):
        if colors[p[i]] == 'red':
            weight.append(sensor_right['red'] if Z == 'red' else 1 - sensor_right['red'])
        else:
            weight.append(sensor_right['green'] if Z == 'green' else 1 - sensor_right['green'])

    return random.choices(population=p, weights=weight, k=len(p))

#main
p = []

width  = len(colors)
n = width

for c in range(len(colors)):
    for i in range(10):
        p.append(c)

for s in range(len(measurements)):
    p = sense(p,measurements[s])
    print(p)
