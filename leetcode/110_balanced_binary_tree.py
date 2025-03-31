# Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Problem Description:
# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees 
# of every node differ in height by no more than 1.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Explanation: The left and right subtrees of every node differ in height by no more than 1.

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Explanation: The left and right subtrees of node 2 differ in height by 2.

# Time Complexity: O(n) where n is the number of nodes
# Space Complexity: O(h) where h is the height of the tree (recursion stack)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, root: TreeNode) -> int:
        # Base case: if root is None, height is 0
        if root is None:
            return 0
        
        # Get heights of left and right subtrees
        leftDepth = self.traverse(root.left)
        if leftDepth == -1:  # Left subtree is not balanced
            return -1
            
        rightDepth = self.traverse(root.right)
        if rightDepth == -1:  # Right subtree is not balanced
            return -1
            
        # Check if current node is balanced
        if abs(leftDepth - rightDepth) > 1:  # Height difference > 1 means not balanced
            return -1
            
        # Return height of current node
        return 1 + max(leftDepth, rightDepth)
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.traverse(root) != -1

if __name__ == "__main__":
    # Test Case 1: Balanced tree
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    # Test Case 2: Unbalanced tree
    #     1
    #    / \
    #   2   2
    #  / \
    # 3   3
    #    /
    #   4
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.right.left = TreeNode(4)
    
    solution = Solution()
    
    # Run test cases
    print("Test Case 1 - Balanced tree:")
    print("Expected: True")
    print("Actual:", solution.isBalanced(root1))
    print()
    
    print("Test Case 2 - Unbalanced tree:")
    print("Expected: False")
    print("Actual:", solution.isBalanced(root2))