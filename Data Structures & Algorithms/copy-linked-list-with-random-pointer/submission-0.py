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
        copy = {None:None}
       
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            node = copy[curr]
            node.next = copy[curr.next]
            node.random = copy[curr.random]
            curr = curr.next
        return copy[head]