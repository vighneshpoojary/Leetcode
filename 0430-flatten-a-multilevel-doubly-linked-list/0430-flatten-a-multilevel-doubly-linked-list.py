"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head

        curr = head
        while curr:
            if curr.child:
                # 1. Save the next node in the main list
                next_node = curr.next

                # 2. Recursively flatten the child list and attach it to curr.next
                curr.next = self.flatten(curr.child)
                curr.next.prev = curr
                curr.child = None

                # 3. Traverse to the tail of the newly attached child list
                tail = curr
                while tail.next:
                    tail = tail.next

                # 4. Connect the tail to the original next node
                if next_node:
                    tail.next = next_node
                    next_node.prev = tail

            curr = curr.next

        return head
        
        