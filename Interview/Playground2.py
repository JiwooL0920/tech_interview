def selectionsort(arr):
	for i in range (len(arr)):
		min_index = i
		for j in range (i+1, len(arr)):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[min_index], arr[i] = arr[i], arr[min_index]

def bubblesort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

def mergesort(arr):
	if len(arr) <= 1:
		return arr
	mid = int(len(arr)/2)
	left, right = mergesort(arr[mid:]), mergesort(arr[:mid])
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


arr = [6,9,8,7,3,4,2,1]
arr2 = mergesort(arr)
print(arr2)