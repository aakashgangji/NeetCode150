# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:
# Input: root = [1]
# Output: [[1]]
# Example 3:
# Input: root = []
# Output: []


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=collections.deque()
        q.append(root)
        res=[]
        while q:
            level=[]
            lq=len(q)
            for i in range(lq):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
