# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, value, n=None):
        self.value = value
        self.next = n

class MyLinkedList:

    def __init__(self):
        self.dummyHead = Node(None)

    def get(self, index: int) -> int:
        ptr = self.dummyHead.next
        i = 0
        while ptr is not None and i < index:
            ptr = ptr.next
            i += 1
        if ptr is None: 
            return -1
        return ptr.value

    def addAtHead(self, val: int) -> None:
        self.dummyHead.next = Node(val, self.dummyHead.next)

    def addAtTail(self, val: int) -> None:
        ptr = self.dummyHead
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        ptr = self.dummyHead
        i = -1
        while ptr is not None and i < index-1:
            ptr = ptr.next
            i += 1
        if ptr is not None:
            ptr.next = Node(val, ptr.next)
        
    def deleteAtIndex(self, index: int) -> None:
        ptr = self.dummyHead
        i = -1
        while ptr.next is not None and i < index-1:
            ptr = ptr.next
            i += 1
        if ptr.next is not None:
            ptr.next = ptr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)