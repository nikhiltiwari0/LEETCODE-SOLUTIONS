class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest 
        substring without repeating characters.
        """
        max_len = 0
        left = 0
        seen = {}

        for right, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            max_len = max(max_len, right - left + 1)
            seen[c] = right
        
        return max_len