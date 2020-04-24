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