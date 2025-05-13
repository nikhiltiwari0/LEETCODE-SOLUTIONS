from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        You are given an integer array nums. 
        You are initially positioned at the array's first index, 
        and each element in the array represents your maximum jump length at that position.
        Return true if you can reach the last index, or false otherwise.
        """
        # Time complexity: O(2^n)
        # Space complexity: O(n)

        # target = len(nums) - 1
        # left = 0


        # def jump(left):
        #     if left > target:
        #         return

        #     if left == target:
        #         return True
            
        #     for num in range(1, nums[left]+1):
        #         if jump(left + num):   
        #             return True
        #     return False

        # return jump(left)



        # Optimal Solution: O(n), O(1)
        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0