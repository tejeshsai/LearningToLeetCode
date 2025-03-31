class Solution:
    def __init__(self):
        self.result, self.count = None, None

    def kthSmallestElementBst(self, root, k):
        self.inorder(root, k)
        return self.result
    
    def inorder(self, root, k):
        if root is None or self.count >= k:
            return
        self.inorder(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root.val
        self.inorder(root.right,k)