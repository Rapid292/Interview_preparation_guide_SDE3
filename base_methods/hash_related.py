from collections import Counter

class Solution:
    @staticmethod
    def prepare_hashmap(word):
        char_hashmap = {}
        for c in word:
            char_hashmap[c] = char_hashmap.get(c, 0) + 1
        return char_hashmap

    @staticmethod
    def prepare_hashmap(word):
        # Example: word = "hello"
        # char_count_hashmap = {"h": 1, "e": 1, "l": 2, "o": 1}
        char_count_hashmap = Counter(word)
        return char_count_hashmap

    @staticmethod
    def compare_dicts(dict1, dict2):

        # Using built-in method:
        return dict1 == dict2

# Check using `if complement in num_map:`:
# - Time Complexity: O(1) (constant time) due to dictionary hash lookup.
# - This is more readable and directly checks for the presence of the key.
# - Preferred unless you need to handle specific cases where the value might be None.

# Check using `if num_map.get(complement) != None:`:
# - Time Complexity: O(1), also uses hash lookup.
# - `.get()` allows a default return value (None), but if `None` is stored as a value, this check might give incorrect results.
# - Use `if num_map.get(complement) is not None:` to handle cases where None could be a stored value.

# Recommendation: Use `if complement in num_map:` for better readability unless handling None values is required.
