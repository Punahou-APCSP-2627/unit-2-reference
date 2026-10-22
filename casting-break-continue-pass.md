# Python Concepts: Type Casting, `break`, `continue`, and `pass`

## 1. Type Casting Input

By default, the `input()` function in Python treats all user input as a string (`str`), regardless of what is typed. To perform mathematical or logical operations, you must convert (cast) the string into another data type using built-in functions such as `int()`, `float()`, or `bool()`.

> **Note on Boolean Casting:** Passing a non-empty string like `"False"` to `bool()` returns `True` because any non-empty string evaluates to `True`. To parse string literals like `"True"` or `"False"`, compare the input string directly or use `ast.literal_eval()`.

### Code Example

```python
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
user_input = user_input.strip() == "True"
print(f"Now, {user_input} is a {type(user_input)}")
```

### Practice #1: Type Casting
> Write a Python program that asks the user for their age using input(), converts the response to an integer, and prints how old they will be next year.

---

## 2. Loop Control: `break` and `continue`

### The `break` Statement

A `while` loop checks its condition before executing the loop body. To execute a loop body at least once before checking a condition (similar to a `do-while` loop in other languages), Python uses infinite loops (`while True`) combined with the `break` keyword.

* **`break`:** Immediately terminates the loop execution completely and jumps to the code following the loop.

#### Code Example

```python
total = 0

while True:
    user_input = int(input("Enter a number, or 0 to quit: "))
    if user_input == 0:
        break
    else:
        total += user_input

print(f"Final Total: {total}")
```

### Practice #2a: Break
> Write a while loop that continuously prompts the user to enter words and prints them back, but immediately exits the loop if the user types "quit".

### The `continue` Statement

One "iteration" of a loop is a single, top-to-bottom execution of the body of code for that loop. Sometimes, we want to _skip_ an iteration of a loop if certain conditions are met. We can achieve the skip using Python's `continue` keyword.

* **`continue`:** Skips the rest of the current loop iteration and returns directly to the loop condition evaluation for the next iteration.

#### Code Example

```python
total = 0

while True:
    user_input = int(input("Enter a positive number to add to total (0 to quit, negative numbers ignored): "))
    
    if user_input == 0:
        break
        
    if user_input < 0:
        print("Negative numbers are ignored! Skipping...")
        continue
        
    total += user_input
    print(f"Current total: {total}")

print(f"Final Total: {total}")
```

### Practice #2b: Continue
> Write a while loop iterating through numbers 1 to 10 that prints each number, but uses continue to skip printing any even numbers.
---

## 3. The `pass` Statement

Python raises a **SyntaxError** if code blocks (such as `if` statements or functions) are completely empty.

* **`pass`:** Acts as a placeholder ("do nothing") statement to keep Python syntax valid while drafting code or explicitly handling conditional branches without executing any actions.

### Scenario A: Placeholder While Drafting Code

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
        pass
    elif guess > secret_number:
        # TODO: Add "Too high!" message later
        pass
```

### Scenario B: Explicitly Doing Nothing

```python
print("SCENARIO B: DO NOTHING HERE")

score = 0

while score < 3:
    action = input("Type 'score' to gain a point, or 'rest' to take a break: ")
    
    if action == "score":
        score += 1
        print(f"Current score: {score}")
    elif action == "rest":
        pass
    else:
        print("Unknown command, try again.")
```

### Practice #3: Pass
> Write an if-elif-else statement checking a variable temperature, where the elif branch for temperature == 20 contains only a pass placeholder for future code.
