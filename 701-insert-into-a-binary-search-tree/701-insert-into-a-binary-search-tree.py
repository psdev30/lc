# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        head, temp, newNode = root, None, TreeNode(val)
        while head:
            temp = head
            if val > head.val:
                head = head.right
            else:
                head = head.left
        if not temp:       
            root = TreeNode(val)
        elif val > temp.val:
            temp.right = newNode
        else:
            temp.left = newNode
        # newNode.p = temp
        
        return root