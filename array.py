# l=['a','b','c','d','e','f','g','h','i','k']

# l.append('s') #o(1)
# l.insert(1,'e') #o(n)
# l.pop() #o(1)
# l.remove('c') #o(n)
# print(l)

# k="karthik"
# l=list(k)
# print(l)
# for i in range(len(l)-1):
#     print(l[i])
    
    
# ##STR REV

# def rev(str):
#     rev_str=str[::-1]
#     print(rev_str)

l =[1,2,3,4,5,6,7]

length =len(l)
lengthminux1=len(l)-1
print(length)
print(lengthminux1)
for i in range(lengthminux1):
    print(l[i])
    
print('------------')

for j in range(length):
    print(l[j])