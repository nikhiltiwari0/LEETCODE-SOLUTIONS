from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

        Args:
            nums (List[int]): The list of integers.
            target (int): The target sum.

        Returns:
            List[int]: A list containing the indices of the two numbers that add up to the target.
        """
        complements = {}

        for i in range(len(nums)):
            if nums[i] in complements:
                return [i, complements[nums[i]]]
            complements[target - nums[i]] = i
        
        return []  # If no solution is found