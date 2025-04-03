# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recur(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        self.recur(root.left, result)
        result.append(root.val)
        self.recur(root.right, result)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.recur(root, result)
        return result