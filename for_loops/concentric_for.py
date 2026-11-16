import py5

def settings():
    py5.size(500, 500)

def setup():
    pass

def draw():
    py5.background(20, 24, 35)
    py5.no_fill()
    py5.stroke_weight(2)
    
    for diameter in range(20, 452, 18):
        # Primary blue ring
        py5.stroke(70, 140, 240)
        py5.circle(250, 250, diameter)
        
        # Accent orange ring
        py5.stroke(255, 170, 50)
        py5.circle(250, 250, diameter - 6)

py5.run_sketch()
