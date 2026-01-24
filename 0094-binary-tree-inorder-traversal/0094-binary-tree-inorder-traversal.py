# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def in_order(self, root, result):
        if root == None:
            return

        self.in_order(root.left, result)
        result.append(root.val)
        self.in_order(root.right, result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.in_order(root,result)
        return result
