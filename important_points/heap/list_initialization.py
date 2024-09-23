"""
### Note on List Initialization in Python

When initializing a list of lists in Python, it's important to ensure that each inner list is a separate list object.
Otherwise, you might inadvertently create a list where all inner lists are references to the same object,
leading to unintended side effects.

#### Correct Initialization
To create a list of independent empty lists:

freq_list = [[] for _ in range(len(nums) + 1)]

#### Possible Mistake
Avoid creating a list of references to the same list object:

```python
# Incorrect approach: This creates a list of references to the same empty list.
freq_list = [[]] * (len(nums) + 1)
```

### Example

#### Correct Initialization

```python
# Correct method initializing independent lists
len_nums = 5
freq_list = [[] for _ in range(len_nums + 1)]

# Modifying one inner list does not affect others
freq_list[2].append('A')
print(freq_list)  # Output: [[], [], ['A'], [], [], []]
```

#### Possible Mistake

```python
# Incorrect method creating references to the same list
len_nums = 5
freq_list = [[]] * (len_nums + 1)

# Modifying one inner list affects all of them
freq_list[2].append('A')
print(freq_list)  # Output: [['A'], ['A'], ['A'], ['A'], ['A'], ['A']]
```

### Conclusion

Always use list comprehensions or explicit loops to initialize lists of independent lists in Python. Avoid using list multiplication on lists containing mutable objects, as this will create references to the same object rather than distinct objects.
"""