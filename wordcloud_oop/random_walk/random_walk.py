import random 

def random_walk(n):
    '''Return coordinates after 'n' block random walk.'''
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x,y)


for i in range(25):
      walk = random_walk(10)
      print(walk, "Distance from home = ",
              abs(walk[0]) + abs(walk[1]))



def random_walk2(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)


for i in range(25):
    walk = random_walk_2(10)
    print(walk, "Distance from home = ",
            abs(walk[0]) + abs(walk[1]))