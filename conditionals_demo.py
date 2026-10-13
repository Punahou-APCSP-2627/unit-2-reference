import py5

def setup():
    py5.size(400, 200)

def draw():
    py5.background(240)
    
    # Visual threshold dividing the screen in half
    py5.stroke(180)
    py5.line(200, 0, 200, py5.height)
    
    # Selection: Respond dynamically to cursor location
    if py5.mouse_x < 200:
        py5.fill(70, 130, 240)    # Blue for left half
        label = "LEFT ZONE"
    else:
        py5.fill(240, 90, 70)     # Red for right half
        label = "RIGHT ZONE"
        
    py5.circle(py5.mouse_x, py5.mouse_y, 40)
    py5.fill(20)
    py5.text(label, 20, 30)

py5.run_sketch()
