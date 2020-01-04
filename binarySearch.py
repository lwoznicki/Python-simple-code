def binary_search(data, target):

	low = 0
	high = len(data) - 1
	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
		return False

#Sorted data
data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binary_search(data, 4))