# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1
            return 1+ max(left,right)
        
        return check(root) != -1