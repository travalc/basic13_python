def square_list_values(list):
    for i in range(0, len(list)):
        list[i] = list[i] ** 2
    print list

square_list_values([0, 1, 2, 3, 4])