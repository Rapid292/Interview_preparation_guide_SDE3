from collections import defaultdict

class Solution:
    @staticmethod
    def prepare_hashmap(word):
        char_hashmap = defaultdict(int)
        for c in word:
            char_hashmap[c] += 1
        return char_hashmap

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char_hashmap = Solution.prepare_hashmap(s)
        t_char_hashmap = Solution.prepare_hashmap(t)
        return s_char_hashmap == t_char_hashmap
