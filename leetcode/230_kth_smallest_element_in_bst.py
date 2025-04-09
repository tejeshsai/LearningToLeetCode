# Kth Smallest Element in BST
# LeetCode Problem #230: Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Problem Description:
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Time Complexity: O(H + k) where H is the height of the tree
# Space Complexity: O(H) for the recursion stack

class Solution:
    def __init__(self):
        self.result = None
        self.count = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder(root, k)
        return self.result
    
    def inorder(self, root, k):
        if root is None or self.count >= k:
            return
        
        # Traverse left subtree
        self.inorder(root.left, k)
        
        # Process current node
        self.count += 1
        if self.count == k:
            self.result = root.val
            return
        
        # Traverse right subtree
        self.inorder(root.right, k) 