# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 나의 처음 풀이 완전탐색이기 때문에 개선의 여지가 있다.
class Solution:
    val = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        if low <= root.val <= high:
            self.val += root.val
            
        self.rangeSumBST(root.left,low,high)
        self.rangeSumBST(root.right,low,high)        
        
        return self.val

# BST의 특성을 활용한 재귀적 풀이
class Solution:
    result = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # result = 0
        def dfs(node):
            if node:
                if node.val < low :
                    return dfs(node.right)
                if node.val > high:
                    return dfs(node.left)
                if low <= node.val <= high:
                    self.result += node.val
                    dfs(node.right)
                    dfs(node.left)
        dfs(root)
        return self.result

# 책의 풀이 내가 짠 코드와 결이 비슷하지만 훨씬 깔끔하다.
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        return dfs(root)

# 반복문을 활용한 풀이 조금 더 직관적이다.
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, result = [root], 0
        
        while stack:
            node = stack.pop()
            
            if node:
                if low <= node.val <= high:
                    result += node.val
                    stack.append(node.left)
                    stack.append(node.right)
                
                elif node.val < low:
                    stack.append(node.right)
                elif node.val > high:
                    stack.append(node.left)
            
        return result