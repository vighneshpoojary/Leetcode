# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)
        first_ptr = dummy
        second_ptr = dummy
        for i in range(n):
            second_ptr = second_ptr.next
        while second_ptr.next is not None:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next
        first_ptr.next = first_ptr.next.next
        return dummy.next

            
