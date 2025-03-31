# Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Problem Description:
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Explanation: The longest path is 3 -> 20 -> 7 with length 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2
# Explanation: The longest path is 1 -> 2 with length 2

# Time Complexity: O(n) where n is the number of nodes
# Space Complexity: O(h) where h is the height of the tree (recursion stack)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if root is None, depth is 0
        if root is None:
            return 0
            
        # Recursively calculate depth of left and right subtrees
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        # Return the larger depth plus 1 (for the current node)
        return 1 + max(leftDepth, rightDepth)

if __name__ == "__main__":
    # Test Case 1: Regular tree with depth 3
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
    
    # Test Case 2: Skewed tree (all nodes to the right)
    #   1
    #    \
    #     2
    #      \
    #       3
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    root2.right.right = TreeNode(3)
    
    # Test Case 3: Empty tree
    root3 = None
    
    # Test Case 4: Single node tree
    root4 = TreeNode(1)
    
    solution = Solution()
    
    # Run test cases
    print("Test Case 1 - Regular tree:")
    print("Expected: 3")
    print("Actual:", solution.maxDepth(root1))
    print()
    
    print("Test Case 2 - Skewed tree:")
    print("Expected: 3")
    print("Actual:", solution.maxDepth(root2))
    print()
    
    print("Test Case 3 - Empty tree:")
    print("Expected: 0")
    print("Actual:", solution.maxDepth(root3))
    print()
    
    print("Test Case 4 - Single node tree:")
    print("Expected: 1")
    print("Actual:", solution.maxDepth(root4))