class Solution(object):
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: None Do not return anything, modify nums1 in-place instead.
		"""
		# make a copy of nums1
		nums1_save = nums1[:m]
		# record current position in the array
		index1, index2 = 0, 0
		# while there still are elements in array
		while (index1 < m and index2 < n):
			if nums1_save[index1] <= nums2[index2]:
				nums1[index1 + index2] = nums1_save[index1]
				index1 += 1
			else:
				nums1[index1 + index2] = nums2[index2]
				index2 += 1
			# we used up all elements from nums1 but elements from nums2 remaining
		if index1 == m:
			nums1[(index1 + index2):] = nums2[index2:]
		if index2 == n:
			nums1[(index1 + index2):] = nums1_save[index1:]

