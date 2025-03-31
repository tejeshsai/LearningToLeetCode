class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BSTTraversal:
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.val, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=" ")



if __name__ == "__main__":
    # Create a sample BST:
    #         8
    #       /   \
    #      3     10
    #     / \      \
    #    1   6      14
    #       /
    #      4
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.right.right = TreeNode(14)

    it = BSTTraversal()
    print("Inorder Traversal (Sorted Order):")
    it.inorder(root)  # Expected output: 1 3 4 6 8 10 14
    print()
    print("Preorder Traversal:")
    it.preorder(root)  # Expected output: 8 3 1 6 4 10 14
    print()
    print("Postorder Traversal:")
    it.postorder(root)  # Expected output: 1 4 6 3 14 10 8
    