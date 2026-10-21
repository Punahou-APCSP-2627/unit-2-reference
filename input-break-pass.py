
'''
input() automatically assumes that whatever the user enters is a string.
You can see this by using the type() function. 
You can turn that string into a corresponding int or bool.
'''

print("\nSTRING --> INTEGER")

user_input = input("Type a number: ")
print(f"Originally, {user_input} is a {type(user_input)}")
print("\nConverting...")
user_input = int(user_input)
print(f"Now, {user_input} is a {type(user_input)}")

print("\nSTRING --> BOOLEAN")

user_input = input("Type True or False, with correct capitalization: ")
print(f"Originally, {user_input} is a {type(user_input)}")
print("\nConverting...")
ser_input = eval(user_input)
print(f"Now, {user_input} is a {type(user_input)}")

'''
A while loop always checks the loop condition before executing
the code within the loop body. Sometimes, we want to execute the
loop body at least once before even checking the condition.

Other languages use do-while loops to accomplish this.
Python uses inifinite loops (aka forever loops) and break.

The break keyword forces the loop to end immediately when a condition is met,
regardless of what the while condition says.

EXAMPLE: Write a program that asks users to enter numbers and keeps a 
running total of all numbers entered. The loop should stop running when 
the user enters 0. Afterwards, print the final sum.
'''

# declare running total variable and initialize to zero
# forever/infinite loop:
    # ask for input and store it in a variable user_input
    # if input is zero, break out of loop
    # otherwise, add to running total
# print total

total = 0

while True:
    user_input = int(input("Enter a number, or 0 to quit: "))
    if user_input == 0:
        break
    else:
        total += user_input

print(total)



'''
Python throws a syntax error if a code block, like the body of an if-statement
or a loop, is completely empty.

However, it can be userful to leave an empty block while you draft your code,
or if you want to explicitly say "do nothing here."

The pass keyword allows us to leave empty blocks without errors.
'''

print("SCENARIO A: PLACEHOLDER while drafting a guessing game")

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number (1-10): "))
    
    if guess == secret_number:
        print("You got it!")
    elif guess < secret_number:
        # TODO: Add "Too low!" message later
        pass  # Placeholder
    elif guess > secret_number:
        # TODO: Add "Too high!" message later
        pass  # Placeholder

print("SCENARIO B: DO NOTHING HERE")

score = 0

while score < 3:
    action = input("Type 'score' to gain a point, or 'rest' to take a break: ")
    
    if action == "score":
        score += 1
        print(f"Current score: {score}")
    elif action == "rest":
        pass  # We acknowledge the rest command, but no score change happens!
    else:
        print("Unknown command, try again.")