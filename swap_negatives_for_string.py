def swap_negatives_for_string(list):
    for i in range (0, len(list)):
        if list[i] < 0:
            list[i] = 'Dojo'
    print list

swap_negatives_for_string([1, 2, 3, -3, 4, -5, 0])