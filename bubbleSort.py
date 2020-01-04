
def bubbleSort(array):
	arrayLength = len(array)
	
	for i in range(arrayLength):
		for j in range(0, arrayLength-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]

array = [34,25,151,163,561,682,725,820,200,625,215,461,727,241,169,415,1,513,635,563,178]
 
bubbleSort(array)
 
print ("Sorted array: ")

for i in range(len(array)):
    print ("%d" %array[i]) 
