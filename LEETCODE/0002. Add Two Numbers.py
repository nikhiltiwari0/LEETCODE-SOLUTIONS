# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        """

        # Logic, I want to go through each list, reverse it, and then add them, and then add the last digit to a new list, then output it.

        num_one = 0
        tens = 1
        while l1: # O(n)
            l1.val*=tens
            tens*=10
            num_one+=l1.val
            l1 = l1.next

        num_two = 0
        tens = 1
        while l2: # O(n)
            l2.val*=tens
            tens*=10
            num_two+=l2.val
            l2 = l2.next
        
        num_ans = num_one+num_two

        digit = num_ans%10
        num_ans//=10

        new_num = ListNode(0)
        dummy = new_num

        while num_ans > 0: 
            digit = num_ans%10
            new_num.next = ListNode(digit)
            num_ans//=10
        

        return dummy.next
        

        # Time complexity: O(n)
        # Space complexity: O(1)