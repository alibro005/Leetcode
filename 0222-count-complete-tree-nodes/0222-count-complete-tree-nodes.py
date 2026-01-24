# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def count(self, root, count):
        if root == None:
            return

        self.count(root.left, count)
        self.count(root.right, count)
        count.append(root.val)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = []
        if root == None:
            return 0

        self.count(root, count)
        return len(count)
