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

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head_node
        self.head_node = new_node
    
    def insert_at_tail(self, data):
        new_node = Node(data)
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

singlyLinkedList = SinglyLinkedList()
singlyLinkedList.insert_at_head(1)
singlyLinkedList.insert_at_head(2)
singlyLinkedList.insert_at_head(3)
singlyLinkedList.insert_at_head(4)
singlyLinkedList.insert_at_head(5)
singlyLinkedList.print_SinglyLinkedList()
singlyLinkedList.middle_node(singlyLinkedList.head_node)