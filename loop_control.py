import py5

def settings():
    py5.size(400, 300)

def setup():
    pass

def draw():
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
        # Step 1: Building construction logic by city zone
        if x >= 150 and x <= 210:
            pass  # Public park zone: intentionally leave this lot open
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
            
        # Step 2: Shared city infrastructure (runs for EVERY lot)
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


'''
# Part A: Standard String Input
user_name = input("Enter your name: ")
print("Hello,", user_name)
print("Type of user_name:", type(user_name))
print("-" * 30)

# Part B: Type Casting to Integer
raw_age = input("Enter your age in whole years: ")
print("raw_age value:", raw_age)
print("raw_age type before conversion:", type(raw_age))

# Convert string to integer
age = int(raw_age)
print("age value after conversion:", age)
print("age type after conversion:", type(age))
print("Next year you will be:", age + 1)
print("-" * 30)

# Part C: The Boolean Gotcha vs. eval()
flag_input = input("Type the word False exactly: ")

# Method 1: Using standard bool()
bad_bool = bool(flag_input)
print("Using bool(flag_input):", bad_bool)
print("Type of bad_bool:", type(bad_bool))

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
