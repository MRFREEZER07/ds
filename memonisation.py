def addto80(n):
    print(n +80)
addto80(2)
addto80(2)
addto80(2)


cache ={}
def memoaddto80(n):
    if n in cache:
        return cache[n]
    else:
        print("long time")
        answer =n+80
        cache[n] =answer
        return answer
    
memoaddto80(1)
memoaddto80(1)
memoaddto80(2)
memoaddto80(12)
print(cache)