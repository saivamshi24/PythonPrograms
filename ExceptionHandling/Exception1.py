try:
    num=int(input("enter numerator"))
    den=int(input("enter denominator"))
    div=num/den
    print(div)

except ValueError as ve:
    print("you have to enter a integer value")   

except ZeroDivisionError as ze:
    print("Zero Division Error")

except Exception as e:
    print(e)

else:
    print("no exception raised")

finally:
    print("program completed")        
