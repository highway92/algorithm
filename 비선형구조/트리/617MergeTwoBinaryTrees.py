class Solution:
    def mergeTrees(self, root1, root2):
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.right)
            node.right = self.mergeTrees(root2.left, root2.right)
            return node
        else:
            root1 or root2
        