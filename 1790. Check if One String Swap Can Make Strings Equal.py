class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        You are given two strings s1 and s2 of equal length. 
        A string swap is an operation where you choose two indices in a string 
        (not necessarily different) and swap the characters at these indices.
        Return true if it is possible to make both strings equal by performing 
        at most one string swap on exactly one of the strings. Otherwise, return false.
        """
        # This is O(4n) time complexity, O(n) space complexity, there is a way to do it in better time and space.
        missing_counter = 0

        chars_one = {}
        for c in s1:
            if c not in chars_one:
                chars_one[c] = 1
            else:
                chars_one[c] +=1

        chars_two = {}
        for c in s2:
            if c not in chars_two:
                chars_two[c] = 1
            else:
                chars_two[c] +=1
        
        for c in range(len(s1)):
            if s1[c] != s2[c]:
                missing_counter+=1
            if missing_counter > 2:
                return False
        
        return missing_counter == 0 or missing_counter == 2 and chars_one == chars_two
    

        """
        i=-1
        j=-1
        cnt=0
        for k in range(0, len(s1)):
            if s1[k]!=s2[k]:
                cnt+=1
                if i==-1: i=k
                elif j==-1: j=k
        
        if cnt==0: return True
        elif cnt==2 and s1[i]==s2[j] and s1[j]==s2[i]: return True

        return False
        """