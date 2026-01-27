# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(value)
        if root.val == value:
            return root

        if root.val > value:
            root.left = self.insertIntoBST(root.left, value)
        else:
            root.right = self.insertIntoBST(root.right, value)

        return root
