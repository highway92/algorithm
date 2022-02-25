class Solution:
    def invertTress(self, root : Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            left, right = node.left,node.right
            node.left,node.right = right, left
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root