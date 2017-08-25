def max_min_average(list):
    max = 0
    min = list[0]
    sum = 0
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
        sum += list[i]
    average = sum / len(list)
    print 'max: ' + str(max)
    print 'min: ' + str(min)
    print 'average: ' + str(average)

max_min_average([4,5,6,7,3,11])