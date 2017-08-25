def list_greater_than_y(list, y):
    count = 0
    for i in range(0, len(list)):
        if list[i] > y:
            count +=1
    print count

list_greater_than_y([1, 3, 4, 5, 6], 3)
