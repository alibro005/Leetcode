# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root == None:
            return 0

        leftHeight = self.solve(root.left)
        rightHeight = self.solve(root.right)

        self.result = max(self.result, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.solve(root)
        return self.result
