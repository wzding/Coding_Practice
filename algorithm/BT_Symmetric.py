# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.mirror(root.left,root.right)

    def mirror(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            outer = self.mirror(left.left,right.right)
            inner = self.mirror(left.right,right.left)
            if outer and inner:
                return True
            return False
        
