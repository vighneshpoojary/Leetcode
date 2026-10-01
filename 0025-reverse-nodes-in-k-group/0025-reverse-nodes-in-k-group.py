# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp = head
        cnt = 0
        while cnt<k:
            if temp == None:
                return head
            temp = temp.next
            cnt += 1
        prevnode  = self.reverseKGroup(temp, k)
        temp  = head 
        cnt = 0
        while(cnt<k):
            next = temp.next
            temp.next = prevnode
            prevnode = temp
            temp = next
            cnt += 1
        return prevnode