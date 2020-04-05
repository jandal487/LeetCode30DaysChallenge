# Week1
from typing import List
class Solution:
    # 1. Single Number
    def singleNumber(self, nums):
        """
        :type nums: int
        :rtype: int
        """
        nums = [int(x) for x in str(nums)]
        no_dup_list = []
        for n in nums:
            if(n not in no_dup_list):
                no_dup_list.append(n)
            else:
                no_dup_list.remove(n)
                
        return(no_dup_list[0])
        
    # 2. Happy Number
    def isHappy(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        bucketOfN = []
        while(n != 1):
            dgtsList = [int(x) for x in str(n)]
            sqrsList = [pow(x,2) for x in dgtsList]
            n = sum(sqrsList)
            if n in bucketOfN:
                break
            else:
                bucketOfN.append(n)

        if n == 1:
            return(True)
        else:
            return(False)

    # 3. Maximum Subarray
    def maxSubArray(self, nums):
        # Linear solution using Kadane's Algorithm
        largestSum = nums[0]
        tempSum = nums[0]
        for i in range(1,len(nums)):
            tempSum = max(nums[i], tempSum + nums[i])
            if(tempSum > largestSum):
                largestSum = tempSum

        return(largestSum)

    # 4. Move Zeroes
    def moveZeroes(self, nums):
        numberOfZeroes = nums.count(0)
        returnList = []
        for n in nums:
            if n != 0:
                returnList.append(n)
        
        while numberOfZeroes != 0:
            returnList.append(0)
            numberOfZeroes = numberOfZeroes - 1

        return(returnList)

    def moveZeroes1(self, nums):
        index = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index = index + 1

        for i in range(index, len(nums)):
            nums[i] = 0
        
        return(nums)

solObj = Solution()
#solObj.singleNumber(221)
#solObj.isHappy(19)
#solObj.maxSubArray([8,-19,5,-4,20])
solObj.moveZeroes1([0,1,0,3,12])

