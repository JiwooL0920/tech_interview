# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def mergeTwoLists(self, l1, l2):
		if l1 is None:
			return l2

		if l2 is None:
			return l1

		if (l1.val > l2.val):
			head = ListNode(l2.val)
			head.next = self.mergeTwoLists(l1, l2.next)
		else:
			head = ListNode(l1.val)
			head.next = self.mergeTwoLists(l1.next, l2)

		return head


"""
make another linked list L3 
continue adding nodes in the link list while we traverse
the list both at the same time 
"""