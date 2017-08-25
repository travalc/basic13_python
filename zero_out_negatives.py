def zero_out_negatives(list):
    for i in range (0, len(list)):
        if list[i] < 0:
            list[i] = 0
    print list

zero_out_negatives([1, 2, 0, 4, -3, -4, 9, 10, -12])