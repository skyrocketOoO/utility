from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class visit_tree:
    def preorder(self, root: Optional[TreeNode]) -> List[TreeNode]:
        if root is None:
            return []
        
        stk = [root]
        order = []
        while stk:
            node = stk.pop()
            order.append(node)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
                
        return order