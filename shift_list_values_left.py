def shift_list_values_left(list):
    for i in range(1, len(list)):
        list[i - 1] = list[i]
        if i == len(list) - 1:
            list[i] = 0
    print list

shift_list_values_left([1,2,3,4,5])