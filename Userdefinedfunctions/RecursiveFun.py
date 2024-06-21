def recursive(num):  #6,5,4,3,2,1
    print(num)
    num=num-1
    if num>0:
        recursive(num)

recursive(6)        