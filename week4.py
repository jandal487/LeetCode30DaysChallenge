# Week 4
# 1. Subarray Sum Equals K
class Solution:
    def subarraySum(self, nums, k):
        # O(n) sol can be using a hashmap
        result = 0
        currSum = 0
        prevSum = {}

        for currElem in nums:
            currSum += currElem

            if currSum == k:
                result += 1
            
            if (currSum - k) in prevSum:
                result += prevSum[currSum-k]
            
            if not currSum in prevSum:
                prevSum[currSum] = 1
            else:
                prevSum[currSum] = prevSum[currSum]+1 

        return result

solObj = Solution()
solObj.subarraySum([1,1,1], 2)