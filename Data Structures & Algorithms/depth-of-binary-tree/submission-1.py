# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root,1)]
        max_d = 1

        while stack:
            node,deepth = stack.pop()

            max_d = max(max_d,deepth)

            if node.left:
                stack.append((node.left,deepth+1))
            if node.right:
                stack.append((node.right,deepth+1))
        return max_d

