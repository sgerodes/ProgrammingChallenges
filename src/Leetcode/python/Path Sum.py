# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum-=root.val
        if not root.left and not root.right:
            if sum == 0:
                return True
            else:
                return False

        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
