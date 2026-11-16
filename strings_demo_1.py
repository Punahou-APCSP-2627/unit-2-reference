# A string is text wrapped in single or double quotes.
# Every character (a.k.a. char) has an index starting at 0.

sentence = "Questions, comments, concerns, or dad jokes?"

# String slicing: string[start:stop:step]
# Note: 'start' is inclusive, 'stop' is exclusive!
first_word = sentence[0:9]
last_word = sentence[37:43]
last_char_by_index = sentence[-1]
backwards = sentence[::-1]

# You can obtain the number of letters in a string using len()
num_chars = len(sentence)
last_char_by_len = sentence[len(sentence) - 1]


''''''''''''''''''''''''''''''''''''''''''

print()
print()
print("Original:", sentence)
print("Slice [0:9]:", first_word)
print("Slice [37:43]:", last_word)
print("Last char [-1]:", last_char_by_index)
print("Last char len(sentence) - 1: ", last_char_by_len)
print("Backwards:", backwards)
print()

''''''''''''''''''''''''''''''''''''''''''

# Review: Printing with strings

''' Method 1: String concatenation using the + operator
# Note that Python won't let you combine a string and a number directly,
# so concatenation often requires use of str() '''

jokes = 3
simple_msg = "Hello" + " " + "world."
concat_msg = "Any questions? Current dad joke count:" + str(jokes) + "!" # str(3) --> "3"
print(concat_msg)

''' Method 2: Separate with commas in print() statement
Note: Only works inside print(). Cannot be use to save a 
formatted string into a variable for later 
Note: Forced added spaces around the variable'''

print("Any questions? Current dad joke count:", jokes, "!")



''' Method 3: f-string formatting
Put an 'f' before the quotes to inject variables directly inside {curly braces} '''

print("Any questions? Current dad joke count: {jokes}!")
formatted_msg = f"Any questions? Current dad joke count: {jokes}!"
print(formatted_msg)