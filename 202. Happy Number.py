class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Write an algorithm to determine if a number n is happy.

        A happy number is a number defined by the following process:

            - Starting with any positive integer, replace the number by the sum of the squares of its digits.
            - Repeat the process until the number equals 1 (where it will stay), 
            or it loops endlessly in a cycle which does not include 1.
            - Those numbers for which this process ends in 1 are happy.
        Return true if n is a happy number, and false if not.
        """

        seen = set()
        curr = n

        while curr not in seen:
            seen.add(curr)
            if curr == 1:
                return True
            new_cur = 0
            while curr >0:
                new_cur += (curr%10) ** 2
                curr//=10

            curr = new_cur

        return False