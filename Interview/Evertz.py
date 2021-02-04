# Write a program that detects palindrome
def ispalindrome(s):
	start, end = 0, len(s)-1
	while (start <= end):
		if s[start] is not s[end]:
			return False
		start += 1
		end -= 1
	return True

# bubble sort
def bubblesort(arr):
	for i in range (len(arr)-1):
		for j in range (len(arr)-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


# selection sort
def selectionsort(arr):
	for i in range (len(arr)):
		min_index = i
		for j in range (i+1, len(arr)):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]

# merge sort
def mergesort(arr):
	if len(arr) <= 1:
		return arr
	mid = int(len(arr)/2)
	left, right = mergesort(arr[:mid]), mergesort(arr[mid:])
	return merge(left, right)

def merge(left,right):
	result = []
	l = r = 0
	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	result.extend(left[l:])
	result.extend(right[r:])
	return result


# twosum
# Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
def twosum(arr,target):
	for i in range (len(arr)):
		for j in range (i+1,len(arr)):
			if arr[i] + arr[j] == target:
				return [i,j]
	return [-1,-1]

# reverse singly linked list
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def insertAtEnd(self, n):
		curr = self
		while curr.next != None:
			curr = curr.next
		curr.next = Node(n)

	def print(self):
		curr = self
		while curr != None:
			print(curr.data, "->", end= " ")
			curr = curr.next
		print()

	def reverse(self, head):
		prev = None
		curr = head
		while (curr != None):
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
		return prev






if __name__ == '__main__':
	# s = "racecar"
	# print(ispalindrome(s))
	#
	# arr = [2,7,11,15]
	# print(twosum(arr,9))
	#
	# n = Node(1)
	# n.insertAtEnd(2)
	# n.insertAtEnd(3)
	# n.print()
	# n2 = n.reverse(n)
	# n2.print()

	array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
	arr2 = mergesort(array)
	# selectionsort(array)
	print(arr2)

