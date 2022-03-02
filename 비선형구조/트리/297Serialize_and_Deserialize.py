# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = collections.deque([root])
        result = []
        
        while queue:
            cur = queue.popleft()
            
            if cur:
                result.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                result.append('null')
        
        return ' '.join(result)
            
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        nodes = data.split()
        index = 1
        root = TreeNode(int(nodes[0]))
        queue = collections.deque([root])
        
        while queue:
            cur = queue.popleft()
            
            if nodes[index] != 'null':
                cur.left = TreeNode(int(nodes[index]))
                queue.append(cur.left)
            index += 1
            
            if nodes[index] != 'null':
                cur.right = TreeNode(int(nodes[index]))
                queue.append(cur.right)
            index += 1
            
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))