'''
Rules of thumb:
1. When you know (or can easily calculate) exactly how many times the loop should run, use some version of a for loop.
2. If you don't know how long/how many times the loop will have to run, use a while loop.
3. If you specifically need to obtain and validate input (or validate random selection), use a forever loop (while True) with a break statement.

Of course, there can be exceptions to these rules in certain situations, but they're a good place to start.
'''

# STRATEGY 1: VISUAL EDGE DETECTION (while condition)
# Core Idea: Keep drawing as long as the shape is inside the canvas boundary.

x = 40  # 1. Initial State: Starting position

while x < width:  # 2. Condition: Canvas boundary check
  
    circle(x, 200, 20)  # Draw shape
    x += 40  # 3. Step Update: Move right by 40px

# INFINITE LOOP WARNING:
# Omit `x += 40` and x stays 40 forever, creating an infinite loop!

# ================================================================================

# STRATEGY 2: SPATIAL GRID STEPPING (for loop using range() with multiple parameters)
# Concept: Step directly across canvas coordinates in fixed pixel increments.


# range(40, width, 40) (called the "sequence")creates the sequence of values (40, 80, 120, ...).
# 'x' (called the "item") is a variable name YOU define to hold the current value in the sequence.

for x in range(40, width, 40):
  
    circle(x, 200, 20)

# ================================================================================

# STRATEGY 3: VISUAL COUNTING (while counter)
# Core Idea: Repeat an action a fixed number of times regardless of pixel positions.

count = 0  # 1. Start counter at 0

while count < 5:  # 2. Repeat exactly 5 times
  
    # Calculate position from count: (count * spacing) + margin
    x_pos = count * 80 + 40
    circle(x_pos, 200, 20)

    count += 1  # 3. Increment counter

# ================================================================================

# STRATEGY 4: ABSTRACT FREQUENCY & INDEXING (for loop using range() with one parameter)
# Concept: Repeat N times using a counting index (0, 1, 2, ... N-1).

# range(10) creates the "sequence" of numbers (0, 1, 2, ..., 9).
# 'i' is the "item" — a variable name you choose to hold the current number.
# By convention, programmers use 'i' for "index" but any name is fine.

for i in range(10):
  
    # Map the current item 'i' to canvas geometry using math:
    x_pos = i * 40 + 20
    radius = (i + 1) * 5

    circle(x_pos, 200, radius)

# ================================================================================

# BONUS: FLOW INTERRUPTION (break & continue)
# Core Idea: Dynamically skip an iteration or exit a loop based on conditions.

for i in range(10):
  
    # CONTINUE: Skip drawing at a specific index (creates a gap)
    if i == 4:
        continue  # Skip to next iteration

    # BREAK: Stop drawing completely when reaching a visual barrier
    if i * 40 > mouse_x:
        break  # Exit loop immediately

    circle(i * 40 + 20, 200, 20)
