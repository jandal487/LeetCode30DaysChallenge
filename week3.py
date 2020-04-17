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

solObj = SolutionCountIslands()
grid = [['1','1','0','0','0'], \
        ['1','1','0','0','0'], \
        ['0','0','1','0','0'], \
        ['0','0','0','1','1']]
print(solObj.numIslands(grid))
