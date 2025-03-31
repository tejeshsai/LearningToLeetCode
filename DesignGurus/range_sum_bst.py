# Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

# Problem Description:
# Given the root node of a binary search tree and two integers low and high, 
# return the sum of values of all nodes with a value in the inclusive range [low, high].

# Example 1:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23

# Time Complexity: O(n) where n is the number of nodes
# Space Complexity: O(h) where h is the height of the tree (recursion stack)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # Base case: if root is None, sum is 0
        if root is None:
            return 0
        
        # If current node's value is less than low, only check right subtree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
            
        # If current node's value is greater than high, only check left subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
            
        # Current node's value is in range, add it and check both subtrees
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

if __name__ == "__main__":
    # Test Case 1:
    #     10
    #    /  \
    #   5    15
    #  / \     \
    # 3   7     18
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(7)
    root1.right.right = TreeNode(18)
    
    # Test Case 2:
    #     10
    #    /  \
    #   5    15
    #  / \   / \
    # 3   7 13  18
    # /   /
    # 1   6
    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.right = TreeNode(15)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(13)
    root2.right.right = TreeNode(18)
    root2.left.left.left = TreeNode(1)
    root2.left.right.left = TreeNode(6)
    
    solution = Solution()
    
    # Run test cases
    print("Test Case 1:")
    print("Input: low = 7, high = 15")
    print("Expected: 32")
    print("Actual:", solution.rangeSumBST(root1, 7, 15))
    print()
    
    print("Test Case 2:")
    print("Input: low = 6, high = 10")
    print("Expected: 23")
    print("Actual:", solution.rangeSumBST(root2, 6, 10))