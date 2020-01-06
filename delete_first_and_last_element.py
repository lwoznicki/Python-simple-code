def delete_first_and_last_element(list):
	new_list = []
	i = 1
	while i <= len(list)-2:
		new_list.append(list[i])
		i += 1
	return new_list
	
list1 = [1,2,3,4,5]
print(list1)
print(delete_first_and_last_element(list1))