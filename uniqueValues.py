#Unique values below
array = [31,51,136,7,35,17,86,26,68,76,45,24]
#Not unique values below
#array = [31,51,136,7,35,17,86,26,68,76,45,24,24]

def unique(array):
	for j in range(len(array)):
		for k in range(j+1, len(array)):
			if array[j] == array[k]:
				return False
	return True
	
print(unique(array))	
