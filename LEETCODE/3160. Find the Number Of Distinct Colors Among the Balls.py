from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        """
        You are given an integer limit and a 2D array queries of size n x 2.

        There are limit + 1 balls with distinct labels in the range [0, limit]. 
        Initially, all balls are uncolored. For every query in queries that is of the form [x, y], 
        you mark ball x with the color y. After each query, you need to find the number of distinct 
        colors among the balls.

        Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

        Note that when answering a query, lack of a color will not be considered as a color.
        """

        res = [-1] * limit
        
        

