def find_and_print_max(arr):
    max = 0
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
    print max

find_and_print_max([3,5,7,2,9,11,5,3])