"""
generate postorder from preorder and inorder
"""
class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder:
            return
        self.res = []
        self.get_postorder(preorder, inorder, len(preorder))
        return self.res

    def get_postorder(self, preorder, inorder, n):
        root = preorder[0]
        idx = inorder.index(root)
        if idx != 0 : # left tree exist
            self.get_postorder(preorder[1:idx+1], inorder[:idx], idx)
        if idx != n - 1: # right tree exist
            self.get_postorder(preorder[idx+1:], inorder[idx+1:], len(inorder[idx+1:]))
        self.res.append(root)
