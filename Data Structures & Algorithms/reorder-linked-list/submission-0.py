# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def findmid(node):
            # find mid node
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        mid = findmid(head)
        head2_start = mid.next
        mid.next = None
        head1 = head
        head2 = reverse(head2_start)
        dummy = curr = ListNode()
        while head1 and head2:
            nxt1,nxt2 = head1.next,head2.next
            # link head1 first
            curr.next = head1
            curr = curr.next

            # link head2
            curr.next = head2
            curr = curr.next

            # get next node for both
            head1 = nxt1
            head2 = nxt2
        # incase odd node
        if head1:
            curr.next = head1
