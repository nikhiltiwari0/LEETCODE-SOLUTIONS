from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums of unique elements, return all possible subsets (the power set).
        The solution set must not contain duplicate subsets. Return the solution in any order.
        """

        res = []
        subset = []

        def create_subset(i):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            create_subset(i+1)
            subset.pop()

            create_subset(i+1)

        create_subset(0)
        return res