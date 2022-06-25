def sel_sort(a):
    for i in range(len(a)-1):
        indexofmin = i
        min =a[i]
        for j in range(i+1,len(a)):
            if a[j]< min:
                min =a[j]
                indexofmin=j
        if indexofmin != i:
            a[indexofmin],a[i]=a[i],a[indexofmin]
    
    return a            
    
    
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(sel_sort(numbers))