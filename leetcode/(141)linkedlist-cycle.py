# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # move fast pointer by 2
        # move slow pointer by 1
        # check if fast pointer reached end or
        # fast pointer == slow pointer (cycle)
        # space: 2 pointers O(1)
        # time: O(n)
        if head is None:
            return False
        ptr = head
        fastPtr = head.next
        while (ptr is not None) and (fastPtr is not None) and (fastPtr.next is not None):
            if ptr == fastPtr:
                return True
            ptr = ptr.next
            fastPtr = fastPtr.next.next
        return False 