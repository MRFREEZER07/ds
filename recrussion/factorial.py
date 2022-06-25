#5!=5x4x3x2x1
def factorial(number):
    if number <=1:
        return 1
    else:
        return number * factorial(number-1)
    
    
    
    
    
    
    
    
    
def normal_FACT(number):
    fact =1
    for i in range(2,number+1):
        fact=fact*i
    return fact
print(normal_FACT(23))
print(factorial(23))       
        