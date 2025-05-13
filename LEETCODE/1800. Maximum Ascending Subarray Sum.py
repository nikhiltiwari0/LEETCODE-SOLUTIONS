from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
        A subarray is defined as a contiguous sequence of numbers in an array.
        A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. 
        Note that a subarray of size 1 is ascending.
        """

        max_sum = nums[0] # [10,20,30,5,10,50]
        # max = 10
        current = max_sum
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]: # 10 > 20 False
                current = nums[i]
            else: # current = 30
                current+=nums[i]
                max_sum = max(max_sum, current)
        
        return max_sum