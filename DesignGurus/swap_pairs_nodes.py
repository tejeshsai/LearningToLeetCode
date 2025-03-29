# Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Problem Description:
# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes 
# (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Time Complexity: O(n) where n is the number of nodes
# Space Complexity: O(1) as we only use a constant amount of extra space

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle the head of the list
        dummy = ListNode(-1)
        dummy.next = head

        # Keep track of the previous node for linking
        previous = dummy

        # Continue while we have at least two nodes to swap
        while head and head.next:
            # Store the two nodes to be swapped
            firstNode = head
            secondNode = head.next

            # Perform the swap
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            previous.next = secondNode

            # Move to the next pair
            head = firstNode.next
            previous = firstNode
            
        return dummy.next