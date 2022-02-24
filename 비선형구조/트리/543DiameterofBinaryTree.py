class Solution:
    longest : int = 0

    def diameterOfBinaryTree(self, root : TreeNode) -> int:
        def dfs(node: TreeNode) -> int :
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1
        dfs(root)
        return self.longest


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_length(node):
            left = right = 0
            
            if node.left:
                left = get_length(node.left) + 1
            
            if node.right:
                right = get_length(node.right) + 1
                
            res.append(left + right)
            return max(left, right)
        
        res = [0]
        
        if root:
            get_length(root)
        
        return max(res)