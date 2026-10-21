# Python Concepts: `input()`, type casting, `break`, and `pass`

---

## 1. Type Casting Input

By default, the `input()` function in Python treats all user input as a string (`str`), regardless of what is typed. To perform mathematical or logical operations, you must convert (cast) the string into another data type using built-in functions like `int()` or `eval()`.

```python
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
user_input = eval(user_input)
print(f"Now, {user_input} is a {type(user_input)}")
```

---

## 2. Using Infinite Loops and `break`

A `while` loop checks its condition before executing the loop body. To execute a loop body at least once before checking a condition (similar to a `do-while` loop in other programming languages), Python relies on **infinite loops** (`while True`) combined with the **`break`** keyword.

> **`break` Keyword:** Immediately terminates the current loop, skipping any remaining code inside the loop block regardless of the loop condition.

### Pseudocode & Implementation Example

* **Goal:** Ask the user to enter numbers, keeping a running total until they enter `0`.

```python
# Pseudocode:
# 1. Declare running total variable and initialize to zero
# 2. Forever/infinite loop:
#     a. Ask for input and store it in user_input
#     b. If input is zero, break out of loop
#     c. Otherwise, add input to running total
# 3. Print total

total = 0

while True:
    user_input = int(input("Enter a number, or 0 to quit: "))
    if user_input == 0:
        break
    else:
        total += user_input

print(total)
```

---

## 3. The `pass` Statement

Python raises a **SyntaxError** if code blocks (such as `if` statements, functions, or loops) are left completely empty.

> **`pass` Keyword:** Acts as a placeholder ("do nothing") statement to keep Python syntax valid while drafting code or explicitly handling conditional branches without executing any actions.

### Scenario A: Placeholder While Drafting Code

Use `pass` as a temporary placeholder while designing logic flow.

```python
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
```

### Scenario B: Explicitly Doing Nothing

Use `pass` when a specific condition is valid and recognized, but no code needs to run.

```python
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
```
