# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None: return False

        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f: return True
        