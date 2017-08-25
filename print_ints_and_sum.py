def print_ints_and_sum():
    sum = 0
    for i in range(0, 255 + 1):
        print 'i is currently ' + str(i)
        sum = sum + i
        print 'Current sum is ' + str(sum)

print_ints_and_sum()