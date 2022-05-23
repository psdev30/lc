# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        s, f, counter = head, head, 0
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                length = self.get_cycle_length(f)
                f = self.move_fast_pointer(length, head)
                return self.find_start_node(head, f)



    def get_cycle_length(self, p):
        pointer, counter = p, 0
        while True:
            pointer = pointer.next
            counter += 1
            if pointer == p:
                break

        return counter



    def move_fast_pointer(self, length, head):
        p = head
        while length > 0:
            p = p.next
            length -= 1

        return p


    def find_start_node(self, s, f):
        while s != f:
            s = s.next
            f = f.next

        return f
