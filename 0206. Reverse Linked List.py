# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, reverse the list, and return the reversed list.
        """


        new_list = None


        while head:
            new_node = head.next
            head.next = new_list
            new_list = head
            head = new_node
        
        return new_list