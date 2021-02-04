arr = [4,2,6,6,8,1,9]

def mergesort(arr):
	if len(arr) <= 1:
		return arr
	mid = int(len(arr)/2)
	left, right = mergesort(arr[:mid]), mergesort(arr[mid:])
	return merge(left,right)

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


def selectionsort(arr):
	for i in range (len(arr)):
		min_index = i
		for j in range (i+1, len(arr)):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[min_index], arr[i] = arr[i], arr[min_index]


def bubblesort(arr):
	for i in range (len(arr)-1):
		for j in range (len(arr)-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

def binarysearch(arr, target):
	start = 0
	end = len(arr)-1
	while start <= end:
		mid = start + (end-start)//2
		mid_value = arr[mid]
		if mid_value == target:
			return mid
		elif target < mid_value:
			end = mid - 1
		else:
			start = mid+1
	return None

def revstirng(s):
	start, end = 0, len(s)-1
	while start <= end:
		s[start], s[end] = s[end], s[start]
		start += 1
		end -= 1

def revstring3(s):
	char = [c for c in s]
	start, end = 0, len(s)-1
	while (start <= end):
		char[start], char[end] = char[end], char[start]
		start += 1
		end -= 1
	return "".join(char)

def revstring2(s):
	words = s.split(" ")
	result = []
	for w in words:
		result.append(w[::-1])
	return " ".join(result)

def swap_numbers(a,b):
	"""
	a = 10, b = 5
	a now becomes 15
	y becomes 10
	x becomes 5
	"""
	a = a + b
	b = a - b
	a = a - b
	return a, b

# given a list write a function to add adjacent two elements and store them in a list and return
def addadjacent(arr):
	result = []
	for i in range(len(arr)-1):
		sum = arr[i] + arr[i+1]
		result.append(sum)
	return result

# print(arr)
# # print(mergesort(arr))
#
# # selectionsort(arr)
# # print(arr)
# bubblesort(arr)
# print(arr)
# s = ["h","e","l","l","o"]
# revstirng(s)
# print(s)
#
# s = "hello world!"
# s2 = revstring2(s)
# print(s2)
#
# a, b = swap_numbers(10,5)
# print(a, b)
#
# arr = [1,2,3,4,5,6,7]
# arr2 = addadjacent(arr)
# print(arr2)

s = "hello world"
print(revstring3(s))

# seq = [1,2,3,4,5,6,7,8,9]
# print(binarysearch(seq,9))