# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length +=1
            curr = curr.next
        times = length // k
        start = head
        dummy = ListNode(0,head)
        prevTail = dummy
        for _ in range(times):
            # reverse
            curr = tail = start
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # prev = 这组反转后的头
            # tail = 这组反转后的尾
            # curr = 下一组的头
            prevTail.next = prev   # 上一组尾 -> 这组新头
            tail.next = curr       # 这组尾 -> 下一组头
            prevTail = tail        # 更新 prevTail
            start = curr           # 更新 start
        return dummy.next
