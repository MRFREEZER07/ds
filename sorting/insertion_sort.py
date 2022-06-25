def ins(a):
    for i in range(1,len(a)):#we consider the forst elemet is sorted
        key =a[i]
        j=i-1 #refers sorted array
        while (j>=0 and a[j]>key):# loop continuous until it reaches its pos  
            a[j+1]=a[j]
            j-=1
        a[j+1] =key #insert key at right pos
    return  a       
    
    
    
      

array = [5,9,3,10,45,2,0]
print(ins(array))