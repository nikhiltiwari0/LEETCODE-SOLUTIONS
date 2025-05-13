class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, return true if x is a palindrome, and false otherwise.
        """

        # reverse_num = 0
        # copy_x = x

        # while x > 0: # Time complexity: O(n)
        #     reverse_num *= 10
        #     reverse_num += x%10
        #     x//=10
        
        # return reverse_num == copy_x


        """
        Will try to get a better solution below, will try for O(n/2) which is still O(n), but faster
        """


        