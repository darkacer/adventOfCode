# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):

        answer = [0]

        def reccursive(node, number):

            if node != None:
                number += str(node.val)
                if node.left == None and node.right == None:
                    answer[0] += int(number)
                if node.left != None:
                    reccursive(node.left, number)
                if node.right != None:
                    reccursive(node.right, number)


        if root != None:
            reccursive(root, '')

        return answer[0]
