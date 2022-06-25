#0,1,1,2,3,5,8,13,21


def fib_rec(n):
    if n<2:
        return n
    else:
        return fib_rec(n-1)+fib_rec(n-2)
    
a=fib_rec(8)
print(a)

def fib(n):
    l=[0,1]
    for i in range(2,n+1):
        l.append(l[i-2] + l[i-1])
    return l[n]

print(fib(0))