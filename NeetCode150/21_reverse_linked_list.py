# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Problem Description:
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Time Complexity: O(n) - we need to traverse the entire list once
# Space Complexity: O(1) - we only use a constant amount of extra space

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize prev as None (will be the new tail)
        # Initialize current as head (will traverse the list)
        prev, current = None, head
        
        # Continue until we reach the end of the list
        while current is not None:
            # Store the next node before we change current.next
            next = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move prev and current one step forward
            prev = current
            current = next
            
        # Return prev which is now the new head
        return prev