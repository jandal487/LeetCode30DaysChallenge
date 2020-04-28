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

#solObj = Solution()
#solObj.subarraySum([1,1,1], 2)

# 2. Bitwise AND of Numbers Range
class SolutionBitwiseAND:
    def rangeBitwiseAnd(self, m, n):
        count = 0
        while(m != n):
            m = m >> 1
            n = n >> 1
            count += 1
        
        return(m << count)

solObj = SolutionBitwiseAND()
solObj.rangeBitwiseAnd(9, 12)

# 3. LRU Cache
# Solution 1: Using Doubly Linked List
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val =  value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def headInsertion(self, node):
        if (self.head is None):
            # First element in DLL
            self.head = node
            self.tail = node
        else:
            # If DLL is not empty
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    
class LRUCache0:
    def __init__(self, capacity):
        self.list = DoublyLinkedList()
        self.dict = {}
        self.capacity = capacity
        
    def put(self, key, val):
        node = Node(key, val)
        self.list.headInsertion(node)
        self.dict[key] = node

    def get(self, key):
        if key in self.dict:
            val = self.dict[key].val
            self.list.delete(self.dict[key])
            self.put(key, val)
            return val
        return -1

    def set(self, key, val):
        if key in self.dict:
            self.list.delete(self.dict[key])
        elif len(self.dict) == self.capacity:
            del self.dict[self.list.head.key]
            self.list.delete(self.list.head)
        self.put(key, val)

# Solution 2: Using OrderedDict
class LRUCache:
    import collections
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1

        val = self.cache[key]

        del self.cache[key]

        self.cache[key] = val

        return val

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
            
        self.cache[key] = value

# Execution on leetcode.com

# 4. Jump Game
class SolutionJump:
    def canJump(self, nums):
        jump = nums[0]

        for i in range(1, len(nums)):
            if jump == 0:
                return False

            jump = max(jump - 1, nums[i])
            
        return True

#solObj = SolutionJump()
#solObj.canJump([2,3,1,0,4])    

# 5. Longest Common Subsequence
class SolutionLCS:
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2) 
    
        # Make 2D grid from 2 strings
        g2D = [[0]*(n+1) for i in range(m+1)] 
    
        for i in range(m): 
            for j in range(n): 
                if text1[i] == text2[j]: 
                    g2D[i+1][j+1] = g2D[i][j]+1
                else: 
                    g2D[i+1][j+1] = \
                        max(g2D[i][j+1], g2D[i+1][j]) 
    
        return g2D[-1][-1] 

# = SolutionLCS()
#olObj.longestCommonSubsequence("abcdef", "ace")

# 6. Maximal Square
class SolutionMS:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        
        m, n, ans = len(matrix), len(matrix[0]), 0
        if m == 0 or n == 0:
            return 0
        
        dp = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    ans = max(ans, dp[i][j])
        
        return ans * ans

# Execution on leetcode.com

# 7. First Unique Number
class FirstUnique:
    def __init__(self, nums):
        self.q = []
        self.dict = {}
        for n in nums:
            self.add(n)

    def showFirstUnique(self):
        while (len(self.q) > 0 \
            and self.dict[self.q[0]] > 1):
            self.q.pop(0)

        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]

    def add(self, value):
        if value in self.dict:
            self.dict[value] += 1
        else:
            self.dict[value] = 1
            self.q.append(value)

    def printQ(self):
        print(self.q)


# Your FirstUnique object will be instantiated and called as such:
nums = [2, 3, 5]
obj = FirstUnique(nums)
obj.printQ()

print(obj.showFirstUnique())
obj.add(3)
obj.printQ()

