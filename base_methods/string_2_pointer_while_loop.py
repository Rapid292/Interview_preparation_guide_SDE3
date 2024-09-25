import re

class Solution:
    @staticmethod
    def remove_non_alphanumeric(input_string):
        return re.sub(r'[^a-zA-Z0-9]', '', input_string)

    def isPalindrome(self, s: str) -> bool:
        s = Solution.remove_non_alphanumeric(s)
        s = s.strip().lower()
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True