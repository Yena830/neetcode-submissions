"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # link old and new node together
        curr1 = head
        while curr1:
            curr2 = Node(curr1.val)
            nxt = curr1.next
            curr1.next = curr2
            curr2.next = nxt
            curr1 = nxt
        newHead = head.next

        # get copy's random 
        curr1 = head
        while curr1:
            curr2 = curr1.next
            if curr1.random:
                curr2.random = curr1.random.next
            curr1 = curr1.next.next
        
        # unlink old and new
        curr1 = head
        while curr1:
            curr2 = curr1.next
            curr1.next = curr2.next
            if curr2.next:
                curr2.next = curr2.next.next
            curr1 = curr1.next
        return newHead
        