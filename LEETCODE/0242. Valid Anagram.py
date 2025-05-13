class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an 
        anagram of s, and false otherwise.
        """

        chars = [0] * 26

        for c in s:
            chars[ord(c)-ord('a')] += 1
        
        for c in t:
            chars[ord(c)-ord('a')] -= 1

        return chars == [0]*26