def insertion_sort(a):
    for i in range(1, len(a)):
        current_val = a[i]
        pos = i
        while pos > 0 and a[pos - 1] > current_val:
            a[pos] = a[pos - 1]
            pos -= 1
        a[pos] = current_val
    return a


a = [2,4,90,0,34,21]
print(insertion_sort(a))


