# Week 3
# 1. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums):
        prod_left = [1] * len(nums)
        prod_right = [1] * len(nums)

        for i in range(1, len(nums), 1):
            prod_left[i] = prod_left[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            prod_right[i] = prod_right[i+1] * nums[i+1]  

        output_list = list(map(lambda x,y: x*y, prod_left, prod_right))
        return(output_list) 

#solObj = Solution()
#solObj.productExceptSelf([1,2,3,4])

# 2. Valid Parenthesis String
class SolutionCheckParanthesis:
    # Solution 1: With 2 stacks
    def checkValidString(self, s):
        if len(s) == 0 or s == '*': return True
        if len(s) == 1 and s != '*': return False

        stack1 = []   # stores ( or )
        stack2 = []   # stores *

        for p, c in enumerate(s):
            if c == '*': stack2.append(p)
            elif c == '(': stack1.append(p)
            elif c == ')': 
                if len(stack1) > 0: stack1.pop()
                elif len(stack2) > 0: stack2.pop()
                else: return False

        while stack1 and stack2:
            if stack1[-1] < stack2[-1]:
                stack1.pop()
                stack2.pop()
            else: break
        
        return len(stack1) == 0
    
    # Solution 2: Without 2 stacks
    def checkValidString2(self, s):
        if len(s) == 0 or s == '*': return True
        if len(s) == 1 and s != '*': return False

        sArr = list(s)
        countLeftP  = 0
        for p in range(len(sArr)):
            if sArr[p] == ')': countLeftP -= 1
            else: countLeftP += 1        
            if countLeftP < 0: return False
        
        countRightP = 0
        for p in range(len(sArr)-1,-1,-1):
            if sArr[p] == '(': countRightP -= 1
            else: countRightP += 1        
            if countRightP < 0: return False

        return True

#solObj = SolutionCheckParanthesis()
#print(solObj.checkValidString("((*"))

# 3. Number of Islands
class SolutionCountIslands:
    def numIslands(self, grid):
        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': 
                    islandCount += 1
                    self.visitConnectingOnes(grid, i, j)
        return islandCount

    def visitConnectingOnes(self, grid, i, j):
        if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0'): 
            return
        grid[i][j] = '0'
        self.visitConnectingOnes(grid, i+1, j) # up
        self.visitConnectingOnes(grid, i-1, j) # down
        self.visitConnectingOnes(grid, i, j+1) # right
        self.visitConnectingOnes(grid, i, j-1) # left

#solObj = SolutionCountIslands()
#grid = [['1','1','0','0','0'], \
#        ['1','1','0','0','0'], \
#        ['0','0','1','0','0'], \
#        ['0','0','0','1','1']]
#print(solObj.numIslands(grid))

# 4. Min Path Sum
class SolutionMinPathSum:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n] * m
        dp[0][0] = grid[0][0] 
        
        for i in range(m):
            if i > 0:
                dp[i][0] = dp[i - 1][0] + grid[i][0]
            for j in range(1, n):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[m - 1][n - 1]

#solObj = SolutionMinPathSum()
#grid = [
#  [1,3,1],
#  [1,5,1],
#  [4,2,1]
#]
#solObj.minPathSum(grid)

# 4. Search in Rotated Sorted Array
class SolutionBST:
    def search(self, nums, target):
        if nums == None or len(nums) == 0: return -1
        #if len(nums) == 1: return 0 if nums[0] == target else -1

        leftIndex = 0
        rightIndex = len(nums)

        while leftIndex < rightIndex:
            midIndex = leftIndex + (rightIndex-leftIndex)//2
            midElemt = nums[midIndex]

            if midElemt == target: return midIndex
            if nums[leftIndex] <= midElemt:
                if target < midElemt and target >= nums[leftIndex]: 
                    rightIndex = midIndex
                else:
                    leftIndex = midIndex+1
            else:
                if target > midElemt and target <= nums[rightIndex-1]:
                    leftIndex = midIndex+1
                else:
                    rightIndex = midIndex
        return -1

#solObj = SolutionBST()
#print(solObj.search([1,3,5], 5))


# 5. Construct Binary Search Tree from Preorder Traversal
class TreeNode:
    def __init__(self, val): 
        self.val = val  
        self.left = None
        self.right = None


class SolutionBST:
    def bstFromPreorder(self, preorder):
        if preorder is None or len(preorder) == 0: return None
        inorder = sorted(preorder)

        return self.createBST(preorder, inorder)

    def createBST(self, preorder, inorder):
        lengthpr = len(preorder)
        lengthin = len(inorder)
        if lengthpr != lengthin or preorder is None \
            or inorder is None or lengthpr == 0 or lengthin == 0: return None


        rootNode  = TreeNode(preorder[0])
        rootIndex = inorder.index(rootNode.val)

        rootNode.left  = self.createBST(preorder[1:rootIndex+1], inorder[:rootIndex])

        rootNode.right = self.createBST(preorder[rootIndex+1:], inorder[rootIndex+1:])

        return rootNode

#solObj = SolutionBST()
#solObj.bstFromPreorder([8,5,1,7,10,12])


# 6. Leftmost Column with at Least a One
class SolutionLMC:
    def leftMostColumnWithOne(self, binaryMatrix): 
        rows, cols = binaryMatrix.dimensions()

        current_row = 0
        current_col = cols - 1
        while(current_row<rows and current_col>=0):
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1

        if current_col != cols-1:
            return current_col+1
        else:
            return -1

# Execution is on leetcode.com




















