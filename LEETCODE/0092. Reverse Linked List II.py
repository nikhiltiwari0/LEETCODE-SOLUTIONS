# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Given the head of a singly linked list and two integers left and right where left <= right, 
        reverse the nodes of the list from position left to position right, and return the reversed list.
        """

        # Time complexity: O(n), space complexity: O(1)

        new_list = ListNode(0, head)
        prev = new_list

        for _ in range(left-1):
            prev = prev.next
        
        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev = temp
        
        return new_list.next