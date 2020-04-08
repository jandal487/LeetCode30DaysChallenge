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
        index = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index = index + 1

        for i in range(index, len(nums)):
            nums[i] = 0
        
        return(nums)

    # 5. Best Time to Buy and Sell Stock II
    def maxProfit(self, prices):
        if len(prices) > 1:
            if (prices[1] - prices[0]) > 0:
                maxProfValue = prices[1] - prices[0]
            else:
                maxProfValue = 0
            for i in range(1,len(prices)-1):
                profit = prices[i+1] - prices[i]
                if profit > 0:
                    maxProfValue = maxProfValue + profit

            return(maxProfValue)
        else:
            return 0
        return 0

    # 6. Group Anagrams
    def groupAnagrams(self, strs):
        temp_dict = {}
        
        for item in strs:
            sortedItem = sorted(item)
            hashKey = ''.join(sortedItem)
            if hashKey in temp_dict:
                temp_dict[hashKey].append(item)
            else:
                temp_dict[hashKey] = [item]

        return [value for value in temp_dict.values()]

    # 7. Counting Elements
    def countElements(self, arr):
        temp_dict = {}
        for x in arr:
            temp_dict[x] = 1
        
        count = 0
        for x in arr:
            if (x+1 in temp_dict):
                count = count + 1

        return count


solObj = Solution()
#solObj.singleNumber(221)
#solObj.isHappy(19)
#solObj.maxSubArray([8,-19,5,-4,20])
#solObj.moveZeroes([0,1,0,3,12])
#solObj.maxProfit([7,6,4,3,1])
#solObj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
solObj.countElements(  [1,3,2,3,5,0])

