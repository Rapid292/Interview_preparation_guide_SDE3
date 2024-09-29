class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Example:
        # s = "abcabcbb"
        # Output: 3
        # Explanation: The answer is "abc", with the length of 3.

        # s = "bbbbb"
        # Output: 1
        # Explanation: The answer is "b", with the length of 1.

        l = 0
        charset = set()
        res = 0

        for r, char in enumerate(s):
            while char in charset:
                charset.remove(s[l])
                l += 1
            charset.add(char)
            res = max(res, (r-l+1))
        return res
