#Factorial => 5*4*3*2*1 =>120
num=int(input("enter a number")) #5
fact=1
num1=num
while num >= 1:
    fact=fact*num #1*5 =>5*4=>20*3=>60*2=>120*1=>120
    num=num-1 #4,3,2,1,0

print("factorial of %d if %d"%(num1,fact))     