# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_order(self, root, result):
        if root == None:
            return

        self.in_order(root.left, result)
        result.append(root.val)
        self.in_order(root.right, result)

        return result

    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        self.in_order(root, result)

        dummy = TreeNode(0)
        current = dummy

        for val in result:
            current.right = TreeNode(val)
            current = current.right
        return dummy.right