def cumulative(list_of_numbers):
    cumulative_sum = 0
    new_list = []
    for i in list_of_numbers:
        cumulative_sum += i
        new_list.append(cumulative_sum)
    return new_list

list = [1,2,3,4,5,6,7,8,9]
print(cumulative(list))