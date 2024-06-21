list1=[]
print(list1)
list1=[10,20,30,20,10]
print(list1)

list2=[6,"december",20.53]
print(list2)

#list functions
#inserting the data--> append(),insert(),extend()
list1.append(40)
list1.append(50)
print(list1)
list1.insert(5,60)
print(list1)
list3=[80,40,60,100]
list1.extend(list3)
print(list1)

#deleting data
list1.pop() #end element
print(list1)
list1.pop(3) #element by position
print(list1)
list1.remove(60)
print(list1)

print("Maximum element : ",max(list1))
print("Minimum element : ",min(list1))

list1.sort()
print(list1)

print("Length of list",len(list1))

#slicing
print(list1[0])
print(list1[5])
print(list1[-1])
print(list1[-2])

#slicing with range
print(list1[0:6])
print(list1[0:])
print(list1[:1])
print(list1[:  :  -1])