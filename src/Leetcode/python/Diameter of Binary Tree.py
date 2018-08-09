# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        return self.diameter(root)[1]

    def diameter(self, root):
        if not root:
            return -1,0
        leftMaxPath,leftDiam=self.diameter(root.left)
        leftMaxPath+=1
        rightMaxPath,rightDiam=self.diameter(root.right)
        rightMaxPath+=1
        nodeDiam=leftMaxPath+rightMaxPath
        return max(leftMaxPath,rightMaxPath),max(nodeDiam,leftDiam,rightDiam)
