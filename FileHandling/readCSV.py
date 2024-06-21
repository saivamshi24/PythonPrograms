f=open("Data.csv","r")
for line in f.readlines(): #10,Jhon,20
    data=line.split(",") #[10,Jhon,20] 
            #split converts string to list where comma is delimiter
    for index in range(len(data)): # 0,1,2
        print(data[index],end=" ")