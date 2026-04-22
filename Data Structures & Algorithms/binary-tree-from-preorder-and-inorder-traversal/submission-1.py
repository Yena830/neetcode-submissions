# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {}
        for i,val in enumerate(inorder):
            inorder_dict[val] = i
        def build(pre_left,pre_right,in_left,in_right):
            if in_left == in_right:
                return None
            root_val = preorder[pre_left]
            root_index = inorder_dict[root_val]
            left_size = root_index - in_left
            left = build(pre_left+1,pre_left+1+left_size,in_left,in_left+left_size)
            right = build(pre_left+1+left_size,pre_right,root_index+1,in_right)
            return TreeNode(root_val,left,right) 
        return build(0,len(preorder),0,len(inorder))
        