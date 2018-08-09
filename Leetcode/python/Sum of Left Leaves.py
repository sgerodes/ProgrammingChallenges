class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        l=root.left
        if l and not l.left and not l.right:
            return l.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(l)