print("\n\nLOOPING THROUGH A STRING character by character\n")

# Method A: Looping by index (using what you already know about len() and [])
word = "dad jokes"
print("Looping by index:")
for i in range(len(word)):
    print(f"Index {i}: {word[i]}")

# Method B: Looping directly over each character (cleaner when you don't need the index)
# This is a very "Pythonic" style. The for/in keywords allow you to loop through any sequence.
# In the past we've looked at range() sequences, but it works for strings as well.
print("\nLooping directly over characters:\nfor char in word:")
for char in word:
    print(char)

print("\n\nCOMMON STRING METHODS (Search 'Python string methods' online for dozens more!)")
print("Methods use dot notation: variable.method().")
print("Note that string methods are often stacked.")

messy = "   dad jokes are great   "

print("\n--- STRING METHODS ---")
print(f"Original:            '{messy}'")
print(f".strip():            '{messy.strip()}'")     # Removes outer spaces
print(f".upper():            '{messy.strip().upper()}'")    # ALL CAPS
print(f".count('a'):         '{messy.count('a')}'")      # Counts substring occurrences
print(f".strip().replace():  ", messy.strip().replace('great', 'terrible'))


print("\n\nSTRING IMMUTABILITY + SAVING RETURN VALUES")
print("Strings CANNOT be modified in place after creation.")

pet = "cat"
print(f"Original value of pet: {pet}")

# UNCOMMENT THE LINE BELOW TO SEE THE ERROR:
# pet[0] = "b"  # TypeError: 'str' object does not support item assignment

print("\nCommon mistake: Calling a method without saving or printing it loses the result!")
pet.upper()
print("\nAfter pet.upper() without saving:", pet)  # Still "cat"! The "CAT" vanished!

print("\nFix: Capture the new string in a variable (or print it directly)")
loud_pet = pet.upper()
print("Saved in new variable:", loud_pet)          # "CAT"

print("\nTo 'change' a single character, build a NEW string and reassign the variable:")
pet2 = "b" + pet[1:]
print("Reassigned pet:", pet)                      # "bat"