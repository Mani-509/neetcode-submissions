# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. Base Case: If the tree is empty, return None
        if not root:
            return None
        
        # 2. The Swap: Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # 3. The Recursive Calls: Invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return the original root, which now represents the inverted tree
        return root