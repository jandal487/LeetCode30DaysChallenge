# Week2
# 1. Middle of the Linked List 
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head_node = None

    def print_SinglyLinkedList(self):
        linked_list = ""
        if self.head_node is None:
            print("Singly Linked List is empty!")
            return
        else:
            p_node = self.head_node
            while p_node is not None:
                linked_list = str(p_node.val) + " -> " + linked_list
                p_node = p_node.next
        print(linked_list)

    def insert_at_head(self, stack):
        new_node = Node(stack)
        new_node.next = self.head_node
        self.head_node = new_node
    
    def insert_at_tail(self, stack):
        new_node = Node(stack)
        if self.head_node is None:
            self.start_node = new_node
            return
        t_node = self.start_node
        while t_node.next is not None:
            t_node = t_node.next
        t_node.next = new_node

    def middle_node(self, head_node):
        iNode = head_node
        jNode = head_node
        while jNode and jNode.next:
            iNode = iNode.next
            jNode = jNode.next.next
        return iNode.val

#singlyLinkedList = SinglyLinkedList()
#singlyLinkedList.insert_at_head(1)
#singlyLinkedList.insert_at_head(2)
#singlyLinkedList.insert_at_head(3)
#singlyLinkedList.insert_at_head(4)
#singlyLinkedList.insert_at_head(5)
#singlyLinkedList.print_SinglyLinkedList()
#singlyLinkedList.middle_node(singlyLinkedList.head_node)

# 2. Backspace String Compare
class Solution:
    def backspaceCompare(self, S, T):
        s_list = []
        t_list = []

        for s in list(S):
            if s != '#':
                s_list.append(s)
            else:
                if len(s_list) > 0:
                    s_list.pop()

        for t in list(T):
            if t != '#':
                t_list.append(t)
            else:
                if len(t_list) > 0:
                    t_list.pop()
                    
        return s_list == t_list

#solObj = Solution()
#solObj.backspaceCompare("a#c", "b")

# 3. Min Stack
class MinStack:

    def __init__(self):
        """
        initialize your stack structure here.
        """
        self.stack = []
        self.minValueStack = []
        

    def push(self, x):
        if x != []:
            if self.isStackEmpty():
                self.stack.append(x)
                self.minValueStack.append(x)
            else:
                self.stack.append(x)
                if x <= self.getMin():
                    self.minValueStack.append(x)

    def pop(self):
        if self.isStackEmpty():
            print("Stack is empty!")
        else:
            removed = self.stack.pop()
            if removed == self.getMin():
                self.minValueStack.pop()

    def top(self):
        if not self.isStackEmpty():
            return self.stack[-1]

    def getMin(self):
        if not self.isMinStackEmpty():
            return self.minValueStack[-1]
        else:
            return None

    def isStackEmpty(self):
        return len(self.stack) < 1

    def isMinStackEmpty(self):
        return len(self.minValueStack) < 1

    def printStack(self):
        print("---")
        for d in range(len(self.stack)-1, -1, -1):
            print("| ", self.stack[d] ,"  \n")
        print("---")

    def printMinStack(self):
        print("---")
        for d in range(len(self.minValueStack)-1, -1, -1):
            print("| ", self.minValueStack[d] ,"  \n")
        print("---")

#minStack = MinStack()
#minStack.push(2)
#minStack.push(0)
#minStack.push(3)
#minStack.push(0)
#minStack.printStack()
#minStack.printMinStack()

#minStack.pop()
#minStack.printStack()
#minStack.printMinStack()

#minStack.pop()
#minStack.printStack()
#minStack.printMinStack()

#minStack.pop()
#minStack.printStack()
#minStack.printMinStack()

# 4. Diameter of Binary Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionBinaryTree:
    def diameterOfBinaryTree(self, root):
        if root == None: return 0

        leftHeight = self.heightOfBinaryTree(root.left)
        rightHeight = self.heightOfBinaryTree(root.right)

        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        heightWithRoot = leftHeight + rightHeight
        heightWithoutRoot = max(leftDiameter, rightDiameter)

        return max(heightWithRoot, heightWithoutRoot)

    def heightOfBinaryTree(self, root):
        if root == None: return 0
        
        leftHeight = self.heightOfBinaryTree(root.left)
        rightHeight = self.heightOfBinaryTree(root.right)
        
        return 1 + max(leftHeight, rightHeight)


# Build a Binary Tree
#rootNode = TreeNode(1)
#n2 = TreeNode(2)
#n3 = TreeNode(3)
#n4 = TreeNode(4)
#n5 = TreeNode(5)
#rootNode.left = n2
#rootNode.right = n3
#n2.left = n4
#n2.right = n5

#solObj = SolutionBinaryTree()
#solObj.diameterOfBinaryTree(rootNode)


# 5. Last Stone Weight
class SolutionLSWeight:
    def lastStoneWeight0(self, stones):
        # Solution 1: Using sorted array
        if len(stones) < 1: 
            return 0
        if len(stones) == 1: 
            return stones[0]
        else:
            while(len(stones) > 1):
                stones.sort()
                x = stones[-2] # second heavy
                y = stones[-1] # heaviest stones

                if (x == y):
                    # Drop last 2 stones
                    stones = stones[:-2]
                else:
                    stones[-2] = y - x
                    # Drop the last stone
                    stones = stones[:-1] 

        if len(stones) == 1:
            return stones[0]
        else:
            return 0

    def lastStoneWeight(self, stones):
        # Solution 2: Using Min Heap
        import heapq
        stones = [-1*i for i in stones]
        heapq.heapify(stones)

        while(len(stones) > 1):
            y = -1*(heapq.heappop(stones))
            x = -1*(heapq.heappop(stones))

            if x != y:

                heapq.heappush(stones, -1*(y - x))

        if len(stones) == 1:
            return -1*(stones[0])
        else:
            return 0

#solObj = SolutionLSWeight()
#solObj.lastStoneWeight([2,7,4,1,8,1])

# 6. Contiguous Array
class SolutionContigArray:
    def findMaxLength(self, nums):
        countDict = {}
        count = 0
        maxLength = 0
        for i in range(len(nums)):
            if nums[i] == 1: count += 1
            if nums[i] == 0: count += -1
            if count == 0: maxLength = i + 1

            if count not in countDict:
                countDict[count] = i
            else:
                maxLength = max(maxLength, i-countDict[count])
                
        return maxLength

#solObj = SolutionContigArray()
#solObj.findMaxLength([0,0,1,0,0,0,1,1])

# 7. Perform String Shifts
class SolutionStringShift:
    def stringShift(self, s, shift):
        shift_left = 0
        for direction, shift_value in shift:
            if direction == 0:
                # Left shift
                shift_left = shift_left + shift_value
            else:
                # Right shift
                shift_left = shift_left - shift_value

        shift_left = shift_left % len(s)

        return s[shift_left:] + s[:shift_left]

solObj = SolutionStringShift()
print(solObj.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))