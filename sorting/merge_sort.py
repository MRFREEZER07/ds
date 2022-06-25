def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array)//2
        left_array = array[:mid]
        right_array = array[mid:]
        print(f'Left : {left_array}')
        print(f'Right : {right_array}')
        return merge(merge_sort(left_array),merge_sort(right_array))
        
        


def merge(left ,right):
    result =[]
    left_index=0
    right_index=0
    while(left_index<len(left) and right_index<len(right)):#to make sure there is an element
        if(left[left_index]<right[right_index]):
            result.append(left[left_index])
            left_index+=1
        else:
            result.append(right[right_index])
            right_index+=1
    
    print(result)      
                        
        










l = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48]  
        
print(merge_sort(l))