# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preOrderTrav(self, root: TreeNode) -> List[int]:
        tree_trav = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                tree_trav.append(curr.val)
                curr = curr.left
            else:
                tree_trav.append(curr)
                curr = stack.pop()
                curr = curr.right
        return tree_trav

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree_trav1 = self.preOrderTrav(p)
        tree_trav2 = self.preOrderTrav(q)
        print(tree_trav1)
        print(tree_trav2)
        return tree_trav1 == tree_trav2

        
            

            