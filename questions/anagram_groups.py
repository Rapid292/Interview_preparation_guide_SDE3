from collections import defaultdict
from typing import List

# Solution 1: Sorting Each Word # time complexity -> O(n*klogk)
class Solution:
    @staticmethod
    def prepare_unique_hash(word):
        # Create a sorted tuple of characters (which is hashable)
        return "".join(sorted(word)) # time complexity -> O(klogk)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        anagrams_hashmap = defaultdict(list)
        for word in strs: # time complexity -> O(n*klogk)
            word_unique_hash = Solution.prepare_unique_hash(word)
            anagrams_hashmap[word_unique_hash].append(word)

        return list(anagrams_hashmap.values())

# Solution 2: Character Count Method: # time complexity -> O(n*k)
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        anagrams_hashmap = defaultdict(list)
        for word in strs: # time complexity -> O(n*k)
            # considering small alphabets only a-z
            count = [0]*26
            for char in word:
                count[ord(char) - ord("a")] += 1

            # make it immutable
            key = tuple(count)
            anagrams_hashmap[key].append(word)

        return list(anagrams_hashmap.values())


