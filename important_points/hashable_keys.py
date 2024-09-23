# Dictionary keys in Python must be immutable and hashable.
# This ensures the keys' hash values remain constant, allowing for reliable value retrieval.

# Mutable types such as lists, dictionaries, and sets cannot be used as dictionary keys
# because:
# 1. Immutability: Mutable objects can change, which would alter their hash value.
# 2. Hashability: An object is hashable if it has a consistent __hash__ method and
#    can be compared to other objects using a __eq__ method.

# Examples of mutable, non-hashable types:
# - Lists
# - Dictionaries
# - Sets

# Valid dictionary keys are immutable and hashable types like:
# - Strings
# - Numbers
# - Tuples (if they contain only immutable objects)

# Example demonstrating why certain types cannot be used as dictionary keys:

# Lists are mutable and unhashable
my_list = [1, 2, 3]
try:
    my_dict = {my_list: "value"}  # Raises TypeError
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: unhashable type: 'list'

# Tuples are immutable and hashable
my_tuple = (1, 2, 3)
try:
    my_dict = {my_tuple: "value"}  # Valid key
    print(my_dict)  # Output: {(1, 2, 3): 'value'}
except TypeError as e:
    print(f"Error: {e}")

# Conclusion:
# Use immutable and hashable types like strings, numbers, and tuples (containing immutable elements)
# as dictionary keys to ensure consistency and reliability in Python dictionaries.