# 1. Binary Tree Maximum Path Sum
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionTN:
    def maxPathSum(self, root):
        self.maxSum = float('-inf')

        self.getMaxSum(root) # Maximum sum starting from root

        return self.maxSum
        
    def getMaxSum(self, root):
        if root == None: return 0

        lresult = max(self.getMaxSum(root.left), 0)
        rresult = max(self.getMaxSum(root.right), 0)

        self.maxSum = max(self.maxSum, root.val + lresult + rresult)

        # Return maximum sum starting from root
        return root.val + max(lresult, rresult)

# Execution on leetcode.com

# 2. Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
class Solution:
    def isValidSequence(self, root, arr):
        index = 0

        return self.checkTreePath(root, arr, index)
    
    def checkTreePath(self, root, arr, index):
        if root is None: 
            return len(arr) == 0
        
        if (index == len(arr)-1) and (root.left == None) \
            and (root.right == None) and (root.val == arr[index]):
            return True

        if (index < len(arr)) and (root.val == arr[index]):
            checkLeft  = self.checkTreePath(root.left, arr, index+1)
            checkRight = self.checkTreePath(root.right, arr, index+1)

            return(checkLeft or checkRight)

# Execution on leetcode.com










