import py5

ACTIVE_ACTIVITY = 3


def setup():
    pass

def settings():
    py5.size(400, 400)


def draw():
    # ==========================================================================
    # ACTIVITY 1
    # ==========================================================================
    if ACTIVE_ACTIVITY == 1:
        py5.background(240)
    
    # Red boundary line
    py5.stroke(220, 50, 50)
    py5.stroke_weight(3)
    py5.line(200, 0, 200, 300)
    
    # Loop to draw shapes across the screen
    py5.stroke(0)
    py5.stroke_weight(1)
    py5.fill(70, 130, 240)
    
    x = 40
    while x < 360:
        if x >= 200:
            break
        py5.circle(x, 150, 30)
        x = x + 40

    # ==========================================================================
    # ACTIVITY 2
    # ==========================================================================
    if ACTIVE_ACTIVITY == 2:
        # Dark green radar background
        py5.background(10, 25, 18)
        
        # Glowing radar crosshairs
        py5.stroke(20, 60, 40)
        py5.stroke_weight(1)
        py5.line(200, 0, 200, 400)
        py5.line(0, 200, 400, 200)
        
        # Center transmitter blip
        py5.fill(0, 255, 140)
        py5.no_stroke()
        py5.circle(200, 200, 8)
        
        # Radar pulse rings
        py5.no_fill()
        py5.stroke(0, 255, 140)
        py5.stroke_weight(2)
        
        ring_size = 0
        while ring_size < 320:
            ring_size = ring_size + 40
            if ring_size == 160:
                continue
            py5.circle(200, 200, ring_size)

    # ==========================================================================
    # ACTIVITY 3
    # ==========================================================================
    elif ACTIVE_ACTIVITY == 3:
        
        # Night sky
        py5.background(20, 24, 38)
        
        # Moon
        py5.no_stroke()
        py5.fill(255, 245, 200)
        py5.circle(340, 60, 40)
        
        # Groundd
        py5.fill(40, 45, 55)
        py5.rect(0, 250, 400, 50)
        
        # City lot loop
        x = 30
        while x < 370:
            
            # Building construction logic by city zone
            if x >= 150 and x <= 210:
                pass  # Public park zone: intentionally leave this lot empty
                
            elif x > 210:
                # Commercial zone: tall modern skyscraper
                py5.fill(60, 110, 170)
                py5.stroke(100, 180, 240)
                py5.stroke_weight(2)
                py5.rect(x, 90, 30, 160)
            
            else:
                # Residential zone: low-rise apartment
                py5.fill(95, 80, 120)
                py5.stroke(140, 125, 170)
                py5.stroke_weight(2)
                py5.rect(x, 160, 30, 90)
                
            #Shared city infrastructure (runs for EVERY lot)
            # Streetlamp post
            py5.stroke(180)
            py5.stroke_weight(2)
            py5.line(x + 15, 230, x + 15, 250)
            # Glowing streetlamp light
            py5.no_stroke()
            py5.fill(255, 230, 100)
            py5.circle(x + 15, 230, 6)
            
            x = x + 40

py5.run_sketch()

# ==========================================================================
# ACTIVITY 4
# ==========================================================================

'''
# Part A: Standard String Input
user_name = input("Enter your name: ")
print("Hello,", user_name)
print("Type of user_name:", type(user_name))
print("\n" + "-" * 30+ "\n")

# Part B: Type Casting to Integer
raw_age = input("Enter your age in whole years: ")
print("raw_age value:", raw_age)
print("raw_age type before conversion:", type(raw_age))

# Convert string to integer
age = int(raw_age)
print("age value after conversion:", age)
print("age type after conversion:", type(age))
print("Next year you will be:", age + 1)
print("\n" + "-" * 30+ "\n")

# Part C: The Boolean Gotcha vs. eval()
flag_input = input("Type the word False exactly: ")

# Method 1: Using standard bool()
bad_bool = bool(flag_input)
print("Using bool(flag_input):", bad_bool)
print("Type of bad_bool:", type(bad_bool))

print("\n")

# Method 2: Using eval() to interpret the string literal
real_bool = eval(flag_input)
print("Using eval(flag_input):", real_bool)
print("Type of real_bool:", type(real_bool))

# Testing in a conditional
if real_bool:
    print("Condition evaluated to TRUE.")
else:
    print("Condition evaluated to FALSE.")
'''
