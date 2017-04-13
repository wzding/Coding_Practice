# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min = float('inf')
        self.previous = float('inf')
            
        def inorder(root): # left - root - right
            if root:
                inorder(root.left)
                self.min = min(self.min, abs(root.val - self.previous))
                self.previous = root.val
                inorder(root.right)
        
        inorder(root)
        return self.min