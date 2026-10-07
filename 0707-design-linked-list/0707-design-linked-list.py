class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            index = 0
        if index > self.size:
            return
        
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
            
        new_node = ListNode(val, curr.next)
        curr.next = new_node
        self.size += 1        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
            
        curr.next = curr.next.next
        self.size -= 1