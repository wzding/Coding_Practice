# 530. Minimum Absolute Difference in BST
# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

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

# 538. Convert BST to Greater Tree
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.inorder(root)
        return root
    
    def inorder(self,root): # right - root - left
        if not root:
            return
        self.inorder(root.right)
        root.val += self.sum
        self.sum = root.val
        self.inorder(root.left)
# Since this is a BST, we can do a reverse inorder traversal to traverse the nodes of the tree in descending order. In the process, we keep track of the running sum of all nodes which we have traversed thus far.