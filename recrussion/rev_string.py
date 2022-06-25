def rev(str):
    rev = ""
    for i in range(len(str)):
        rev = rev + str[(len(str)-i-1)]
        
    return rev


print(rev("karthik"))