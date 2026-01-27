# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check_BST(self, root, result):
        if root == None:
            return
        self.check_BST(root.left, result)
        result.append(root.val)
        self.check_BST(root.right, result)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        self.check_BST(root, result)
        for i in range(len(result) - 1):
            if result[i] >= result[i + 1]:
                return False
        return True
