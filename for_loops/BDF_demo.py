'''
Rules of thumb:
1. When you know (or can easily calculate) exactly how many times the loop should run, use some version of a for loop.
2. If you don't know how long/how many times the loop will have to run, use a while loop.
3. If you specifically need to obtain and validate input (or validate random selection), use a forever loop (while True) with a break statement.

Of course, there can be exceptions to these rules in certain situations, but they're a good place to start.
'''

import py5

def settings():
    py5.size(400, 400)

def setup():
    pass

def draw():

    # direct WHILE, y = 100
    py5.fill("#e76b64")
    x = 20
    while x < py5.width:
        py5.circle(x, 100, 20)
        x += 40

    # indirect WHILE, y = 150
    count = 0
    py5.fill("#f1bd2d")
    while count < 10:
        py5.circle(count * 40 + 20, 150, 20)
        count += 1
    
    # indirect FOR, y = 200
    py5.fill("#049630")
    for circle_num in range(10):
        print(circle_num, circle_num * 40 + 20)
        py5.circle(circle_num * 40 + 20, 200, 20)

    # direct FOR, y = 250
    py5.fill("#327DB6")
    for x_pos in range(20, py5.width, 40): # range(start, stop, step)
        py5.circle(x_pos, 250, 20)

    # just for kicks, decreasing the loop var, y = 300
    py5.fill("#a80ea8")
    for x_pos in range(380, 0, -40):
        py5.circle(x_pos, 300, 20)


py5.run_sketch()
