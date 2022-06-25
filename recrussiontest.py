count=0
def dummy():
    global count
    print(count)

    if  count>3:
        print("done")
    else:
        count +=1

        dummy()
       
dummy()