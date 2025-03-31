# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Problem Description:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by 
# splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Time Complexity: O(n + m) where n and m are lengths of input lists
# Space Complexity: O(1) as we only use a constant amount of extra space

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle the head of merged list
        current_head = ListNode(-1)
        current = current_head

        # Compare and merge nodes from both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes from either list
        current.next = list1 or list2
        return current_head.next
        
        
        