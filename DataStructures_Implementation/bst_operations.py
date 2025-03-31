class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BSTOperations:
    def __init__(self):
        self.root = None
    
    def insert(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.val:
            node.left = self.insert(node.left, key)
        elif key > node.val:
            node.right = self.insert(node.right, key)
        else:
            raise ValueError("Duplicates not allowed in BST")
        
        return node
    
    def search(self, node, key):
        if node is None:
            print("Not Found")
            return None
        if node.val == key:
            print("Found")
            return node
        
        if key < node.val:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
        
    def deletion(self, node, key):
        if node is None:
            print("Key is not found to delete")
            return None
            
        if key < node.val:
            node.left = self.deletion(node.left, key)
        elif key > node.val:
            node.right = self.deletion(node.right, key)
        else:
            # Case 1: Node with no children or one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
                
            # Case 2: Node with two children
            # Example: Deleting node 70
            # Before:    50        After:    50
            #          /  \                 /  \
            #         30   70             30   80
            #        /  \  / \           /  \  /
            #       20  40 60 80        20  40 60
            #
            # Steps:
            # 1. Find the successor (smallest value in right subtree)
            #    - Start from right child (60)
            #    - Keep going left until we find the smallest value (80)
            # 2. Replace the node's value with successor's value
            #    - Node 70's value becomes 80
            # 3. Delete the successor from the right subtree
            #    - Recursively delete 80 from the right subtree
            successor = self.minValueNode(node.right)
            node.val = successor.val
            node.right = self.deletion(node.right, successor.val)
            
        return node
    
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

if __name__ == "__main__":
    # Create a sample BST
    bst = BSTOperations()
    root = None
    
    # Initial Tree Structure:
    #        50
    #       /  \
    #     30    70
    #    /  \   / \
    #   20  40 60  80
    
    print("Building the BST:")
    root = bst.insert(root, 50)
    print("After inserting 50:")
    print("    50")
    
    root = bst.insert(root, 30)
    print("\nAfter inserting 30:")
    print("    50")
    print("   /")
    print("  30")
    
    root = bst.insert(root, 20)
    print("\nAfter inserting 20:")
    print("    50")
    print("   /")
    print("  30")
    print(" /")
    print("20")
    
    root = bst.insert(root, 40)
    print("\nAfter inserting 40:")
    print("    50")
    print("   /")
    print("  30")
    print(" /  \\")
    print("20  40")
    
    root = bst.insert(root, 70)
    print("\nAfter inserting 70:")
    print("    50")
    print("   /  \\")
    print("  30   70")
    print(" /  \\")
    print("20  40")
    
    root = bst.insert(root, 60)
    print("\nAfter inserting 60:")
    print("    50")
    print("   /  \\")
    print("  30   70")
    print(" /  \\  /")
    print("20  40 60")
    
    root = bst.insert(root, 80)
    print("\nFinal BST Structure:")
    print("    50")
    print("   /  \\")
    print("  30   70")
    print(" /  \\  / \\")
    print("20  40 60 80")
    
    print("\nInorder traversal of the BST:")
    bst.inorder(root)
    print()
    
    # Test search
    print("\nSearching for 40:")
    bst.search(root, 40)
    
    # Test deletion
    print("\nDeleting 20:")
    root = bst.deletion(root, 20)
    print("Tree after deleting 20:")
    print("    50")
    print("   /  \\")
    print("  30   70")
    print("   \\  / \\")
    print("   40 60 80")
    
    print("\nInorder traversal after deletion:")
    bst.inorder(root)
    print()
    
    root = bst.deletion(root, 70)
    print("\nAfter deletion (80 becomes the successor):")
    print("    50")
    print("   /  \\")
    print("  30   80")
    print("   \\  /")
    print("   40 60")
    
    print("\nInorder traversal after deletion:")
    bst.inorder(root)
    print()
