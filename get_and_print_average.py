def print_average(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    average = sum / len(list)
    print average

print_average([1, 2, 3, 4, 5])