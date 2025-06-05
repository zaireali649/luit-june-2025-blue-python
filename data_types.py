# Integers: basic arithmetic
first_pokemon_number = 151  # Mew
second_pokemon_number = 251  # Celebi

# Subtracting two integers → result is also an integer
print(second_pokemon_number - first_pokemon_number)  # Output: 100

# Strings that look like numbers
string_number_one = "386"  # Deoxys
string_number_two = "493"  # Arceus

# String concatenation: just joins the text
print(string_number_one + string_number_two)  # Output: '386493'

# Converting strings to integers and then adding them
print(int(string_number_one) + int(string_number_two))  # Output: 879

# Checking the type of a string
print(type(string_number_one))  # Output: <class 'str'>

# More integer division
dividend = 9
divisor = 3
division_result = dividend / divisor  # Division always returns a float in Python 3

print(division_result)  # Output: 3.0

# Print the types: dividend and divisor are int, result is float
print(type(divisor), type(dividend), type(division_result))  # Output: <class 'int'> <class 'int'> <class 'float'>

# Convert float back to int (truncates decimal)
truncated_result = int(division_result)

print(truncated_result)  # Output: 3

# String with alphabetic words instead of numeric digits
words_as_numbers = "six four nine" # Genesect

# Check the data type
print(type(words_as_numbers))  # Output: <class 'str'>

# Show available string methods
print(dir(words_as_numbers))

# Demonstrate string methods
print(words_as_numbers.capitalize())  # Capitalize first letter: 'Six four nine'
print(words_as_numbers.upper())       # All uppercase: 'SIX FOUR NINE'
print(words_as_numbers.title())       # Title case: 'Six Four Nine'

# Check if string is alphanumeric (no spaces or symbols)
print(words_as_numbers.isalnum())     # False: contains spaces
print(string_number_one.isalnum())    # True: only digits
