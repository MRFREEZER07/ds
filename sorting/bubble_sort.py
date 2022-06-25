def bubble_sort(a):
    for i in range(len(a)-1):
        print(a)
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a




numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(bubble_sort(numbers))