# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        time: O(n)
        space: O(1)
        """
        # 2 pointers
        p1 = headA
        p2 = headB
        # advance pointers by one step, when they reach end, they are
        # assigned to the other list's head
        while (p1 != p2):
            # if p1 is not at the end, advance 1 step
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1 #or p2, doesn't matter 