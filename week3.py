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

solObj = Solution()
solObj.productExceptSelf([1,2,3,4])

