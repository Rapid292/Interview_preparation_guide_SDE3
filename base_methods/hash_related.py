class Solution:
    @staticmethod
    def prepare_hash(word):
        char_hash = {}
        for c in word:
            char_hash[c] = char_hash.get(c, 0) + 1
        return char_hash

    @staticmethod
    def compare_dicts(dict1, dict2):

        # Option 1: Using built-in method:
        return dict1 == dict2

        # Option 2: Using custom method:

        # Step 1: Early exit if keys are different
        if dict1.keys() != dict2.keys():
            return False

        # Step 2: Compare values for each key
        for key in dict1:
            if dict1[key] != dict2[key]:
                return False

        return True


# Check using `if complement in num_map:`:
# - Time Complexity: O(1) (constant time) due to dictionary hash lookup.
# - This is more readable and directly checks for the presence of the key.
# - Preferred unless you need to handle specific cases where the value might be None.

# Check using `if num_map.get(complement) != None:`:
# - Time Complexity: O(1), also uses hash lookup.
# - `.get()` allows a default return value (None), but if `None` is stored as a value, this check might give incorrect results.
# - Use `if num_map.get(complement) is not None:` to handle cases where None could be a stored value.

# Recommendation: Use `if complement in num_map:` for better readability unless handling None values is required.
